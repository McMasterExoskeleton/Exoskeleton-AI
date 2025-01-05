# Exoskeleton-AI
Main repo for Exoskeleton-AI. The goal is to train a real-time gait prediction model for use in the feedback loop
test-pr

## Prerequisite Setup
For the following commands to work we assume you have these downloaded on your system:
- python3
- make (mac or linux only)

### Linux
```
sudo apt update
sudo apt install python3 make
```
### MacOS
```
brew install make
brew install python3
```
### Windows
https://www.python.org/downloads/windows/

## Setup

### Linux / MacOS
To setup the virtual environment, run this command from the home folder of the repo:
```
make setup
```
this won't activate the venv in your terminal, but (hopefully) your IDE can find the interpreter in the venv without any additional steps. If not you can run this in order to activate the venv in your terminal. 
```
source venv/bin/activate
```

### Windows
Personally I hate developing on windows and would recommend looking into Windows Subsystem for Linux (https://learn.microsoft.com/en-us/windows/wsl/install)
```
python3 -m venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Adding Dependencies
See above on how to activate the virtual environment in your terminal, you can then run:
### Linux / MacOS
```
pip install <dependency>
make add-deps
```
### Windows
```
pip install <dependency>
pip freeze > requirements.txt
```

## Contributing Guidelines
See [here](docs/contributing.md) for extensive guidelines on how to develop, and things like commit syntax
