import keyboard  
from PIL import Image, ImageGrab

while True: 
    try:  
        if keyboard.is_pressed('q'):  
            print('You Pressed A Key!')
            img = ImageGrab.grab()

            img.save("test.png", "PNG")
            img.show()
            break  
        else:
            pass
    except:
        break  