// Hubtel "Quick Send" SMS API. Base URL is env-overridable (HUBTEL_SMS_URL)
// in case Hubtel's documented host changes — verify against a real account's
// docs before the first live send, this wasn't reachable to double-check
// directly while building it.
const HUBTEL_URL = process.env.HUBTEL_SMS_URL || "https://api.hubtel.com/v1/messages/send";

async function sendSms(to, content) {
  const clientId = process.env.HUBTEL_CLIENT_ID;
  const clientSecret = process.env.HUBTEL_CLIENT_SECRET;
  const from = process.env.HUBTEL_SENDER_ID || "MCCShop";

  if (!clientId || !clientSecret) {
    throw new Error("SMS is not configured (missing Hubtel credentials)");
  }

  const auth = Buffer.from(`${clientId}:${clientSecret}`).toString("base64");
  const res = await fetch(HUBTEL_URL, {
    method: "POST",
    headers: {
      Authorization: `Basic ${auth}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ From: from, To: to, Content: content }),
  });

  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(data.Message || data.message || "Failed to send SMS");
  }
  return data;
}

module.exports = { sendSms };
