"""Publishes multiple messages to a Pub/Sub topic with an error handler."""
import time
from google.cloud import pubsub_v1
import os
import json
from flask import Flask, Response
from flask import request
import requests

# TODO(developer)
project_id = "ip-data-team-rvl"
topic_name = "pubsub-bigquery"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
app = Flask(__name__)
@app.route('/merkle-id',methods=['POST'])
def handlePost():
   send_obj = json.load(open('./schema.json'))
   recv_obj = json.loads(request.data)
   for i in recv_obj:
      send_obj[i]=recv_obj[i]
   publisher.publish(topic_path, json.dumps(send_obj).encode("utf-8"))
   print("Message published.")
   return json.dumps({'message':'success'}), 200

@app.route('/merkle-id-get',methods=['GET'])
def handleGet():
    return json.dumps({'message':'success'}), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)