#first have to do : pip install qrcode[pil]

import qrcode 

#METHOD ONE
# text = input("Enter the text to convert : ")
# filename = input("Enter filename : ")

# def generate_QRCode(text,filename):
#     image_qrcode = qrcode.make(text)
#     image_qrcode.save(filename)

# generate_QRCode(text,filename)

#METHOD TWO (import text and filename from txt file)
def generate_QRCode(filepath):

    with open(filepath,"r") as file:
        lines = file.readlines()

    text = lines[0].strip()
    filename = lines[1].strip()

    #makeing qr code 
    image_qrcode = qrcode.make(text)
    #saving qr code
    image_qrcode.save(filename)

generate_QRCode('input.txt')
