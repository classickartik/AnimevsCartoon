# from flask import Flask, request, jsonify
# from flask.templating import render_template
# # import util
# from flask_dropzone import Dropzone
# import os

# app = Flask(__name__)
# basedir=os.getcwd()
# app.config.update(
#     UPLOADED_PATH=os.path.join(basedir, 'uploads'),
#     DROPZONE_MAXFILE_SIZE=10,
#     DROPZONE_TIMEOUT=300*1000)
# dropzone = Dropzone(app)


# @app.route('/upload', methods=['POST', 'GET'])
# def upload():
#     if request.method == 'POST':
#         f = request.files.get('file')
#         f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
#     return render_template('index.html')


# # @app.route('/', methods=['GET', 'POST'])
# # def hello_world():
# #     return render_template('app.html')


# # @app.route('/classify_image', methods=['GET', 'POST'])
# # def classify_image():
# #     image_data = request.form['image_data']

# #     response = jsonify(util.classify_image(image_data))

# #     response.headers.add('Access-Control-Allow-Origin', '*')

# #     return response


# if __name__ == "__main__":
#     app.run(debug=True,port=5000)


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Ready'
