from PIL import Image
'''
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

string_null = str(string_null)
		with open ('test.txt','a') as file:
			file.write(string_null)
'''
image_file = Image.open('message.png')

color_dict = {(0,0,14):'а',(255,0,0):'б',(0,15,14):'в',(14,0,15):'г',(13,13,13):'д',(12,246,123):'е',(74,45,85):'ё',(77,88,99):'ж',(11,22,33):'з',(44,45,46):'и',(78,77,46):'к',(47,77,98):'л',
			(0,11,11):'м',(11,0,11):'н',(13,11,0):'о',(1,1,1):'п',(2,2,2):'р',(33,33,45):'с',(45,12,123):'т',(78,151,55):'у',(200,199,158):'ф',(185,201,99):'х',(44,45,116):'ц',(111,222,123):'ч',
			(33,14,186):'ш',(78,99,65):'щ',(0,0,65):'ь',(78,95,117):'ъ',(74,71,116):'э',(117,47,58):'ю',(59,87,78):'я',(74,11,12):'й',(11,78,78):'q',(0,14,13):'w',(89,115,169):'e',(255,208,16):'t',
			(216,222,255):'y',(202,203,165):'u',(3,49,85):'i',(44,11,22):'o',(189,198,178):'p',(178,98,79):'a',(97,98,94):'s',(95,14,13):'d',(77,77,66):'f',(16,14,22):'g',(15,44,88):'h',(189,188,116):'j',
			(11,114,115):'k',(124,125,198):'l',(198,152,154):'z',(44,75,188):'x',(59,89,156):'c',(165,166,138):'v',(128,129,11):'b',(3,2,1):'n',(255,12,13):'m',(74,38,238):' '}
first_iter = 0
second_iter = 0
word_list =''
for first_iter in range(0,20):
	for second_iter in range(0,20):
		pixel_color = image_file.getpixel((first_iter,second_iter))
		if pixel_color in color_dict:
			word_list = word_list + str(color_dict[pixel_color])
			print(color_dict[pixel_color])
print(word_list)
print(image_file.getpixel((0,0)))