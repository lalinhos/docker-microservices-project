from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = os.environ.get('HOSTNAME', 'Unknown Host')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Hello from Server! Container: {hostname} at {timestamp}"
    print(f"Request received from client. Response: {message}")
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
