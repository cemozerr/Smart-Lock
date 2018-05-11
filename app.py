from flask import send_from_directory
from flask import Flask

app = Flask(__name__)

@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory('/Users/CemosBeast/Desktop/Projects/IoT/uploads',filename)

if __name__ == "__main__":
    app.run(port=7777)

