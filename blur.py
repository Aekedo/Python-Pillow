from PIL import Image,ImageFilter
before = Image.open("bird_names.jpg")
after = before.filter(ImageFilter.BLUR)
after.save("blur-bird.jpg")