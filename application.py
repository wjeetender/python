from flask import Flask

application = Flask(__name__)  # IMPORTANT: variable must be named `application`

@application.route('/')
def index():
    return "Hello from Elastic Beanstalk! Prod Test"

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)  # expose externally
