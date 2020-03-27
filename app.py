from flask import Flask, redirect
from modules import module_device, module_handle, module_lan, module_server

app = Flask(__name__, static_folder='static', static_url_path='')
app.register_blueprint(module_device)
app.register_blueprint(module_handle)
app.register_blueprint(module_lan)
app.register_blueprint(module_server)


@app.route('/')
def index():
    return redirect('/index.html', code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
