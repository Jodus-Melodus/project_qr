import qrcode
import PIL.Image

while True:
    path = input("Input file path > ")
    
    with open(path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        img = qrcode.make(line)
        img.save(line + '.png')
        image = PIL.Image.open(line + ".png")
        image = image.resize((57, 57))
        image.save(line + ".png")
        print("Successfull!")
