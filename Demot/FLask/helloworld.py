from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/<string:post>")
def show_post(post):
	return "hey, %s you shouted" % post
	
if __name__ == "__main__":
    app.run()
	