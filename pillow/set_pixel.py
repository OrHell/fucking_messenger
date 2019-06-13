from PIL import Image, ImageDraw
im = Image.open('1.png')

im.putpixel((9,9),(0,0,0,0))


a= im.getpixel((9,9))
print(a)
# write to stdout
im.save('test.png', "PNG")