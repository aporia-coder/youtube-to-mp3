Install locally:

Run the flowwing command to create the virtual environemt:

```
python -m venv venv
```

Run the folowing command to activate the virtual environment
you should see (venv) in the terminal if this worked correctly

```
. venv/Scripts/activate
```
Run the following command to install depenencies using pip

```
pip install -r requirements.txt
```
You are now ready to run the application

```
python app.py
```
this should run the project and you can begin using the application

To compile the project into a single.exe file you can run

```
pyinstall -F app.py
```
This will compile the application into a single .exe file inside the dist folder, you can run this without doing any of the previous set up