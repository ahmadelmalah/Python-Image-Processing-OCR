from PIL import Image, ImageDraw, ImageFont
img = Image.open('car.jpg')
logo = Image.open('logo.jpg')

print(img.size)
print(img.format)

resized_img = img.resize((128, 128))
resized_img.save('resized.png')

rotated = img.transpose(Image.ROTATE_90)
rotated.save('rotated.jpg')

cropped = img.crop((130, 260, 190, 350))
cropped.save('cropped.jpg')

logo.thumbnail((100, 100))
with_logo = img.copy()
with_logo.paste(logo, (10, 10))
with_logo.save('with_logo.jpg')

with_copyright = img.copy()
watermark = Image.new('RGBA', img.size)
draw = ImageDraw.Draw(watermark)
text = "Copyright 2024"
font=ImageFont.load_default()
textwidth = draw.textlength(text, font)
text_location = (img.width /2 - textwidth / 2, img.height / 2 - 50 / 2)
draw.text(text_location, text, font=font)
with_copyright.paste(watermark, (0, 0), watermark)
with_copyright.save('with_copyright.jpg')