# SmartBizQR

SmartBizQR generates a QR code containing business card information, social media links (Instagram and Facebook) in vCard format. The QR code is saved as an image file.

## Prerequisites

Ensure you have Python installed on your system. You also need to install the following Python libraries:
- `qrcode[pil]`

You can install the necessary libraries using pip:
```bash
pip install qrcode[pil]
```

## Usage
1. Clone this repository or download the script.
2. Open the script file and update the business card information, UPI ID, and social media links with your actual details.
3. Run the script.

## Script
```bash
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
```

## Customization
- Replace "John Doe" with your actual name.
- Replace "Company Name" with your actual company name.
- Replace "Software Engineer" with your actual title.
- Replace "(123) 456-7890" with your actual phone number.
- Replace "123 Main Street;City;State;12345;Country" with your actual address.
- Replace "john.doe@example.com" with your actual email.
- Replace "https://www.example.com" with your actual website URL.
- Replace "your.upi.id@example" with your actual UPI ID.
- Replace "https://www.instagram.com/yourprofile" with your actual Instagram profile link.
- Replace "https://www.facebook.com/yourprofile" with your actual Facebook profile link.
- - Replace "geo: x ,y " with your actual location .
## Output

The script generates a QR code image file named business_card_qr_with_socials.png in the current directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.