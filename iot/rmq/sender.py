#!/usr/bin/env python
import os
import sys
import pika
import subprocess
import threading
from datetime import datetime

def sendPayload(message, network, host, port, username, password, channel, connection):

	channel.basic_publish(exchange='',
                      routing_key=network,
                      body=message,
		      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

	print " [x] Sent '%s'"%(message)
	connection.close()


def timeLogger(message):
	timenow = (datetime.utcnow()-datetime.fromtimestamp(0)).total_seconds()
	#raise Exception(timenow)
	with open('%s/results/%s'%(os.path.dirname(os.path.abspath(__file__)), message), 'w+') as f:
		f.write(str(timenow))

def testSender(host, ports, networks,files, username, password, channel, connection, iters=1):
	l = len(networks)
	n = 0
	for t in range(iters):
		for f in files:
			timeLogger(f)
			#print f, networks[n], host, ports[n], username, password
			sendPayload(f, networks[n], host, ports[n], username, password, channel, connection)
			n +=1
			if n == len(networks):
				n = 0

def startSenderThread(num, device, ip, port, network, username, password):
	credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip, port=port, credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=network,  durable=True)

	th = threading.Thread(target=testSender, args=(ip, [port], [network], [device], username, password, channel, connection))
	th.daemon = True
	th.start()
	th.setName('Thread #%d for Device: %s'%(num, device))


def parseDevicesFile(devfile):
	#try:
		with open(devfile, 'r') as f:
			devices = f.readlines()
		return devices[0]
	#except:
	#	return None
	
if __name__ == '__main__':
	args = sys.argv
	"""
		ARG1: IP ADDRESS
		ARG2: PORT NUMBER
		ARG3: NETWORKS ... THEY ARE COMMA SEPARATED
		ARG4: NUMBER OF THREADS
		ARG5: USERNAME DEFAULT: GUEST
		ARG6: PASSWORD DEFAULT: GUEST
	"""
	networks = ['network1']
	threads = 5
	username = 'guest'
	password = 'guest'
	ip = '130.206.113.11'
	port = 5672
	for arg in args:
		if '-h=' in arg:
			ip = arg.split("=")[1]
		if '-p=' in arg:
			port = int(arg.split("=")[1])
		if '-n=' in arg:
			networks = arg.split("=")[1]
			try:
				networks = netowkrs.split(',')
			except:
				networks = [networks]
		if '-t=' in arg:
			threads = int(arg.split("=")[1])
		if '-f=' in arg:
			devfile = arg.split("=")[1]
	
	devices = parseDevicesFile(devfile)
	if devices:
		try:
			devices = devices.split(',')
		except:
			devices = [devices]
		for dev in devices:
			dev = dev.replace('\n','')
			network = 0
			for n in range(threads):
				#print n, dev, ip, port, networks[network], username, password
				startSenderThread(n, dev, ip, port, networks[network], username, password)
				if network+1 < len(networks):
					network +=1
				
				
			
"""
testSender('130.206.113.11',[5672, 5673, 5674], ['network1', 'network2', 'network3'] , ['00s8z6256vy1gut35yip','640xj3pirkyz088d5wbn','ci9kpb7lvxucy4x4iy02','kgyjzcbvugoq5bf3jdys','qptek5ye1wjstjmjgnyi','0zo24mw7lwtxjbu7s8wk','6luak9f2jngh5dqiyp40','daecnvcnasqcu2nbmo83','knwho9c4b1dmjrldnaz3','vjtpw2ohy8tnjoxzcncm','2uiw4hcwwtaa8rtb6au0','8df3f10gohh01sgumolc','e274p6nbxa82g9qwbqwp','kzvzyl0qsunxgnbwy8tz','wx8gdr8tjouac49331dx','316zj9mpqmnhpimunp2o','9790ptnovt86w4yaq1dm','g9sr8xf2gb9d6a3f31vb','l6e8d04n4pbkmatk80x7','zca8sp1pfabx4t5zjtrn','3ru0m2fwwnzpqzqytlgw','9ynv5dkwf71088d46tjz','hdhnkj6jxgfz9lqtyrza','mg5dbgj6zgq2tfy27wrr','zjua7h0xilpvh5iusrlj','43hwiua28f3vr36zr0b7','ayqen42e0y8x2dguziii','hwa8ric7vsyk3gz4arin','my416mvowdqvgbz5qupf','4jrkq1nrojd5e1codyht','bjuzw134ze1pkc42n55i','kb677dz1ppu7de0xjqgt','pu6xn9vd3n9oveuimizq'], 'guest', 'guest', iters=100)

"""	
