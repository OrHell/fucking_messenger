from PIL import Image, ImageGrab
img = ImageGrab.grab()
img.save("screen.png","PNG")


img2 = ImageGrab.grab( (100, 100, 300, 300) )
img2.save("screen2.png","PNG")
