# INSTALLATION

* Create RabbitMQ Cluster as follows:

```
	$ cd cluster
	$ sudo docker-compose up 
```

* Start Reciever workers

```
	$ python rabbit.py network1 RABBIT1
	$ python rabbit.py network2 RABBIT2
	$ python rabbit.py network3 RABBIT3
``` 

But before starting sender, you have to copy device files on <code>devs</code> folder

* Start Sender.py
```
	$ for i in {1..50}; do python sender.py -f=/home/azureuser/scagent-test/rmq/results/00s8z6256vy1gut35yip -t=5 &  done;

	# to simulate different devices events use a list of files in dirctory instead of {1..50} and substitue this value in 
	# -f option in sender.py command.

```
