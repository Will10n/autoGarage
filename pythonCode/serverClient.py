import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import csv
import threading

class serverClient:
     def __init__(self):
          self.config = {}
          with open("config.csv.txt", mode='r') as file:
               reader = csv.DictReader(file)
               for row in reader:
                    self.config[row['key']] = row['value']
          self.client = None
          self.running = False

     def MQTTConnect(self):

          print("Configuring MQTT Client")
          self.client = AWSIoTMQTTClient(self.config["client_id"])
          self.client.configureEndpoint(self.config["endpoint"],8883)
          self.client.configureCredentials(self.config["root_ca"], self.config["private_key"], self.config["certificate"])
          self.client.configureOfflinePublishQueueing(-1)
          self.client.configureDrainingFrequency(2)
          self.client.configureConnectDisconnectTimeout(10)
          self.client.configureMQTTOperationTimeout(5)

     def start_polling(self):
          print("Connecting to client...")
          self.client.connect()
          self.client.subscribe(topic=self.config["topic"], QoS=1, callback=self.callback)
          print("Subscribed to topic")

          print("Polling for messages...")
          self.running = True
          threading.Thread(target=self.polling_thread,daemon=True).start()

     def polling_thread(self):
          while self.running:
               time.sleep(5)
     
     def stop_polling(self):
          print("Disconnecting...")
          self.running= False
          self.client.disconnect
          print("Disconnected")
     
     
     def callback(self, client, userdata, message):
          print("Received Message From AWS IoT Core")
          print(f"Topic: {message.topic}")
          print(f"Payload: {message.payload.decode('utf-8')}")


     
def main():

     client = serverClient()
     client.MQTTConnect() # connect to IoT cloud
     client.start_polling() # start polling for messages

     try:
          print("Client running. Press Ctrl+C to exit.")
          while True:
               time.sleep(1)  # Main thread can perform other tasks if needed
     except KeyboardInterrupt:
          print("\nStopping services...")
          client.stop_polling()
          print("Exited.")

if __name__ == "__main__":
     main()




