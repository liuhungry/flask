from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """<h1>Hello World</h1>
<p>Hello World Hello World Hello World</p>
"""

app.run()