import datetime
import socket

from flask import Flask, jsonify

app = Flask(__name__)

"""
/api/v1/details
"""
@app.route('/api/v1/details', methods=['GET'])

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
    }), 200


"""
/api/v1/health
"""
@app.route('/api/v1/health', methods=['GET'])

def health():
    return jsonify({'status': 'OK'}), 200



if __name__ == '__main__':
    app.run()