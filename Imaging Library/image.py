from PIL import Image

im = Image.open('Capture.jpg', 'r')

pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]

print(pix_val_flat)