# Flask App

## Start

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

## Test

Run this once so that we can import the module 'app' correctly
```bash
pip install -e .
```

Then to test run
```bash
pytest
```