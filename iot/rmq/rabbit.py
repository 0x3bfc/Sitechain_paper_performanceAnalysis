#!/usr/bin/env python
import os
import pika
import config as conf
import request
import rmq
import json

def receiver(queue, server):
	# main consumer function
	channel, connection = rmq.get_channel(queue, server)

	print(' [*] WORKER -- Waiting for messages. To exit press CTRL+C')

	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(callback,
                      queue=queue)
	
	channel.start_consuming()


def getDevToken(body):
	return body

def getDeviceSpecs(devtoken):
	try:
		with open('%s/devs/%s'%(os.path.dirname(os.path.abspath(__file__)), devtoken), 'r') as f:
			lines = f.readlines()
		return lines[0].replace(' ','').replace('\n','')
	except:
		return False

def callback(ch, method, properties, body):
	print " [*] WORKER: INFO -- Starting worker"
	print " [*] WORKER: INFO -- send body to sitewhere"
	print " [*] BODY: %s" %(body)
	devtoken = getDevToken(body)	
	
	assignment = getDeviceSpecs(devtoken)

	# prepare header 
	header = {
			"Authorization": "Basic YWRtaW46cGFzc3dvcmQ=",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "en-US,en;q=0.8",
			"X-SiteWhere-Tenant": "sitewhere1234567890",
			"Content-Type": "application/json",
			"Accept": "application/json, text/javascript, */*; q=0.01",
			"X-Requested-With": "XMLHttpRequest",
			"Connection": "keep-alive"
		}

	config = conf.configLoader('%s/config.conf'%(os.path.dirname(os.path.abspath(__file__))))	

	ip_address = config['SITEWHERE']['ipaddr']
	commandtoken = config['SITEWHERE']['commandtoken']
	print commandtoken, devtoken, assignment
	if assignment:
		sender = request.Request('http://%s:5000/sitewhere/api/assignments/%s/invocations'%(ip_address, assignment))
	
		data = {"initiator":"REST","initiatorId":"admin","target":"Assignment","commandToken":commandtoken,"status":"Pending","metadata":{},"parameterValues":{"greeting":devtoken,"loud":"false"}}
		data = json.dumps(data)
		

		print " [*] WORKER: INFO -- send data to sitewhere"
		res =  sender.sendPostRequest(header, data)
		print res
	ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__ == '__main__':
	import sys
	args = sys.argv
	network = args[1]
	host 	= args[2]
	receiver(network, host)
