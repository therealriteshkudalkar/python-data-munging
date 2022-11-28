# Python - Data Munging Project

To organize data, extract common code in reuseable units.

## Instructions to define a virtual environment

To define a virtual environment for current directory (project directory) use

```bash
python3 -m venv <folder_name>
```

For example:

```bash
python3 -m venv env
```

This creates a virtual environment called env in a folder named `env`. It's important to note that we must add this folder to the .gitignore file.

Next we need to activate the virtual environment. To do so, we run the following command in the project directory

```bash
source env/bin/activate
```

Note that we must be in the project directory where we defined the virtual environment for the above command to work.

## Instructions to install dependencies

The dependencies can be installed by running the following command

```bash
pip3 install -r requirements.txt
```

Remember to activate the virtual environment before you install all the dependencies

## Instructions to run

To run the project, activate the virtual environment, then run the following command

```bash
python3 main.py
```
