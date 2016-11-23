# -*- coding:UTF-8 -*-
from PIL import Image,ImageDraw,ImageFont

def add_num(picPath,num):
	image = Image.open(picPath)
	x,y = image.size
	myfont = ImageFont.truetype('Futura.tff',x/3)
	#加载一个truetype字体文件，并且创建一个对象
	ImageDraw.Draw(img).text((2 * x / 3,0),str(num),front = myfont,fill = 'red')
	image.save('pic_with_num.jpg')
if __name__ == '__main__':
	add_num('abc.jpg',9)