from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def index():
    info = {
            'HostName': socket.gethostname(),
            'IP': socket.gethostbyname(socket.gethostname()),
    }
    return render_template('index.html', data=info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
