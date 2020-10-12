from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return 'heyyyy'


@app.route('/health')
def health():
  return 'Healthy'