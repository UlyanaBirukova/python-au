import imghdr
import os
from flask import Flask, render_template, url_for, request, redirect, abort, send_from_directory, session
from werkzeug.utils import secure_filename


site = Flask(__name__)
site.config['UPLOAD_PATH'] = os.getcwd()+'/uploads'


@site.route('/')
@site.route('/home')
def index():
    return render_template('index.html')
    
    
@site.route('/admin')
def admin():
    return render_template('admin.html')
    
    


@site.route('/Readen')
def q():
    return render_template('Readen.html')
    
    
@site.route('/Readru')
def w():
    return render_template('Readru.html')
    
    
@site.route('/3class')
def r():
    return render_template('3.html')
    
    
@site.route('/4class')
def t():
    return render_template('4.html')
    
    
@site.route('/5class')
def y():
    return render_template('5.html')
    
    
@site.route('/8class')
def u():
    return render_template('8.html')
    
    
@site.route('/9class')
def i():
    return render_template('9.html')
    
    
@site.route('/11class')
def o():
    return render_template('11.html')
    
    
@site.route('/myclass')
def p():
    return render_template('myclass.html')
    
    
@site.route('/library')
def a():
    return render_template('library.html')
    
    
@site.route('/EGE')
def s():
    return render_template('EGE.html')
    
    
@site.route('/OGE')
def d():
    return render_template('OGE.html')
    
    
@site.route('/2class', methods=['POST', 'GET'])
def clss():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = uploaded_file.filename
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            uploaded_file.save(os.path.join(site.config['UPLOAD_PATH'], filename))
        return redirect(url_for('clss'))
    elif request.method == 'GET':
        if 'admin' in session:
            admin=1
        else:
            admin=0
        print('asdffgf')
        files = os.listdir(site.config['UPLOAD_PATH'])
        print('dfgdfgsgfd', files)
        return render_template('2.html', files=files, admin=admin)
        

@site.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(site.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    #site.run(debug=True)
    site.run(debug=False)
