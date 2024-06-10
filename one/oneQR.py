import PIL.Image
import qrcode, PIL

while True:
    data = input("Data > ")
    save_as = input("Save as > ")

    img = qrcode.make(data)
    img.save(save_as + ".png")
    image = PIL.Image.open(save_as + ".png")
    image = image.resize((57, 57))
    image.save(save_as + ".png")
    print("Successfull!")
