from PIL import Image

x, y = 160, 60

bg = Image.open('G:/pythondealPic/originalPic.jpg').convert("RGBA")   # 背景图
mask = Image.open('G:/pythondealPic/test111.psd').convert("RGBA")   # 蒙板

mask_size = mask.size
crop = bg.crop((x, y, x + mask_size[0], y + mask_size[1]))

m2 = Image.new('RGBA', mask.size)
m2.paste(crop, mask = mask)
crop.save('G:/pythondealPic/test.png')
