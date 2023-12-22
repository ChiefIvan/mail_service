from flask import Flask, request
from flask_mail import Mail, Message

from matplotlib.pyplot import figure, subplot, plot, legend, tight_layout, savefig
from re import search
from .credentials import EMAIL, PASSWORD


app = Flask(__name__)
mail = Mail()

app.config["SECRET_KEY"] = "myKey888"
app.config["MAIL_SERVER"] = "smtp-mail.outlook.com"
app.config["MAIL_PORT"] = 443
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = EMAIL
app.config["MAIL_PASSWORD"] = PASSWORD

mail.init_app(app)


def smt(email_address, title, value, image_path=""):

    try:
        msg = Message(recipients=[email_address], subject=title,
                      body=value)
    
        if len(image_path) != 0:
            with app.open_resource(image_path) as image:
                msg.attach("data_report.png", "image/png", image.read())
    
        mail.send(msg)
    
        return "Email Sent"
    except ConnectionRefusedError:
        return "No connection could be made because the target machine actively refused it"
    # except Exception:
    #     return "There's an error while sending an Email!"


def visualize(log_data):

    cpu = []
    memory = []
    disk = []

    print(cpu)
    print(memory)
    print(disk)

    for line in log_data.split('\n'):
        match = search(r'Cpu: (\d+)%?, Memory: (\d+)%?, Disk: (\d+)%?', line)
        if match:
            cpu_usage, memory_usage, disk_usage = match.groups()
            cpu.append(int(cpu_usage))
            memory.append(int(memory_usage))
            disk.append(int(disk_usage))

    figure(figsize=(10, 6))
    subplot(3, 1, 1)
    plot(cpu, label='CPU Usage')
    legend()
    subplot(3, 1, 2)
    plot(memory, label='Memory Usage')
    legend()
    subplot(3, 1, 3)
    plot(disk, label='Disk Usage')
    legend()
    tight_layout()

    savefig("data.png")


@app.route("/", methods=["POST"])
def index():
    data = request.json
    if log_Data := data["data"]:
        visualize(log_Data)
        response = smt(data["email"], data["title"],
                       data["value"], image_path="data.png")
    else:
        response = smt(data["email"], data["title"],
                       data["value"])
    return response


def server_instance():
    return app

