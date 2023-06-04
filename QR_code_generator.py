import qrcode
import image

qr=qrcode.QRCode(
    version = 15,
    box_size = 10, #size of the box where qr will be displayed
    border = 5
)

data = "https://www.github.com/AkshatNaruka/"
#path to my github but you can insert your link for the qr this field 


qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("qr.png")
