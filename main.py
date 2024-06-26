import qrcode

# business card information in vCard format with  social media links

vcard = """BEGIN:VCARD
VERSION:3.0
FN:John Doe
ORG:Company Name
TITLE:Software Engineer
TEL;TYPE=WORK,VOICE:(123) 456-7890
ADR;TYPE=WORK:;;123 Main Street;City;State;12345;Country
EMAIL:john.doe@example.com
URL:https://www.example.com
X-UPI-ID:your.upi.id@example
X-INSTAGRAM:https://www.instagram.com/yourprofile
X-FACEBOOK:https://www.facebook.com/yourprofile
END:VCARD"""


qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
qr.add_data(vcard)
qr.make(fit=True)

img = qr.make_image(fill = 'black' , back_color = 'white')

img.sava('business_card_qr_with_socials.png')

print("QR code with social media links generated and saved as 'business_card_qr_with_socials.png'")