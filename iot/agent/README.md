# README

* Sample Curl command

```
	docker run --rm appropriate/curl  'http://130.206.113.11:5000/sitewhere/api/assignments/f07901f8-9744-4289-818d-119a895424ce/invocations' -H 'Content-Length: 220' -H 'Accept-Language: en-US,en;q=0.8' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H'X-SiteWhere-Tenant: sitewhere1234567890' -H 'Connection: keep-alive' -H 'X-Requested-With: XMLHttpRequest' -H 'Content-Type: application/json' -H 'Authorization: Basic YWRtaW46cGFzc3dvcmQ='   --data-binary '{"initiator":"REST","initiatorId":"admin","target":"Assignment","commandToken":"d9332646-b074-4520-8ddb-15f920969ae8","status":"Pending","metadata":{},"parameterValues":{"greeting":"br8js0gk3r5obnkiywyj","loud":"false"}}' --compressed 

```

* Sample device startup

```

	python /opt/scagent/scagent --host=130.206.113.11 --devtoken=7dfd6d63-5e8d-4380-be04-fc5c73801dfb  --sitetoken=c2f92d04-2c8e-45c0-a6eb-dd9df4c0c6fd
```

* Start docker (device emulator)

```
	sudo docker run -d -v /home/ahmed/Desktop/scagent/:/opt/scagent aabdulwahed/sitechain:agent-test /bin/sh -c " bash /opt/scagent/start.sh ; while true; do ping 8.8.8.8 ; done"
```
