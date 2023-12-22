from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def redirect_to_url():
    target_url = "https://synopsis-instrumentation-won-evans.trycloudflare.com"
    data = request.get_data()
    print(data)
    response = requests.post(target_url, data=data, headers=request.headers)
    return response
    


def server_instance():
    return app
