from flask import Flask

application = Flask(__name__)  # AWS looks for `application` by default

@application.route('/')
def hello():
    return "Hello from Elastic Beanstalk!"

if __name__ == '__main__':
    application.run(debug=True)
