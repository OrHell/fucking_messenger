from PIL import Image
im = Image.open('1.png')

im.putpixel((9,9),(0,0,0,0))

'''
a= im.getpixel((0,0))
print(a)
'''