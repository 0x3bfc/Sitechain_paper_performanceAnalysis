#!/bin/bash
for i in {1..50}
	do

	sudo docker run -d -v $1/:/opt/scagent aabdulwahed/sitechain:agent-test /bin/sh -c " bash /opt/scagent/start.sh ; while true; do ping 8.8.8.8 ; done"

done

