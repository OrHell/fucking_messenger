from PIL import Image, ImageDraw

def write_def():
	file = Image.new('RGBA',(20, 20))
	file.save('message.png')
	word = input ('>')
	image_file = Image.open('message.png')

	word_dict = {'a':(0,0,14),'б':(255,0,0),'б':(),'в':(),'г':(),'д':(),'е':(),'ё':(),
				'ж':(),'з':(),'и':(),'к':(),'л':(),'м':(),'н':(),'о':(),'п':(),'р':(),
				'с':(),'т':(),'у':(),'ф':(),'х':(),'ц':(),'ч':(),'ш':(),'щ':(),'ь':(),
				'ъ':(),'э':(),'ю':(),'я':(),'й':(),'q':(),'w':(),'e':(),'r':(),'t':(),
				'y':(),'u':(),'i':(),'o':(),'p':(),'a':(),'s':(),'d':(),'f':(),'g':(),
				'h':(),'j':(),'k':(),'l':(),'z':(),'x':(),'c':(),'v':(),'b':(),'b':(),
				'n':(),'m':(),' ':()}
	word_list = list(word)

	count = len(word_list)
	null_arg = 0

	for null_arg in range(0,count):
		image_file.putpixel((0,null_arg),(word_dict[word_list[null_arg]]))
	image_file.save('message.png')

def read_def():
	image_file = Image.open('message.png')

	color_dict = {():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',
			():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',
			():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',
			():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',
			():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',
			():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',():'',}
	first_iter = 0
	second_iter = 0
	word_list =''

	for first_iter in range(0,20):
		for second_iter in range(0,20):
			pixel_color = image_file.getpixel((first_iter,second_iter))
			if pixel_color in color_dict:
				word_list = word_list + str(color_dict[pixel_color])
	print(word_list)

