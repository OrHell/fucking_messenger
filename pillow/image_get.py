from PIL import Image, ImageGrab, ImageDraw
import sys
img = Image.new("RGB", (20, 20),(0,255,255))
img.save("1.png","PNG")                             # Черный квадрат
'''
text = "Hello, PIL!!!"
color = (0, 0, 120)
img = Image.new('RGB', (100, 50), color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((10, 20), text)
img.save("pil-basic-example.png")  
'''


im = Image.open("1.png")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

# write to stdout
im.save(sys.stdout, "PNG")