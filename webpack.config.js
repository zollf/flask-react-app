const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./frontend/index.jsx",
  output: {
    path: path.resolve(__dirname, "./app/views/static/dist"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
};