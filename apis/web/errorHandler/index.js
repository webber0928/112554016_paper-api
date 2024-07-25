const appRoot = require('app-root-path');

const errorFormat = require(`${appRoot}/apis/web/errorHandler/errorFormat`);
const PrettyError = require('pretty-error');
const prettyError = new PrettyError();
prettyError.withoutColors();
prettyError.skipPackage(
    'koa-compose',
    'koa-router',
    'koa2-cors',
    'koa-body',
    'koa-logger',
    'jsonwebtoken',
    'bluebird'
);

module.exports = () => {
    return async (ctx, next) => {
        try {
            await next();
        } catch (err) {

            const sequelizeValidationError = err.name === 'SequelizeValidationError' ? {
                code: -2,
                status: 503,
                message: err.errors[0]?.message
            } : null;

            let customError = errorFormat[err.message] ?? sequelizeValidationError ?? errorFormat['1000'];
            let errorResponse = {};
            errorResponse.code = customError.code;
            errorResponse.status = customError.status;
            errorResponse.message = customError.message;

            if (customError.code) {
                console.log(`---------- ERROR ----------`);
                console.log(`code: ${errorResponse.code}`);
                console.log(`message: ${errorResponse.message}`);
                console.log(`status: ${errorResponse.status}`);
                console.log(`stack:`);
                console.log(prettyError.render(err));
                console.log(`---------- ERROR ----------`);
            }

            ctx.status = errorResponse.status;
            return (ctx.body = errorResponse);
        }
    };
};
