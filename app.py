# I'm still learning python. 
# Made by @Quinny-J
# 03/07/2024

# References 
# Flask - https://flask.palletsprojects.com/en/3.0.x/
# Socket - https://docs.python.org/3/library/socket.html

from concurrent.futures import ProcessPoolExecutor
import socket
import subprocess
import sys
import util
import pscan
from flask import Flask, request, render_template

app = Flask(__name__)
sanz = pscan.pscan


# main 
@app.route('/')
def do_index():
    print(f"{util.statusMsg.OK} sPy running"); # ignore
    return render_template('index.html', sys_uptime='yo')

@app.route("/spy-api/", methods=['POST', 'GET'])
def do_scan_queue():
    # Basic error handling fixes a web error you get when throttling
    try:
        # Get request data
        server_data = request.form.get('server_address')
        # Split the data 0.0.0.0:80 becomes two items
        server_data_splt = server_data.split(":")
        # Call my function and return result
        return render_template('index.html', sPy_response=sanz.do_sing_scan(server_data_splt[0], server_data_splt[1]))
    except:
            return "An exception occurred"


