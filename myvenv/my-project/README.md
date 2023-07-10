data : input/output data

docs : helper docs for each functionality

src
    scripts : code to create documentation from given user input
    templates : html files to generate the UI

tests : unit test data and results 

.gitignore : files to ignore when committing project to the GitHub repository

pyproject.toml - equivalent to setup.py

README.md : overview

requirements.txt : contain precise versions of all installed packages, and you can use these files to freeze the requirements of an environment. Using precise versions, you can easily reproduce your environment on another system.

*********************************************************************

https://speakerdeck.com/bachmann1234/structuring-your-python-project

*********************************************************************

Install requirements from a file
pip install -r <requirement_file>

List installed packages
pip freeze

*********************************************************************

create virtual env
python -m venv <env_name>

activate virtual env
.\<env_name>\scripts\activate

*********************************************************************
