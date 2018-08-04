from PIL import Image
from PIL import PSDraw
from PIL import ImageDraw
from PIL import ImageFont

#from __future__ import print_function
import os,sys

##转换图片格式
"""
for infile in sys.argv[1:]:
	f, e = os.path.splitext(infile)
	outfile = f + ".jpg"
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print("cannot convert", infile)

#im = Image.open("ascii_dora.png")
#print(im.format, im.size, im.mode)
"""

##
"""
for infile in sys.argv[1:]:
	try:
		with Image.open(infile) as im:
			print(infile, im.format, "%dx%d" % im.size, im.mode)
	except IOError:
		pass
"""

"""
im = Image.open("ascii_dora.jpg")
title = "hhahah"
box = (1*72, 2*72, 7*72, 10*72)

ps = PSDraw.PSDraw()
ps.begin_document(title)

ps.image(box, im, 75)
ps.rectangle(box)

ps.setfont("HelveticaNarrow-bold", 36)
ps.text((3*72, 4*72), title)

ps.end_document()
"""

im = Image.open('ascii_dora.png').convert('RGBA')

txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
fnt = ImageFont.truetype("/System/Library/Fonts/SFNSText.ttf", 15)
d = ImageDraw.Draw(txt)
d.text((txt.size[0]-20, txt.size[1]-150), "+4", font = fnt, fill = (255, 140, 255, 255))
out = Image.alpha_composite(im, txt)
out.show()





