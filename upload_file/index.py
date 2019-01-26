from flask import *
import os
from werkzeug import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER']="images"

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug = True)
