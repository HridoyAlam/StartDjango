# StartDjango
### Creating virtual environment
python -m venv new_project,
cd new_project,
On Windows, you can run: Scripts\activate.bat, 
On Unix or macOS, run: source bin/activate,

### specifies a particular version of a package:
pip install package_name==package_version
### shows the detailed information about a package
pip show package_name
### displays the installed packages:
pip list
### To create a requirements.txt file
pip freeze > requirements.txt
### delete the directory.
Unix or macOS run:
rm -r new_project

for Windows:
rmdir new_project


##### if else in one line/ terminoary operator
first_alternative if condition else second_alternative
