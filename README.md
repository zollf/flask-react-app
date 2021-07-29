# Flask App
Basic flask and react app.

# Pre-installation
Before installing, please install the prerequisites for this project

| Package | Site | Guide |
| ----------- | ----------- | ----------- |
| node | https://nodejs.org/en/download/ |  https://phoenixnap.com/kb/install-node-js-npm-on-windows
| python | https://www.python.org/downloads/ | https://realpython.com/installing-python/
| yarn | after installing node run `npm install --global yarn` | https://classic.yarnpkg.com/en/docs/install/#windows-stable

# Installation

## Installing Flask
**MacOS/Linux**
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

**Windows**
```bash
py -3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Installing React
We use yarn to keep track of packages and their version. Running yarn will install all packages.
```bash
yarn
```

# Starting Up
## Installing Flask
This will start the flask server up.
```bash
venv\Scripts\activate
flask run
```

## Webpack
This will start a webpack environment that will watch for changes in `frontend/index.jsx` and minify them in `app/views/static/dist`. Which then can be imported as a script within a flask rendered template. You will have to run this in another terminal if you want both dev environments to be concurrently active.
```bash
yarn dev
```

# Running Test
## PyTest
Runs tests for flask.

Run this once so that we can import the module 'app' correctly
```bash
pip install -e .
```

Then run pytest whenever you need to test
```bash
pytest
```

## Jest
This runs test for all components within frontend/components
```bash
yarn test
```

# TODO
- db
- deployment
- integration flask tests