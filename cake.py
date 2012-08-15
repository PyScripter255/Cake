#!/usr/bin/env python
import sys, os, cmdln

class Cake(cmdln.Cmdln): # Main class, defines the tool
	s = os.sep
	name = "cake" # The name of the tool is cake
	@cmdln.option("-f", "--framework", help="Choose a framework to be installed to your app directory.") # Adds the framework option to new
	def do_new(self, subcmd, opts, newApp):  # Defines cake new
		"""${cmd_name}: Creates a new application. Creates the directory, makes it a virtualenv, and installs the library of your choice. Default is web.py 

    	${cmd_usage}
    	${cmd_option_list} """# The help prompt
		print "Creating Directory..."
		os.system('mkdir'+' '+newApp)#Creates the app directory
		os.system('python virtualenv.py'+' '+newApp)# Makes the directory a virtualenv
		framework = {None: 'web.py', # Defines the possible frameworks
				 'web.py': 'web.py',
			     'bottle':'bottle',
			     'tornado': 'tornado',
			     'cherrypy': 'cherrypy',
			     'flask': 'flask'
			     }.get(opts.framework, None)
		if not framework:#Checks if the framework is valid
			 print "Invalid Framework"
		else:#Sets up the framework
			print "Setting up "+framework+"..."
			if os.name != "nt":
				os.system(newApp+os.sep+"bin"+os.sep+"pip install "+framework)# Installs the framework
			else:
				os.system(newApp+os.sep+"Scripts"+os.sep+"pip.exe install "+framework)#Installs the framework
			
			sys.path.append(newApp)#Adds folder to the PYTHONPATH
			# Possible create info file: open(newApp+'\.cakeinfo.txt', 'w').write('{"module":"'+framework+', "name" : "'+newApp+'"}')
		print "Done"
	@cmdln.option("-p", "--port", help="Choose a port to be passed as an argument to the python file.")
	def do_test(self, subcmd, opts, module="main.py"):
		"""${cmd_name}: Tests your application by running the main python file. The file to test by default is main.py. You can define an optional file to test.
		Usage:
		cake test [OPTIONAL MODULE]\n
		${cmd_option_list}"""
		if os.name == "nt":
			os.system("Scripts\python.exe "+module+" "+str(opts.port))
		else:
			os.system("bin/python.exe "+module+" "+str(opts.port))			
if __name__ == "__main__":
    cake = Cake()
    sys.exit( cake.main() )
