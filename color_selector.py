def pick_color(color_name, color_shade):

	bg_colors = {
		"red": { "core":(212, 30, 113), "dark": (171, 9, 82), "light": (252, 189, 218)},
		"green": { "core":(116, 193, 86), "dark":(63, 128, 37), "light":(185, 232, 167)},
		"blue": {"core":(26, 127, 228), "dark":(13, 64, 114), "light":(178, 212, 246)},
		"black": {"core":(153, 153, 153), "dark":(51, 51, 51), "light":(238, 238, 238)}
	}


	return bg_colors[color_name][color_shade]