const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
  app.use(
    '/api',  // Specify the base URL where API requests should be redirected
    createProxyMiddleware({
      target: 'http://127.0.0.1:5000',  // Change to match your Flask server URL
      changeOrigin: true,
    })
  );
};