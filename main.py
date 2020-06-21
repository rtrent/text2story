from flask import Flask, redirect, url_for, request, render_template, send_file
from note2story import convert


app = Flask(__name__)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/results", methods=['POST'])
def results():
	text = request.form['note-text']

	if text =='':
		text = 'You need to paste your note into the text box. \n\n Thanks,\nRicky'


	bg_color = request.form['bg-color']
	font_color = request.form['font-color']

	filenames = convert(input_text = text, bg_color = bg_color, font_color = font_color)

	return render_template('results.html', results = filenames)

if __name__ == "__main__":
	app.run()