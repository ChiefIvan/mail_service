from flask import Flask, request
from requests import post

app = Flask(__name__)

@app.route("/", methods=["POST"])
def redirect_to_url():
    target_url = "https://replace-briefly-motion-cricket.trycloudflare.com"
    data = request.get_data()
    headers = {
        "Content-Type": "application/json",
    }  

    try:
        response = post(target_url, data=data, headers=headers)
    except:
        return "Mail Service is offline, Please try again later"

    return response.text
    


def server_instance():
    return app
