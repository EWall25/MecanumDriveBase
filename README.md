# Mecanum Drive Base

Simple code written using RobotPy for a mecanum drive.

## Installation

First, create a **virtual environment**. Virutal environments keep our projects seperate from each other and organized. All Python pacakges for this project will be installed inside the virtual environment.

```bash
python -m venv .venv
```

This command invokes `python`, and calls an application named `venv`. `venv` will create our virtual environment for us. We give our virtual environment a name, `.venv`.

Second, we **activate** our virtual environment.

```bash
.venv\Scripts\activate.bat
```

By running `activate.bat`, we have activated the virtual environment, and we're ready to download packages.

Packages are pieces of code written by other people that make programming easier for us. To install packages, we'll use a tool called `pip`.

Notice, a file named `requirements.txt` exists in this project. `requirements.txt` contains a list of all the packages we need for the project. There should be one package in `requirements.txt`, `robotpy`.

To install the packages...

```bash
pip install -r requirements.txt
```

The `-r` flag tells `pip` to install all the packages it finds in the file we give it (in this case, `requirements.txt`).

Once, `pip` is done installing packages, we're ready to go! Have fun coding!

## Running

To run the robot code in a simulator...

```bash
python -m robot sim
```

Recall, `python -m` calls upon python to run a program. Here, we're running the `robot.py` program.

## Deploying

To run the robot code on an actual robot...

```bash
python -m robot deploy
```