from flask import Flask, render_template, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads,IMAGES, UploadSet
from werkzeug import secure_filename, FileStorage
import base64
import os
from flask.templating import render_template
import util


app = Flask(__name__)

app.config['SECRET_KEY']='test'
app.config['UPLOADED_IMAGES_DEST']='uploads/images'

images=UploadSet('images', IMAGES)
configure_uploads(app, images)
class MyForm(FlaskForm):
  image=FileField('image')

@app.route('/', methods=['GET', 'POST'])
def index():
  form=MyForm()
  if form.validate_on_submit():
    print(form.image.data)
    filename=images.save(form.image.data)
    curr_path=os.path.join('./uploads/images/',filename)
    with open(curr_path, "rb") as image2string:
      converted_string = base64.b64encode(image2string.read())

    with open('encode.bin', "wb") as file:
      file.write(converted_string)

  return render_template('index.html',form=form)

# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     return render_template('app.html')


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = 'encode_bin'

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response



if __name__ == "__main__":
  app.run(debug=True)