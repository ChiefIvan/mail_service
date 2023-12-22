from flask import Flask, request
from requests import post

app = Flask(__name__)

@app.route("/", methods=["POST"])
def redirect_to_url():
    target_url = "https://synopsis-instrumentation-won-evans.trycloudflare.com"
    data = request.get_data()
    headers = {
        "Content-Type": "application/json",
    }  
    
    response = post(target_url, data=data, headers=headers)
    return "Sent"
    


def server_instance():
    return app
