from Cymon_API import *
from flask import Flask
from flask import request
app = Flask(__name__)

host = '0.0.0.0'
port = 5000

#Returns False for good websites, and True for bad websites
def check_IP(ip):
    data = ip_events(ip)
    if data == None:
        return False
    elif data["count"]>0:
        return True
    else:
        return False

@app.route("/")
def respond():
    ip_result = check_IP(request.args.get('ip', default = '', type = str))
    return str(ip_result)


if __name__ == '__main__':
    app.run(host=host, port=port)

#Example malicious ip = 5.248.253.190
