// Special handling for Stripe Webhook (needs raw body for signature verification)
app.post('/api/stripe/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;

    try {
        event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
    } catch (err) {
        console.error(`Webhook Error: ${err.message}`);
        return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    // 1. Phản hồi ngay cho Stripe
    res.json({ received: true });

    // 2. Xử lý logic ngầm - Không dùng await ở cấp độ cao nhất này 
    // để tránh làm treo hàm callback nếu có vấn đề gì đó
    if (event.type === 'checkout.session.completed') {
        // Gọi một hàm async riêng để xử lý mà không chặn luồng chính
        handleBookingAsync(event.data.object);
    }
});

// Tách hàm xử lý ra riêng cho sạch code
async function handleBookingAsync(session) {
    const bookingData = session.metadata;
    try {
        console.log('Processing background tasks for:', bookingData.clientName);

        const authClient = await getAuthClient();
        const calendar = google.calendar({ version: 'v3', auth: authClient });

        // ... (Logic tạo thời gian) ...

        await calendar.events.insert({
            // ... (Cấu hình calendar) ...
        });

        // Đảm bảo trong hàm này đã fix lỗi family: 4 (IPv4)
        await sendConfirmationEmail(bookingData);

        console.log('✅ All tasks completed.');
    } catch (error) {
        console.error('❌ Background Task Error:', error.message);
    }
}