"""Pixel Gallery - こなぬの美術館"""
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/artworks/<path:filename>')
def artworks(filename):
    return send_from_directory('artworks', filename)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=18806, debug=False, threaded=True)
