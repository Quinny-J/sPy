# I'm still learning python. 
# Made by @Quinny-J
# 03/07/2024

# References 
# Flask - https://flask.palletsprojects.com/en/3.0.x/
# Socket - https://docs.python.org/3/library/socket.html

import socket
import subprocess
import sys
import util
from flask import Flask, request, render_template

app = Flask(__name__)


# main 
@app.route('/')
def do_index():
    print(f"{util.statusMsg.OK} sPy running"); # ignore
    return render_template('index.html', sys_uptime='yo')


