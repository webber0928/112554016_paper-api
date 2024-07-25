const appRoot = require('app-root-path');
const services = require(`${appRoot}/services`);

module.exports = async (ctx, next) => {
  try {
    const res = await services.test();
    ctx.body = res;
  } catch (err) {
    return ctx.throw(err);
  }
};