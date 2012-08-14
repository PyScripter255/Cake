#Cake: Python web development, simplified
##NOTE: cake test doesn't work! Will fix **very** soon.
##What is Cake?
Cake is a command-line, cross platform tool to help ease development of python web applications.
##Usage
You create a new project with Cake like this:
```
cake new test
```
What does that do? That creates a new folder (called test) in your current  directory, makes it a virtual environment (using the virtualenv.py script that can be found [here](http://pypi.python.org/pypi/virtualenv) or on github [here](https://github.com/pypa/virtualenv). It then installs web.py with pip. If you want to use another library, do so like this:
```
cake new -f [your framework] test
```
The supported frameworks are: web.py, cherrypy, bottle, tornado, and flask.
##Why don't you support (Django, Turbogear, Web2py, webapp2)?
Those frameworks have their own workflows, with scripts and projects, ect. Cake is designed to give a workflow to projects who **don't** have a set workflow, while leveraging the freedom those frameworks provide.
##Where can I get it?
You can download the zip [here](https://github.com/downloads/PyScripter255/Cake/cake.zip). It's a crossplatform executable, just add the cake folder to your path.
