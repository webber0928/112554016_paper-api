const appRoot = require('app-root-path');

// Load environment variables
const envPath = `.env.${process.env.NODE_ENV ?? 'localhost'}`;
require('dotenv').config({ path: envPath });

// Load the app
const api = require(`${appRoot}/apis/web/app.js`);

// Start the app
const port = process.env.PORT ?? 6666;
api.listen(port);
console.log(`🚀 web api running on port ${port} 🚀`);