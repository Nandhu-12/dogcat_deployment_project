import base64

#once we receive the encoded image in the backend then there we do decoding of the image
#we will call this function inside app.py as we do decode in the backend

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

# here we are converting the images to string to send to cloud (encoding the image) because we cannot pause raw image
# through UI as HTML does not accept raw images
#inside HTML file we will encode so we will call this function inside html
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())