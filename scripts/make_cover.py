#!/usr/bin/env python3
"""Generate an original open-graph cover image. Requires Pillow."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
W,H=1200,630
img=Image.new('RGB',(W,H),(17,30,42))
d=ImageDraw.Draw(img)
for i in range(H):
    blend=i/H
    d.line((0,i,W,i),fill=(int(17+9*blend),int(30+15*blend),int(42+16*blend)))
for x in range(30,W,46): d.line((x,0,x,H),fill=(35,49,59),width=1)
for y in range(20,H,46): d.line((0,y,W,y),fill=(35,49,59),width=1)
# editorial rings
for j in range(6):
    box=(740-j*16,50+j*15,1320-j*16,650+j*15)
    d.ellipse(box,outline=(70+j*7,73+j*7,75+j*7),width=2)
d.rounded_rectangle((775,132,1082,492),radius=4,fill=(27,49,63),outline=(197,156,95),width=2)
d.rounded_rectangle((789,147,1068,477),radius=2,outline=(92,80,61),width=2)
font_cjk='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
font=ImageFont.truetype(font_cjk,77,index=2)
font_mid=ImageFont.truetype(font_cjk,26,index=2)
font_small=ImageFont.truetype(font_cjk,22,index=2)
font_latin=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',23)
font_big_latin=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',106)
d.rectangle((62,90,99,93),fill=(217,177,122))
d.text((113,74),'INTJ / CAREER / COMPENSATION',font=font_latin,fill=(220,191,149))
d.text((59,151),'INTJ 职场',font=font,fill=(251,248,240))
d.text((59,253),'拿高薪',font=font,fill=(232,194,138))
d.text((59,352),'保姆级攻略',font=font,fill=(251,248,240))
d.text((62,486),'10章实战   ·   7天计划   ·   6份模板',font=font_small,fill=(192,206,211))
d.text((62,553),'AI 酋长 Andy / OPEN SOURCE',font=font_small,fill=(210,180,135))
d.text((844,203),'¥↑',font=font_big_latin,fill=(236,199,145))
d.line((861,339,1009,339),fill=(215,171,112),width=2)
d.text((803,382),'价值·证据·谈判',font=font_mid,fill=(245,227,198))
img.save(ROOT/'assets/social-preview.png',optimize=True)
print('Generated',ROOT/'assets/social-preview.png')
