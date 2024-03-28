#https://pypi.org/
#https://pypi.org/project/pwntools/

'''
1. Install python3-venv:

***** sudo apt install python3-venv *****


This command installs the python3-venv package, which is necessary for creating virtual environments.

2. Create a virtual environment:

***** python3 -m venv myenv *****

Make sure the command runs successfully without any errors.

3. Activate the virtual environment:
On Linux/macOS:

***** source myenv/bin/activate *****


On Windows:

***** myenv\Scripts\activate *****

4. Install pwntools in the virtual environment:

*****  pip install pwntools *****





Additional Notes:
Ensure that your Python version is compatible with pwntools. Sometimes, specific versions of packages may require a certain Python version.

If you still encounter issues, you may want to consider using python3 explicitly when creating the virtual environment and installing packages:


python3 -m venv myenv
source myenv/bin/activate
pip install pwntools
pip uninstall pwntools




How to Exit the Virtual Environment:

Simply run the command:


deactivate
'''