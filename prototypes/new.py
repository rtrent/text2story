import sys
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def main(filename='01.png', bg_color = 'red', font_size=70, text_color='white'):
	"Draw a text on an Image, saves it, show it"
	text = "Black\nLives\n\nMatter Black\n\nLives Matter"
	
	fnt = ImageFont.truetype('Courier New.ttf', font_size)
	image = Image.new(mode = "RGB", size = (1080,1080), color = bg_color)

	draw = ImageDraw.Draw(image)
	#width is the number of characters so you need to calculate
	#the pixels each character would take up given the font size
	lines = textwrap.wrap(text, width = 20, drop_whitespace  = False)

	y_padding = 10
	for line in lines:
		print(f"line: {line}")
		w,h = fnt.getsize(line)
		#.txt is like what is the position of your text
		draw.multiline_text(((1080 - w) / 2,y_padding), line, font = fnt, fill = text_color)
		y_padding += h

	# save file
	image.save(filename)

	image.show()

	sys.exit()

	#how do i make the font size responsive
	#how do i break the text into lines

if __name__ == '__main__':
	main()