from flask import Flask, redirect, request,session
from dotenv import load_dotenv
import requests
import os
import sys

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run()