const bcrypt = require("bcryptjs");
const prisma = require("./prisma");
const { sendSms } = require("./sms");

const OTP_TTL_MS = 10 * 60 * 1000; // 10 minutes to enter the code
const RESEND_COOLDOWN_MS = 60 * 1000; // 1 minute between sends to the same number
const MAX_ATTEMPTS = 5;

function generateCode() {
  return String(Math.floor(100000 + Math.random() * 900000));
}

// Send (or resend) a verification code. Throws { status, message } on cooldown
// or misconfiguration so routes can just forward it as an HTTP error.
async function issueOtp(phone, purpose) {
  const recent = await prisma.otpCode.findFirst({
    where: { phone, purpose, consumed: false },
    orderBy: { createdAt: "desc" },
  });
  if (recent) {
    const ageMs = Date.now() - new Date(recent.createdAt).getTime();
    if (ageMs < RESEND_COOLDOWN_MS) {
      const waitSec = Math.ceil((RESEND_COOLDOWN_MS - ageMs) / 1000);
      throw { status: 429, message: `Please wait ${waitSec}s before requesting another code` };
    }
  }

  const code = generateCode();
  const codeHash = await bcrypt.hash(code, 10);
  await prisma.otpCode.create({
    data: { phone, codeHash, purpose, expiresAt: new Date(Date.now() + OTP_TTL_MS) },
  });

  const label = purpose === "RESET_PASSWORD" ? "reset your MCC Shop password" : "verify your MCC Shop account";
  const message = `Your code to ${label} is ${code}. It expires in 10 minutes.`;

  try {
    await sendSms(phone, message);
  } catch (e) {
    // No SMS provider configured yet (dev/staging) — don't block the flow,
    // just surface the code server-side so it's still testable end to end.
    if (process.env.NODE_ENV !== "production") {
      console.warn(`[otp] SMS not sent (${e.message}). Dev code for ${phone}: ${code}`);
      return { devCode: code };
    }
    throw { status: 502, message: "Couldn't send the verification code. Please try again." };
  }
  return {};
}

// Verifies a code and marks it consumed. Throws { status, message } on failure.
async function verifyOtp(phone, purpose, code) {
  const record = await prisma.otpCode.findFirst({
    where: { phone, purpose, consumed: false },
    orderBy: { createdAt: "desc" },
  });
  if (!record) throw { status: 400, message: "No code was requested for this number" };
  if (record.expiresAt < new Date()) throw { status: 400, message: "Code expired — request a new one" };
  if (record.attempts >= MAX_ATTEMPTS) throw { status: 429, message: "Too many attempts — request a new code" };

  const match = await bcrypt.compare(String(code || ""), record.codeHash);
  if (!match) {
    await prisma.otpCode.update({ where: { id: record.id }, data: { attempts: { increment: 1 } } });
    throw { status: 400, message: "Incorrect code" };
  }

  await prisma.otpCode.update({ where: { id: record.id }, data: { consumed: true } });
}

module.exports = { issueOtp, verifyOtp };
