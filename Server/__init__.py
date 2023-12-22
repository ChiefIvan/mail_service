from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def redirect_to_url():
    target_url = "https://synopsis-instrumentation-won-evans.trycloudflare.com"
    return redirect(target_url, code=302)


def server_instance():
    return app