# Building UIs

A simple `notepad` app.

## Install

We need to setup the environment for the project. This only needs to be done
once.

```sh
# Set up a new environment
python3 -m venv env

# Activate the environment
source env/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

## Execute

We can execute the example project, after activating the environment.

```sh
# Activate the environment, if not already active
source env/bin/activate

# Run the example project
python notepad.py

# Deactivate the environment
deactivate
```

## Preview

The following screenshot is what you should see when you execute the app.

![Notepad][img-preview]

<!-- References -->

[img-preview]: ./assets/preview.png
