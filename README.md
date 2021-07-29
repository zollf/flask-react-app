# Flask App
Basic flask up with mvc setup, templates, testing and pipeline.

## Installation

### Install Flask
MacOS/Linux
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Windows
```bash
py -3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Install REact
```bash
yarn
```

## Start
```bash
venv\Scripts\activate
flask run
```

```bash
yarn dev
```

## Test

Run this once so that we can import the module 'app' correctly
```bash
pip install -e .
```

Then to test run
```bash
pytest
```

## Todo:
- db
- integration test
- deployment