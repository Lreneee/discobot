from flask import Flask
from flask import render_template
from flask import request
import json
import webbrowser
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('discobot-ml.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        # Extract the label with the high rating
        detected = max(data, key=lambda key: data[key])
        print(detected)
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
#    app.run(host='localhost', debug=False, port=420)
#    os.system("sudo -upi chromium-browser http://localhost:8080")
    app.run(host='localhost', debug=False, port=8080)

if __name__ == '__main__':
    startInterface()
