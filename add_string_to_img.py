from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import os,sys


im = Image.open('ascii_dora.png').convert('RGBA')

txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
fnt = ImageFont.truetype("/System/Library/Fonts/SFNSText.ttf", 15)
d = ImageDraw.Draw(txt)
d.text((txt.size[0]-20, txt.size[1]-150), "+4", font = fnt, fill = (255, 140, 255, 255))
out = Image.alpha_composite(im, txt)
out.show()





