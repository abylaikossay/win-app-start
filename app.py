import subprocess
from flask import Flask

app = Flask(__name__)


@app.route('/start')
def hello_world():  # put application's code here
    application_path = r'C:\Program Files (x86)\Steam\steam.exe'

    try:
        subprocess.Popen(application_path)
        return 'Application started successfully!'
    except Exception as e:
        return f'Error starting application: {str(e)}'



if __name__ == '__main__':
    app.run()
