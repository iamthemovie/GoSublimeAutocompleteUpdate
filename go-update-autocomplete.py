import threading
import time
import os
import sublime_plugin
import subprocess
def goInstall(settings):
	try:
		iDir = settings['GOPATH'] + '/' + settings['ROOT']
		os.environ['GOPATH'] = settings["GOPATH"]
		go = settings['GOBIN'] + '/go'
		os.chdir(iDir)
		o =  subprocess.Popen([go, "install"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		p, err = o.communicate()
		print (p)
		print(err)
	except:
		return

class SaveAndGoInstall(sublime_plugin.TextCommand):
	def run(self, edit):

		self.view.window().run_command('save')
		
		# If we're not a go file then don't bother.
		if (not self.view.file_name().lower().endswith('.go')):
			return

		s = self.view.window().project_data()
		# If we don't have everything set then print a message and exit.
		# this doesn't take into account any environmental variables 
		# set outside of sublime, sorry.
		check = ['GOPATH', 'GOBIN', 'ROOT']
		for item in check:
			if not item in s['env']:
				print (item + ' not set in the project file')
				return

		t = threading.Thread(target=goInstall(s['env']))
		t.daemon = True
		t.start() 