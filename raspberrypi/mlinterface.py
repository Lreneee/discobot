from flask import Flask
from flask import render_template
from flask import request
import json
import os
# import discobotapp

import dataqueue

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('discobot-ml.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.get_json()
        # discobotapp.fillMusicData(data)  
        # Extract the label with the high rating
        detected = max(data, key=lambda key: data[key])
        #print(detected)
        dataqueue.enterData(detected)
        # Save entire dataset to .txt
        """
        with open("./Flask app/data.txt", 'w', encoding='utf-8') as f:
            f.write(
                str(data)
            )
            f.close()
        """
    return ""

def startInterface():
    app.run(host='localhost', debug=False, port=420)
    
def terminate():
    print("mlinterface terminate test")
    
if __name__ == '__main__':
    startInterface()
