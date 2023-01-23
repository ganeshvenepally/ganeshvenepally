# Virtual Environment

Creating a Python virtual environment is a good practice to isolate your Python project's dependencies and avoid conflicts with other projects. Here's an example of how you can create a virtual environment using the venv module in Python 3:

## Example 
* Open a command prompt and navigate to the directory where you want to create the virtual environment.

* Run the following command to create a new virtual environment:

```
python -m venv myenv
```

This will create a new directory called "myenv" that contains the files needed for the virtual environment.

* To activate the virtual environment, run the following command:

```
myenv\Scripts\activate.bat
```

*  *Once the virtual environment is activated, you should see the name of the virtual environment in the command prompt, for example:

```
(myenv) C:\myproject>
```

*  To install packages in the virtual environment, you can use pip, for example:

```
(myenv) C:\myproject> pip install requests
```

*  To deactivate the virtual environment, you can simply run the command:

```
deactivate
```

> It's worth noting that the myenv directory is a copy of the python executable and all the standard libraries, this means that the virtual environment is not dependent of the global python installation and you can have multiple versions of a package or libraries installed.

> You can also use other tools such as conda, virtualenvwrapper, pipenv and more to manage virtual environments, each of them have its own advantages and usecases, you can refer to the documentation of the tool you choose to learn more about them.