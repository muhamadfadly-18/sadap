from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/ig')
def track_and_redirect():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Simpan data ke file
    with open('log.txt', 'a') as f:
        f.write(f"{access_time} | IP: {ip_address} | Agent: {user_agent}\n")

    # Ganti dengan link IG kamu
    return redirect("https://www.instagram.com/fadly.di")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
