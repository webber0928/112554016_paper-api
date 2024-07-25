const appRoot = require('app-root-path');
const Router = require('koa-router');
const router = new Router({
    prefix: '/api/v0'
});

router.get('/test', require(
    `${appRoot}/apis/web/routers/v0/test`
));

module.exports = router;