# from crypt import methods
from flask import Flask, flash, request, redirect, url_for, render_template,jsonify
import numpy as np
import urllib.request
import os








app=Flask(__name__)

UPLOAD_FOLDER = 'static/img/'


app.secret_key = "cairocoders-ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

     
def saveFile(inputName,filename):
    file = request.files[inputName]
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
   
            


# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/", methods=["POST","GET"])
def main():
    if request.method == "POST" :

        saveFile('file1',"image1.jpg")
        saveFile('file2',"image2.jpg")
        
        
        
        path1 = '.' + url_for('static', filename='img/' + "image1.jpg")
        path2 = '.' + url_for('static', filename='img/' + "image2.jpg")

        print(path1)
        print(path2)

        
        return render_template('index.html')
                    
         
    else: 
       return render_template("index.html")
    
            




 


if __name__=="__main__":
    app.run(debug=True ,port=4610) 







