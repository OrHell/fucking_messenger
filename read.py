from PIL import Image
im = Image.open('message.png')

fuck_dict = {(0,0,0):'п',(255,0,0):'р',(0,16,255):'и',
(50,205,50):'в',(97,5,15):'е',(52,58,5):'т'}
k =0
i = 0
j = 0
print(im.getpixel((0,1)))
word_list = ''
for i in range (0,20):
	for j in range(0,20):
		string_null = im.getpixel((i,j))
		if string_null in fuck_dict:
				word_list =word_list + str(fuck_dict[string_null] )
print(word_list)




#a= im.getpixel((1,1))
#print(a)
'''
string_null = str(string_null)
		with open ('test.txt','a') as file:
			file.write(string_null)
'''