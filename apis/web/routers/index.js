const appRoot = require('app-root-path');

const v0 = require(`${appRoot}/apis/web/routers/v0`);

module.exports = (app) => {
  app.use(v0.routes());
  app.use(v0.allowedMethods());
  return async (ctx, next) => {
      try {
          return next();
      } catch (err) {
          return next(err);
      }
  };
};