import sys
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def main(input_filename = 'input.txt', output_filename='01.png', bg_color = 'blue', font_name = 'Courier New.ttf', font_size=30, text_color='white'):
	"Draw a text on an Image, saves it, show it"



	#Generate background
	dimensions = (1080,1080)
	image = Image.new(mode = "RGB", size = dimensions, color = bg_color)
	draw = ImageDraw.Draw(image)

	#settings for the font and size
	#i feel like, knowing the font size, I need to make a calculation for
	#the max length of the lines when I wrap them.
	fnt = ImageFont.truetype('Courier New.ttf', font_size)
	padding = (10, 10)

	#center uses (dimension width - line width_ / 2
	#align left uses padding
	#align right uses dimension width - line width - padding

	with open(input_filename) as file:
		lines = file.readlines()
	
	y_line_height = padding[0]

	for line in lines:
		sublines = textwrap.wrap(line, width = 25, drop_whitespace = False)
		for line in sublines: #breaks long lines into smaller parts
			print(f"line: {line}") # print for qc
			w,h = fnt.getsize(line) #line height and width, width changes with the wrapping
			draw.multiline_text((padding[1],y_line_height), line.strip(), font = fnt, fill = text_color)
			y_line_height += h


	#width is the number of characters so you need to calculate
	#the pixels each character would take up given the font size

	# save file
	image.save(output_filename)

	image.show()

	sys.exit()

	#how do i make the font size responsive
	#how do i break the text into lines

if __name__ == '__main__':
	main()