from flask import Flask, jsonify, request
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def test():

    data = request.get_json()

    target = data.get("target")
    port = data.get("port")
    
    if not target or not port:
        return jsonify({
            "message": "remplir le champ"
        })
    try:
        port = int(port)

    except:
        return jsonify({
            "message": "mets un nombre valide"
        }), 400

    s = socket.socket()

    s.settimeout(4)

    result = s.connect_ex((target, port))

    s.close()

    if result == 0:

        return jsonify({
            "message": f"le port {port} est ouvert sur {target}"
        }), 200

    else:

        return jsonify({
            "message": f"le port {port} est fermé"
        }), 404


if __name__ == "__main__":
    app.run(port=3000, debug=True)
