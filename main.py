from PIL import Image,ImageFilter


with Image.open("parrot.jpg") as original:
    pic_gray = original.convert("L")
    pic_blur = original.filter(ImageFilter.BLUR)
    pic_up = pic_gray.transpose(Image.ROTATE_90)
    pic_gray.save("bw_pic.jpg")
    pic_up.save("bw_pic2.jpg")
    pic_blur.save("blur_pic.jpg")
    pic_up.show()
