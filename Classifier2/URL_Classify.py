from Cymon_API import *
from FeatureExtraction import *
from flask import Flask
from flask import request
import numpy as np
from joblib import dump, load

app = Flask(__name__)

host = '0.0.0.0'
port = 5000

#Returns False for good websites, and True for bad websites
def classify(url):
    f = np.array(getFeatures(url))
    clf = load('AlexaDecisionTree.joblib')
    out = clf.predict(f.reshape(1,-1))
    return not out

@app.route("/")
def respond():
    #ip_result = check_IP(request.args.get('ip', default = '', type = str))
    result = classify(request.args.get('url', default = '', type = str))
    return str(result)


if __name__ == '__main__':
    app.run(host=host, port=port,debug = True)