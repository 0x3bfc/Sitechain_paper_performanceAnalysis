import os
import sys
from ConfigParser import ConfigParser

def configLoader(filename):
	if os.path.exists(filename):
		_config = ConfigParser()
		_config.read(filename)
		return _config._sections
	else:
		return False	
