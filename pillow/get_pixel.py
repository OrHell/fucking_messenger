from PIL import Image
im = Image.open('1.png')
px = im.load()
print (px[0,0])
px[9,9] = (255,0,0)
print (px[9,9])

'''
a= im.getpixel((0,0))
print(a)
'''