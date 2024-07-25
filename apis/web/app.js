const appRoot = require('app-root-path');

const koa = require('koa');
const app = new koa();

app.proxy = true;

const errorHandler = require(`${appRoot}/apis/web/errorHandler`);
const middlewares = require(`${appRoot}/apis/web/middlewares`);
const routers = require(`${appRoot}/apis/web/routers`);

app.use(errorHandler());
app.use(middlewares(app));
app.use(routers(app));

module.exports = app;