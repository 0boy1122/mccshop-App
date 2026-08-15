const prisma = require("./prisma");

const STATUS_COPY = {
  CONFIRMED: { title: "Order confirmed", body: "Payment received — your order is being prepared." },
  DISPATCHED: { title: "Order on the way", body: "Your rider has picked up your order." },
  DELIVERED: { title: "Order delivered", body: "Your order has arrived. Enjoy!" },
  CANCELLED: { title: "Order cancelled", body: "Your order was cancelled and any charge was released." },
};

// Creates an in-app notification for an order status change and pushes it
// over the socket if the customer is connected right now.
async function notifyOrderStatus(io, order) {
  const copy = STATUS_COPY[order.status];
  if (!copy) return;
  const notification = await prisma.notification.create({
    data: { userId: order.userId, title: copy.title, body: copy.body, type: "ORDER", orderId: order.id },
  });
  if (io) io.to(`order:${order.id}`).emit("notification", notification);
  return notification;
}

module.exports = { notifyOrderStatus };
