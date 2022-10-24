# checklist

## for running off CMD line

- create a new assignment folder
- navigate `into` which assignment you will be working on
- create your virtual env

`-m pipenv install flask`
Every time you open that new project folder

*you must run* ` python -m pipenv install flask flask-bcrypt `
**WARNING** Your directory needs to contain ` Pipfile.lock ` and ` Pipfile `
**WARNING** otherwise your shell will not build or run

- navigate CMD Terminal into virtual environment or shell

`python -m pipenv shell`

- Folder Structure
    -Pipfile
    -Pipfile.lock
    -server.py
    -templates
    -static

*******************************************************************************

1. Navigate to the level you want to create your new project directory
2. `mkdir [name_of_project]`
3. `cd [name_of_project]`
4. `mkdir flask_app`
5. `type nul > server.py`
    a. this has a snippet
6. `cd flask_app`
7. Create these directories inside flask_app
   1. `config`
      1. this has a snippet
   1. `controllers`
   1. `models`
   1. `static`
   1. `templates`
8. and your dunder_init file
`type nul > __init__.py`
   1. this has a snippet
9. Continue to use snippets to build out your controllers & models
`type nul > [filename]`
