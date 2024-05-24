import qrcode
print("start...")

# create QR code
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

# enter your text or url 
data = "https://github.com/KhadijaAbdeLouassaa"

# add data to QR code object
qr.add_data(data)

# make the QR code 
qr.make(fit=True)

# creat image from QR code with your color options, such as RGB values or CSS color names
img = qr.make_image(fill_color="#9B9AEF", back_color="black")

# save the QR code image
img.save("qr_code.png")

print("done.")