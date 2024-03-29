# save list of installed packages to file -> should be edited for necessary packages only
python -m pip freeze > requirements.txt

# create virtual python environment from existing installation
python3.10.0 -m venv venv

# activate (posix)
source ./venv/bin/activate

# activate (windows)
# venv\Scripts\activate

# install requirements
python -m pip install -r requirements.txt

# deactivate (posix/windows)
deactivate
