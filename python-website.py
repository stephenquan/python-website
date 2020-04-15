from flask import Flask, request, send_from_directory, json

app = Flask(__name__)

@app.route("/")
def website_index():
    return send_from_directory('website', 'index.html')

@app.route('/<path:path>')
def website_path(path):
    return send_from_directory('website', path)

if __name__ == "__main__":
    app.run()
