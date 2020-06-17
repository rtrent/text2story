import sys
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def convert(input_text = 'hello world', output_name='output', output_filetype='.png', bg_color = 'blue', font_name = 'Arial.ttf', font_size=40, font_color='white', alignment='left', shape='post'):
	"Draw a text on an Image, saves it, show it"

	#Details of colors for background and font
	color_dict = {
	"black": (0,0,0),
	"red": (212,30,113),
	"green": (116,193,86),
	"blue": (61,149,240),
	"white": (255,255,255)
	}

	bg_color = color_dict[bg_color]
	font_color = color_dict[font_color]

	#details of dimensions and formatting depending on the posting method, feed or story
	#bg_x, bg_y, padding_x, padding_y
	shape_dict = {
		"post": (1080,1080,100,100),
		"story":(1080,1920,100,150)
	}

	#Generate background - sizes are expressed as x dimension, y dimension
	bg_x, bg_y, padding_x, padding_y = shape_dict[shape]

	image = Image.new(mode = "RGB", size = (bg_x,bg_y), color = bg_color)
	draw = ImageDraw.Draw(image)

	#Font details
	fnt = ImageFont.truetype(font_name, font_size)

	#Read lines of the text file
	# with open(input_filename) as file: 
	# 	lines = file.readlines()

	#used to take string from the input rather than a file
	lines = input_text.splitlines(keepends = True)
	
	#various size variables
	character_limit_list = []
	canvas_width = bg_x - 2 * padding_x
	canvas_height = bg_y - padding_y

	#compares the line width to the width of the type area and calculates the right character limit to wrap 
	#width is the number of characters so you need to calculate the pixels each character would take up given the font size

	for line in lines:
		char_limit = len(line)
		font_width = fnt.getsize(line.strip())[0]

		#if the length exceeds the width, then adjust
		if font_width > canvas_width:
			char_limit = int(char_limit * (canvas_width / font_width)) - 1

		character_limit_list.append(char_limit)

	# of all the character lengths pick the smallest one that is not 0
	#max_characters = min(i for i in character_limit_list if i > 1)

	#get dimensions of the font based on the first line
	(font_width, font_height), (offset_x, offset_y) = fnt.font.getsize(lines[0])
	#Set initial posiiton for the first line
	y_line_height = padding_y - offset_y

	#variable to help make file names when creating output images
	file_num = 1

	#Set flags for blank line calculations
	blank_line = False
	blank_line_previous = False

	line_num = -1

	#write each line of text, one by one on the image
	#each line is a paragraph
	#each subline is a segment of that which can fit on a width of the typing area
	for line in lines:

		#use the character max list for each line, so that each is treated differently
		line_num += 1
		max_characters = character_limit_list[line_num]

		#use the wrap function to split lines that are too long
		#make each into a subline
		sublines = textwrap.wrap(line, width = max_characters, drop_whitespace = False)
		for subline in sublines: #breaks long lines into smaller parts

			#Flag to capture if the current line is a blank
			blank_line = (len(subline.strip()) == 0)

			#if the line is too low on the image then save the imgage and make a new one
			if y_line_height + font_height > canvas_height:
				#show and save the completed image
				image.show()
				image.save(f"{output_name}_{file_num}{output_filetype}")
				file_num += 1

				#make a new blank image
				image = Image.new(mode = "RGB", size = (bg_x, bg_y), color = bg_color)
				draw = ImageDraw.Draw(image)
				y_line_height = padding_y - offset_y

				#if the first line of the new image is a blank line, then skip it
				if blank_line == True:
					blank_line_previous = blank_line
					continue
			
			if blank_line == True and blank_line_previous == True:
				blank_line_previous = blank_line
				continue

			#If it is blank, then skip this whole process and move the y position down
			elif blank_line == True:
				blank_line_previous = blank_line
				y_line_height += font_height + offset_y
				continue

			#If the line is not blank, then calculate font alignment and draw text
			else:
				#calculate x-position for text according to the alignment	
				w, h = fnt.getsize(subline.strip())

				alignment_dict = {
					"left": padding_x,
					"center": (bg_x - w) / 2 ,
					"right": bg_x - w - padding_x
				}

				alignment_x = alignment_dict[alignment]

				#write the text line on the image
				draw.text((alignment_x,y_line_height), subline.strip(), font = fnt, fill = font_color)

				#update the variable that tracks the y placement of the line
				y_line_height += font_height + offset_y

				blank_line_previous = blank_line

	#save current image as the file
	image.show()
	image.save(f"{output_name}_{file_num}{output_filetype}")

if __name__ == '__main__':
	main()