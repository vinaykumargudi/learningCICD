from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    private_ip = socket.gethostbyname(socket.gethostname())
    return f"Hello world, I am {private_ip}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
