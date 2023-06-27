import qrcode

input_URL = "https://play.google.com/store/apps/details?id=com.app.uengage.ufood&hl=en_IN&gl=US&pli=1"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)