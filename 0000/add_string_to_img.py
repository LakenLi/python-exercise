from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os,sys
import platform


###以下是第一种方式
"""
im = Image.open('ascii_dora.png').convert('RGBA')

txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
fnt = ImageFont.truetype("/System/Library/Fonts/SFNSText.ttf", 15)
d = ImageDraw.Draw(txt)
d.text((txt.size[0]-20, txt.size[1]-150), "+4", font = fnt, fill = (255, 140, 255, 255))
out = Image.alpha_composite(im, txt)
out.show()
"""


# system = platform.system()
# print(system)
#v第二种在图片上加字的实现方式

def add_num(img):
	draw = ImageDraw.Draw(img)
	fnt = ImageFont.truetype("/System/Library/Fonts/SFNSText.ttf", 15)
	fillcolor = '#ff0000'
	width, height = img.size
	draw.text((width-40, 0), '99', font = fnt, fill = fillcolor)
	img.save('result.jpg', 'jpeg')

	return 0

if __name__ == '__main__':
	image = Image.open('ascii_dora.jpg')
	add_num(image)


