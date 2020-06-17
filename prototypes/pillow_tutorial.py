import sys
from PIL import Image, ImageDraw, ImageFont
import os
 
def main(filename='01.png', text="Hello", bg_color = 'red', size=200, text_color=(255,255,0)):
	"Draw a text on an Image, saves it, show it"

	if len(sys.argv) > 4:
		sys.exit()



	if len(sys.argv) > 1:
		filename = sys.argv[1]
		text = sys.argv[2]
		bg_color = sys.argv[3]
		text_color = (255,255,255)
	#could replace input text with a file

	text_name = "input.txt"

	with open(text_name) as f:
		text = f.read()


	fnt = ImageFont.truetype('Courier New.ttf', size)
	# create image
	image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), 
		color = bg_color)

	draw = ImageDraw.Draw(image)
	# draw text
	draw.text((10,10), text, font=fnt, fill=text_color)
	# save file
	image.save(filename)
	# show file
	os.system(filename)

	image.show()

	sys.exit()

if __name__ == '__main__':
	main()