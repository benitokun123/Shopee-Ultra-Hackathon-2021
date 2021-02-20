const merge = require('webpack-merge');
const common_config = require('./base.config.js');

var path = require('path');
module.exports = (env) => {
  return merge(common_config(env), {
    mode: 'development',
    devtool: 'source-map',
    module: {
      rules: [
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
          include: [
            path.join(__dirname, 'src'),
            /node_modules/
          ],
        },
      ]
    },
    devServer: {
      hot: true,
      proxy: {
        '/api/': {
          target: 'https://api.hackathon2021.shopee.sg',
          pathRewrite: {
            '^/api/': '/'
          },
          secure: false,
          changeOrigin: true, // for CORS
        },
      },
    },
  });
};