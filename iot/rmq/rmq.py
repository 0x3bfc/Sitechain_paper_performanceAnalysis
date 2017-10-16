import os
import pika
import config as conf
import request
import rmq

def load_configurations(server):
        config = conf.configLoader('%s/config.conf'%(os.path.dirname(os.path.abspath(__file__))))

        return (config['CONNECTION']['username'],
                config['CONNECTION']['password'],
                config['CONNECTION']['host'],
                config[server]['port']
        )



def get_channel(queue, server):
        username, password, host, port = load_configurations(server)
        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host, int(port), credentials=credentials, heartbeat_interval=0))
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        return (channel, connection)

