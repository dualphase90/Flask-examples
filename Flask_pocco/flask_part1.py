
from flask import Flask

app=Flask(__name__)


@app.route("/")

def helloWorld():
	return("Hello world")



if __name__=='__main__':
	app.debug = True
	app.run()