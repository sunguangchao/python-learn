import os
from PIL import Image

PHONE = {'iPhone5':(1136,640), 'iPhone6':(1134,750), 'iPhone6P':(2208,1242)} 
# dict

def resize_pic(path, new_path, phone_type):
	im = Image.open(path)
	h,w = im.size

	width,height = PHONE[phone_type]

	if w > width:
		h = width * h // w
		w = width
	if h > height:
		w = height * w // h
		h = height

	im_resize = im.resize((w,h), Image.ANTIALIAS)
	im_resize.save(new_path)

def walk_dir_and_resize(path, phone_type):
	for root, dirs, files in os.walk(path):
		for f_name in files:
			if f_name.lower().endswith('jpg'):
				path_dst = os.path.join(root, f_name)
				f_new_name = phone_type + '_' + f_name
				resize_pic(path=path_dst, new_path=f_new_name, phone_type=phone_type)


if __name__ == '__main__':
	walk_dir_and_resize('./', 'iPhone6P')



