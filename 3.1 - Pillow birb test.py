from PIL import Image, ImageFilter, ImageEnhance, ImageOps

with Image.open("birb.jpg") as picture:
    picture = ImageOps.exif_transpose(picture)
    #picture.show()

    black_white = picture.convert("L")
    black_white.save("blackandwhite.jpg")

    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("mirrored.jpg")

    blur = picture.filter(ImageFilter.BLUR)
    blur.save("blur.jpg")

    contrast = ImageEnhance.Contrast(picture)
    contrast = contrast.enhance(1.5)
    contrast.save("contrast.jpg")

    color = ImageEnhance.Color(picture).enhance(1.5)
    color.save("color.jpg")