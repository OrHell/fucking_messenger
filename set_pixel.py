from PIL import Image, ImageDraw
word = input(">")
im = Image.open('1.png')

first_dicts = {'п':(0,0,0,245),'р':(255,0,0),'и':(0,16,255),"в" : (50,205,50),'е':(97,5,15),'т':(52,58,5)}

word_list = list(word)
print(first_dicts[word_list[0]])

count  = len(word_list)
null_arg = 0

for null_arg in range(0,count):
	im.putpixel((0,null_arg),(first_dicts[word_list[null_arg]]))
	a= im.getpixel((1,1))
print(a)

im.save('test.png', "PNG")
