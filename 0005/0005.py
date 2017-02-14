# -*- coding:utf-8 -*-

import os
from PIL import Image

iPhone5_width = 1136
iPhone5_height = 640

def resize_iPhone_pic(path, new_path, width=iPhone5_width, height=iPhone5_height):
	im = Image.open(path)
	w,h = im.size;

	if w > width:
		h = width * h // w   # // 代表整数除法
		w = width
	if h > height:
		w = height * w // h
		h = height

	im_resized = im.resize((w,h), Image.ANTIALIAS)
	im_resized.save(new_path)

def walk_dir_and_resize(path):
	for root, dirs, files in os.walk(path):
		for f_name in files:
			if f_name.lower().endswith('jpg'):
				path_dst = os.path.join(root,f_name)
				f_new_name = 'iPhone5_' + f_name
				resize_iPhone_pic(path=path_dst, new_path=f_new_name)

if __name__ == '__main__':
	walk_dir_and_resize('./')