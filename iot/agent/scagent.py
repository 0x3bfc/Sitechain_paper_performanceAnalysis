import os
import sys
import random
import getpass
import random, string
import subprocess

def generate_config_file(args):
	devname = None
	devtoken = None
	sitetoken = None
	host =None
	devId =  ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(20))
	for arg in args:
		if '--host' in arg:
			hostname = arg.split('=')[1]
		if '--devtoken' in arg:
			devtoken = arg.split('=')[1]
		if '--sitetoken' in arg:
			sitetoken = arg.split('=')[1]
		if '--devname' in arg:
			devname = arg.split('=')[1]
	if not devname:
		devname = devId
	if not devtoken or not sitetoken or not hostname:
		return None
	else:
		data = 'SitwherIP=%s\nmqtt.hostname=%s\ncommand.processor.classname=com.agentcommandprocessor.SitechainAgentCommandProcessor\ndevice.hardware.id=%s\ndevice.specification.token=%s\nsite.token=%s\ndevice.metadata.name=name\ndevice.metadata.value=%s'%(hostname, hostname,devId, devtoken, sitetoken, devname)
		pwd = os.path.dirname(os.path.abspath(__file__))
		with open('%s/config/config.properties'%(pwd), 'w') as conf:
			conf.write(data)
		return '%s/config/config.properties'%(pwd)

 
def execute(command):
	pipe = subprocess.PIPE
	p = subprocess.Popen("sudo -H -u %s bash -c  '%s'"%( getpass.getuser(),command),shell=True)
	return p
 

if __name__=="__main__":
	if len(sys.argv) < 4:
		print "ERROR!"
		sys.exit()
	else:
		conf = generate_config_file(sys.argv)
		if conf:
			command = "java -jar /opt/scagent/sitechainagent.jar %s"%(conf)
			execute(command)
			sys.exit()
		else:
			print "ERROR -- Unable to generate config file"
