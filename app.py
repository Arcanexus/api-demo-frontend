from datetime import datetime
from flask import Flask, render_template, request, send_from_directory
import requests, json, os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  HTTPMethod = ''
  targetURL = ''
  payload = ''
  result = ''

  if request.method == 'POST':
    HTTPMethod = request.form.get('HTTPMethod')
    targetURL = request.form.get('targetURL')
    try:
      # payload = json.loads(request.form.get('payload'))
      payload = request.form.get('payload')
    except:
      payload = '{}'
    
    
    match HTTPMethod:
      case "GET":
        result = requests.get(targetURL)
      case "POST":
        result = requests.post(targetURL, data=payload) # , data=json.dumps(payload))
      case "PUT":
        result = requests.put(targetURL, data=payload)
      case "PATCH":
        result = requests.patch(targetURL, data=payload)
      case "DELETE":
        result = requests.delete(targetURL, data=payload)
      case _:
        return "ERROR, HTTP Method not in (GET, POST, PUT, PATCH, DELETE)", 400

    # return '''
    #           <h1><u>Request:</u></h1>
    #           <h2>HTTP Method: {}</h2>
    #           <h2>Target URL: {}</h2>
    #           <h2>Payload: {}</h2>
    #           <hr \>
    #           <a href="javascript:history.back()">Go Back</a><br \>
    #           <h1><u>Result:</u></h1><h2> {} {}<p>Content:</h2></p>
    #           {}'''.format(HTTPMethod, targetURL, payload, result.status_code, result.reason, result.text)
  # print('Request for index page received')
  return render_template('index.html', HTTPMethod=HTTPMethod, targetURL=targetURL, payload=payload, result=result)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)