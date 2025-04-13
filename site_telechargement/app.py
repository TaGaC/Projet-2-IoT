from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/AdFree.apk')
def download_apk():
    return send_from_directory('.', 'ad_free.apk', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

