
## Installation


## Setup


```sh
conda create -n rps-flask-env python=3.7 # first time only
conda activate rps-flask-env
```

```sh
pip install -r requirements.txt
```

## Usage

Run a local web server, then view your app in a browser at http://localhost:5000/:

```sh
# Mac Terminal:
FLASK_APP=web_app flask run

# Windows Command Prompt:
set FLASK_APP=web_app
flask run
```

> NOTE: you can quit the server by pressing ctrl+c at any time. If you change a file, you'll likely need to restart the server for the changes to take effect.
