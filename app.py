from Server import server_instance
app = server_instance()

if __name__ == "__main__":
    app.run(debug=True)