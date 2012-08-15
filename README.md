#Cake: Python web development, simplified
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
You can install it from [here](https://github.com/PyScripter255/Cake/downloads). It works on [Windows](https://github.com/downloads/PyScripter255/Cake/cake.zip) and [Linux](https://github.com/downloads/PyScripter255/Cake/LinuxCake.zip) . It's a crossplatform executable, just add the cake folder to your path.
##What's the license?
Cake is currently public domain (that may change, but everything you make with cake will always be your own).
##Documentation
Right [here](https://github.com/PyScripter255/Cake/wiki/Tutorial) in the wiki.