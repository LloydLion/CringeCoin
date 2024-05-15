import base64

with open("image.png", "rb") as file:
    out = open("image.base64", "wb")
    out.write(base64.b64encode(file.read()))
    out.close()