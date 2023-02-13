from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests, json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    HTTPMethod = request.form.get('HTTPMethod')
    targetURL = request.form.get('targetURL')
    payload = json.loads(request.form.get('payload'))
    
    match HTTPMethod:
      case "GET":
        result = requests.get(targetURL)
      case "POST":
        result = requests.post(targetURL, data=json.dumps(payload))
      case "PUT":
        result = requests.put(targetURL, data=json.dumps(payload))
      case "PATCH":
        result = requests.patch(targetURL, data=json.dumps(payload))
      case "DELETE":
        result = requests.delete(targetURL, data=json.dumps(payload))
      case _:
        return "ERROR, HTTP Method not in (GET, POST, PUT, PATCH, DELETE)", 400
    
    return '''
              <h1><u>Request:</u></h1>
              <h2>HTTP Method: {}</h2>
              <h2>Target URL: {}</h2>
              <h2>Payload: {}</h2>
              <hr \>
              <a href="javascript:history.back()">Go Back</a><br \>
              <h1><u>Result:</u></h1><h2> {} {}<p>Content:</h2></p>
              {}'''.format(HTTPMethod, targetURL, payload, result.status_code, result.reason, result.text)
   
  print('Request for index page received')
  return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
   app.run()