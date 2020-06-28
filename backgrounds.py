import sys
from PIL import Image, ImageDraw 
import os
from color_selector import pick_color

def grid(bg_color = 'blue', shape='story', text_color = 'white'):
	"create a monochromatic grid background"

	core = pick_color(bg_color, 'core')

	if text_color == 'white':
		dark  = pick_color(bg_color, 'dark')
		light = pick_color(bg_color, 'light')
	else:
		dark  = pick_color(bg_color, 'light')
		light = pick_color(bg_color, 'dark')

	#Generate background - sizes are expressed as x dimension, y dimension
	bg_x, bg_y, padding_x, padding_y = (540,960,50,75)

	image = Image.new(mode = "RGB", size = (bg_x,bg_y), color = core)

	draw = ImageDraw.Draw(image)

	pattern_size = 3
	across = pattern_size * 9
	down = pattern_size * 16

	x_lines = range(1, across)
	y_lines = range(1, down)

	for x_item in x_lines:
		x_coord = bg_x / across * x_item
		draw.line((x_coord, 0, x_coord, bg_y), width = 1, fill = light)

	for y_item in y_lines:
		y_coord = bg_y / down * y_item
		draw.line((0, y_coord, bg_x, y_coord), width = 1, fill = light)

	draw.rectangle((padding_x , padding_y , bg_x-padding_x, bg_y-padding_y), fill=dark)

	return(image)

def dots(bg_color = 'blue', shape='story', text_color = 'white'):
	"create a monochromatic dots background"

	core = pick_color(bg_color, 'core')

	if text_color == 'white':
		dark  = pick_color(bg_color, 'dark')
		light = pick_color(bg_color, 'light')
	else:
		dark  = pick_color(bg_color, 'light')
		light = pick_color(bg_color, 'dark')

	#Generate background - sizes are expressed as x dimension, y dimension
	bg_x, bg_y, padding_x, padding_y = (540,960,50,75)

	image = Image.new(mode = "RGB", size = (bg_x,bg_y), color = core)

	draw = ImageDraw.Draw(image)


	pattern_size = 3
	across = pattern_size * 9
	down = pattern_size * 16

	x_lines = range(1, across)
	y_lines = range(1, down)

	circle_radius = 1

	for y_item in y_lines:
		y_coord = bg_y / down * y_item
		for x_item in x_lines:
			x_coord = bg_x / across * x_item

			rand_x = 0

			if y_item % 2 == 0:
				rand_x = bg_x / across / 2

				if x_item == max(x_lines):
					continue
			else:
				rand_x = 0

			draw.ellipse((x_coord - circle_radius + rand_x, y_coord - circle_radius, x_coord + circle_radius + rand_x, y_coord + circle_radius), fill = light)

	draw.rectangle((padding_x, padding_y, bg_x-padding_x, bg_y-padding_y), fill=dark)

	return(image)

def stripes(bg_color = 'blue', shape='story', text_color = 'white'):
	"create a monochromatic stripes background"

	core = pick_color(bg_color, 'core')

	if text_color == 'white':
		dark  = pick_color(bg_color, 'dark')
		light = pick_color(bg_color, 'light')
	else:
		dark  = pick_color(bg_color, 'light')
		light = pick_color(bg_color, 'dark')

	#Generate background - sizes are expressed as x dimension, y dimension
	bg_x, bg_y, padding_x, padding_y = (540,960,50,75)

	image = Image.new(mode = "RGB", size = (bg_x,bg_y), color = core)

	draw = ImageDraw.Draw(image)

	#if post bultiply down by 9 if story multiply down by 16
	pattern_size = 1
	down = pattern_size * 16

	x_lines = range(1, down * 2, 2)

	width = 42

	for x_item in x_lines:
		coord = bg_y / down * x_item

		draw.line((coord + width, -width, -width, coord + width), width = width, fill = light)
			
	draw.rectangle((padding_x, padding_y, bg_x-padding_x, bg_y-padding_y), fill=dark)

	return(image)

def solid(bg_color = 'blue', shape='story', text_color = 'white'):
	"create a solid background"

	if text_color == 'white':
		color  = pick_color(bg_color, 'dark')
	else:
		color  = pick_color(bg_color, 'light')

	bg_x, bg_y, padding_x, padding_y = (540,960,50,75)

	image = Image.new(mode = "RGB", size = (bg_x,bg_y), color = color)
	draw = ImageDraw.Draw(image)

	return(image)


def build_background(pattern, bg_color, shape, text_color):
	"helper function to return the right background"
	
	if pattern == 'solid':
		result = solid(bg_color = bg_color, shape=shape, text_color = text_color)
	elif pattern == 'grid':
		result = grid(bg_color = bg_color, shape=shape, text_color = text_color)
	elif pattern == 'dots':
		result = dots(bg_color = bg_color, shape=shape, text_color = text_color)
	elif pattern == 'stripes':
		result = stripes(bg_color = bg_color, shape= shape, text_color = text_color)
	else:
		exit()

	return result









