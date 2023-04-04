import os
from werkzeug.security import safe_join
from flask import *

class Reply:
    def __getattr__(self, name):
        match name:
            case "ok":
                return Response(status=200)
            case "error404":
                return jsonify({'error': 'Not found'}), 404
            case "errorCringe":
                return jsonify({'error': 'L+ratio+you fell off'}), 500
Reply = Reply()

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def route(path):
    if path in "/":
        path = "index.html"
    path = safe_join(app.static_folder, path)
    if path is None:
        return Reply.errorCringe
    if os.path.isfile(path):
        return send_file(path)
    elif os.path.isdir(path):
        return jsonify(os.path.listdir(path))
    return Reply.error404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')