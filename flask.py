from flask import Flask, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/image', methods=['GET'])
def get_image():
    img_url = request.args.get('img')
    
if __name__ == '__main__':
    app.run(debug=True)
