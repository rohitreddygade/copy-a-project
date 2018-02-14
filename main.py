from flask import Flask
app = Flask(__name__)

app.route('/')
def hoem():
	return "<center><h1>This is Home Page Site is under developement</h1></center>"

# test server configurations

if __name__ =='__main__':
	app.run(host="0.0.0.0",port=80)