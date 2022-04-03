import os
from flask import Flask, render_template, request, redirect, url_for
from  werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
import keras
import numpy as np
import argparse
import imutils
import cv2
import time
import uuid
import base64
import requests

###########################################

img_width, img_height = 150,150
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
#model.load_weights(model_weights_path)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'JPG', 'png', 'PNG'])

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

#############################################


def predict(file):
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = model.predict(x)
    result = array[0]
    answer = np.argmax(result)

    
    if answer == 0:
      print("Label: Antipolo Cathedral")
      print("Name: https://wonderfilledjournal.com/2016-tanay-rizal-calinawan-cave/")
    elif answer == 1:
      print("Label: Bulawan Floating Restaurant")
      print("Name: https://wonderfilledjournal.com/2016-tanay-rizal-daranak-falls-batlag-falls/")
    elif answer == 2:
      print("Label: Celossian Flower Farm")
      print("Name: https://wonderfilledjournal.com/2016-tanay-rizal-daranak-falls-batlag-falls/")
    elif answer == 3:
      print("Label: Cloud 9")
      print("Name: Ito ay ang Hapunang Banoi sa Rizal")
    elif answer == 4:
      print("Label: Coffee Rush")
      print("Name: Ito ay ang Kinabuan Falls sa Rizal")
    elif answer == 5:
      print("Label: Daraitan")
      print("Name: Ito ay ang Mt. Lagyo sa Rizal")
    elif answer == 6:
      print("Label: Daranak")
      print("Name: Ito ay ang Mt. Oro sa Rizal")
    elif answer == 7:
      print("Label: Dinasaur Park")
      print("Name: Ito ay ang Mystical Cave sa Riza")
    elif answer == 8:
      print("Label: Diocesan Shrine of Our Lady of Arazanzu")
      print("Name: Ito ay ang Palo Alto sa Rizal")
    elif answer == 9:
      print("Label: Jardin De Miramar")
      print("Name: https://www.celineism.com/2016/05/tongtong-falls-tanay-rizal-photos.html")
    elif answer == 10:
      print("Label: Kasarinlan Park")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 11:
      print("Label: Lakeside Park")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 13:
      print("Label: Marian Hill")
      print("Name: https://www.celineism.com/2016/05/tongtong-falls-tanay-rizal-photos.html")
    elif answer == 14:
      print("Label: Masungi Georeserve")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 15:
      print("Label: Mount Calvary")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 16:
      print("Label: Our Lady of Light")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 18:
      print("Label: Our Lady of the Holy Rosary")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 17:
      print("Label: Our Lady of the Most Holy Rosary")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 18:
      print("Label: Light House (Parola)")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 19:
      print("Label: Petroglyphs")
      print("Name: https://www.celineism.com/2016/05/tongtong-falls-tanay-rizal-photos.html")
    elif answer == 20:
      print("Label: Pinto Art Museum")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 21:
      print("Label: Puente Del Diablo")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 22:
      print("Label: Rambulls Bakahan")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 23:
      print("Label: Regina Rica")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 24:
      print("Label: Rock Garden")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 25:
      print("Label: Saint Joseph Parish Church")
      print("Name: https://www.celineism.com/2016/05/tongtong-falls-tanay-rizal-photos.html")
    elif answer == 26:
      print("Label: Saint Clement Parish Church")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 27:
      print("Label: Saint Jerome Parish Church")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 28:
      print("Label: Saint Mary Magdalene Parish Church")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 29:
      print("Label: Saint Rose of Lima Parish Church")
      print("Name: https://www.celineism.com/2016/05/tongtong-falls-tanay-rizal-photos.html")
    elif answer == 30:
      print("Label: San Idelfonso Parish Church")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 31:
      print("Label: Saint John Parish Church")
      print("Name: https://www.celineism.com/2016/05/tongtong-falls-tanay-rizal-photos.html")
    elif answer == 32:
      print("Label: Sta Ursula Parish Church")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 33:
      print("Label: Tungtong Falls")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 34:
      print("Label: Wawa Dam")
      print("Name: https://www.wander.am/travel/manila-74/places/wawa-dam-80919.en.html")
    elif answer == 35:
      print("Label: Pililia Windmill")
      print("Name: https://www.celineism.com/2016/05/tongtong-falls-tanay-rizal-photos.html")

      

    return answer

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def template_test():
    return render_template('template.html', label='',name='', imagesource='../uploads/Banner.jpg')


