from flask import Flask
from flask import render_template
from flask import request
import json
import os

import dataqueue
import discobotapp

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('discobot-ml.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.get_json()
        discobotapp.fillMusicData(data)
    
        # Extract the label with the high rating
        detected = max(data, key=lambda key: data[key])
        dataqueue.enterData(detected)
       
    return ""

def startInterface():
    app.run(host='localhost', debug=False, port=420)
    

if __name__ == '__main__':
    startInterface()
