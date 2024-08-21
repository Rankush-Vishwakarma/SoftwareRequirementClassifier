from flask import *
import os
from deployment import *
from werkzeug.utils import secure_filename
app = Flask(__name__)
model , tokenizer = load_Model_Tokenizer()

# Create a directory in a known location to save files to.
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/')  
def home():  
    return render_template("home.html")  
 
@app.route('/', methods = ['POST'])  
def success():
    global file
    predicted_class = ''
    if request.method == 'POST':
        if request.args.get("f") == "f1":
            text = request.form['styled-textarea']
            print(text)
            predicted_class = predict(text,model , tokenizer)
            print(predicted_class)
        else:
            f = request.files['file']
            #f.save(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            new_path = os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
            #print(new_path)
            #print(os.path.abspath(new_path))
            new_path = os.path.abspath(new_path)
            file = multiplePrediction(new_path, model, tokenizer)
            print(file)
            predicted_class =  'file uploaded successfully and class has been predicted'
    return render_template("home.html", name = predicted_class)

@app.route('/download')
def download():
    #print('download', file)
    try:
        if file:
            return send_file(file, as_attachment = True)
    except:
        return 'No file is uploaded'
    
  
if __name__ == '__main__':  
    app.run(debug=True)  
