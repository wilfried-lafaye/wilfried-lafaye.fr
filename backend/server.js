const express = require('express');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 4000;

// Enable CORS for all routes
app.use(cors());

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.json({ status: 'ok' });
});

app.listen(port, () => {
    console.log(`Backend server listening on port ${port}`);
});
