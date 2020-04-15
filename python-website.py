from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route("/")
def website_index():
    return send_from_directory('.', 'index.html')

@app.route('/website/<path:path>')
def website_path(path):
    return send_from_directory('website', path)

if __name__ == "__main__":
    app.run()