@app.route('/', methods=['GET', 'POST'])

def upload_file():
 
    if request.method == 'POST':
        import time
        start_time = time.time()
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = predict(file_path)
            
            if result == 0:
              label = 'Antipolo Cathedral'
              name = ''
            elif result == 1:
              label = 'Bulawan Floating Restaurant'
              name = ''
            elif result == 2:
              label = 'Celossian Flower Farm'
              name = ''
            elif result == 3:
              label = 'Cloud 9'
              name = ''
            elif result == 4:
              label = 'Coffee Rush'
              name = ''
            elif result == 5:
              label = 'Daraitan'
              name = ''
            elif result == 6:
              label = 'Daranak'
              name = ''
            elif result == 7:
              label = 'Dinasaur Park'
              name = ''
            elif result == 8:
              label = 'Diocesan Shrine of Our Lady of Arazanzu'
              name = ''
            elif result == 9:
              label = 'Jardin De Miramar'
              name = ''
            elif result == 10:
              label = 'Kasarinlan Park'
              name = ''
            elif result == 11:
              label = 'Lakeside Park'
              name = ''
            elif result == 12:
              label = 'Marian Hill'
              name = ''
            elif result == 13:
              label = 'Masungi Georeserve'
              name = ''
            elif result == 14:
              label = 'Mount Calvary'
              name = ''
            elif result == 15:
              label = 'Our Lady of Light'
              name = ''
            elif result == 16:
              label = 'Our Lady of the Holy Rosary'
              name = ''
            elif result == 17:
              label = 'Our Lady of the Most Holy Rosary'
              name = ''
            elif result == 18:
              label = 'Light House (Parola)'
              name = ''
            elif result == 19:
              label = 'Petroglyphs'
              name = ''
            elif result == 20:
              label = 'Pinto Art Museum'
              name = ''
            elif result == 21:
              label = 'Puente Del Diablo'
              name = ''
            elif result == 22:
              label = 'Rambulls Bakahan'
              name = ''
            elif result == 23:
              label = 'Regina Rica'
              name = ''
            elif result == 24:
              label = 'Rock Garden'
              name = ''
            elif result == 25:
              label = 'Saint Joseph Parish Church'
              name = ''
            elif result == 26:
              label = 'Saint Clement Parish Church'
              name = ''
            elif result == 27:
              label = 'Saint Jerome Parish Church'
              name = ''
            elif result == 28:
              label = 'Saint Mary Magdalene Parish Church'
              name = ''
            elif result == 29:
              label = 'Saint Rose of Lima Parish Church'
              name = ''
            elif result == 30:
              label = 'San Idelfonso Parish Church'
              name = ''
            elif result == 31:
              label = 'Saint John Parish Church'
              name = ''
            elif result == 32:
              label = 'Sta Ursula Parish Church'
              name = ''
            elif result == 33:
              label = 'Tungtong Falls'
              name = ''
            elif result == 34:
              label = 'Wawa Dam'
              name = ''
            elif result == 35:
              label = 'Pililia Windmill'
              name = ''

            print(result)
            print(file_path)
            filename = my_random_string(6) + filename

            os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("--- %s seconds ---" % str (time.time() - start_time))
            return render_template('template.html', label=label,name=name, imagesource='../uploads/' + filename)


from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

from werkzeug import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})


if __name__ == "__main__":
    app.debug = False
    app.run(host='0.0.0.0', port=3000)

