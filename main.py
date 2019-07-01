from PIL import Image, ImageDraw
def count_word(word):
	count = len(word)
	return count

def write_def():
	file = Image.new('RGB',(1, 400))
	file.save('message.png')
	word = input ('>')
	image_file = Image.open('message.png')

	word_dict = {'а':(0,0,14),'б':(255,0,0),'в':(0,15,14),'г':(14,0,15),'д':(13,13,13),'е':(12,246,123),'ё':(74,45,85),
				'ж':(77,88,99),'з':(11,22,33),'и':(44,45,46),'к':(78,77,46),'л':(47,77,98),'м':(0,11,11),'н':(11,0,11),'о':(13,11,0),'п':(1,1,1),'р':(2,2,2),
				'с':(33,33,45),'т':(45,12,123),'у':(78,151,55),'ф':(200,199,158),'х':(185,201,99),'ц':(44,45,116),'ч':(111,222,123),'ш':(33,14,186),'щ':(78,99,65),'ь':(0,0,65),
				'ъ':(78,95,117),'э':(74,71,116),'ю':(117,47,58),'я':(59,87,78),'й':(74,11,12),'q':(11,78,78),'w':(0,14,13),'e':(89,115,169),'r':(34,5,231),'t':(255,208,16),
				'y':(216,222,255),'u':(202,203,165),'i':(3,49,85),'o':(44,11,22),'p':(189,198,178),'a':(178,98,79),'s':(97,98,94),'d':(95,14,13),'f':(77,77,66),'g':(16,14,22),
				'h':(15,44,88),'j':(189,188,116),'k':(11,114,115),'l':(124,125,198),'z':(198,152,154),'x':(44,75,188),'c':(59,89,156),'v':(165,166,138),'b':(128,129,11),'b':(11,13,112),
				'n':(3,2,1),'m':(255,12,13),' ':(74,38,238),'ы':(74,74,175)}
	word_list = list(word)
	global count
	#count = len(word_list)
	count = count_word(word_list)
	null_arg = 0
	fuck_arg = 0
	first_iter = 0
	second_iter = 0

	file = Image.new('RGB',(1, count))
	file.save('message.png')
	image_file = Image.open('message.png')

	for null_arg in range(fuck_arg,count):
		image_file.putpixel((fuck_arg,null_arg),(word_dict[word_list[null_arg]]))
		
	print(word_list)
	'''
	for first_iter in range(0,20):
		null_arg = null_arg+1
		for second_iter in range(0,20):
			image_file.putpixel((first_iter,second_iter),(word_dict[word_list[null_arg]]))
'''
	image_file.save('message.png')
	return main()

def read_def():
	image_file = Image.open('message.png')

	color_dict = {(0,0,14):'а',(255,0,0):'б',(0,15,14):'в',(14,0,15):'г',(13,13,13):'д',(12,246,123):'е',(74,45,85):'ё',(77,88,99):'ж',(11,22,33):'з',(44,45,46):'и',(78,77,46):'к',(47,77,98):'л',
			(0,11,11):'м',(11,0,11):'н',(13,11,0):'о',(1,1,1):'п',(2,2,2):'р',(33,33,45):'с',(45,12,123):'т',(78,151,55):'у',(200,199,158):'ф',(185,201,99):'х',(44,45,116):'ц',(111,222,123):'ч',
			(33,14,186):'ш',(78,99,65):'щ',(0,0,65):'ь',(78,95,117):'ъ',(74,71,116):'э',(117,47,58):'ю',(59,87,78):'я',(74,11,12):'й',(11,78,78):'q',(0,14,13):'w',(89,115,169):'e',(255,208,16):'t',
			(216,222,255):'y',(202,203,165):'u',(3,49,85):'i',(44,11,22):'o',(189,198,178):'p',(178,98,79):'a',(97,98,94):'s',(95,14,13):'d',(77,77,66):'f',(16,14,22):'g',(15,44,88):'h',(189,188,116):'j',
			(11,114,115):'k',(124,125,198):'l',(198,152,154):'z',(44,75,188):'x',(59,89,156):'c',(165,166,138):'v',(128,129,11):'b',(3,2,1):'n',(255,12,13):'m',(74,38,238):' ',(74,74,175):'ы'}
	i = 0
	word_list =''

#	for first_iter in range(0,20):
#		for second_iter in range(0,20):
#			pixel_color = image_file.getpixel((first_iter,second_iter))
#			if pixel_color in color_dict:
#				word_list = word_list + str(color_dict[pixel_color])
	for i in range(0,count):
		pixel_color = image_file.getpixel((0,i))
		if pixel_color in color_dict:
			word_list = word_list + str(color_dict[pixel_color])				
	print(word_list)
	return main()
def main():
	print('1. Write message'+'\n'+'2. Read message')
	choose = input('>')
	if choose == '1':
		return write_def()
	if choose == '2':
		return read_def()
if __name__ == '__main__':
	main()