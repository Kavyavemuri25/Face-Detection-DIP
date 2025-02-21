from flask import Flask, request, render_template
import face_eye_detect
import detect_face_image
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/face_eye')
def face_eye():
    face_eye_detect.construct();
    return render_template('form.html')

@app.route('/detect_face', methods=['GET', 'POST'])
def detect_face():
    if request.method == 'POST':
        detect_face_image.face_detect(request.files['image']);
    return render_template('form.html')

@app.route('/team_members')
def team_members():
    return render_template('team_members.html')

if __name__ == '__main__':
    app.run()
