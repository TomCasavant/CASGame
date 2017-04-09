from PIL import Image
from PIL import ImageDraw
def concatenateImages(image1, image2):
	''' Combines two images into one, takes stings of image names 
		Usage: concatenateImages("1", "2")'''
	first = Image.open(image1 + ".png")
	second = Image.open(image2 + ".png")
	solution = Image.new("RGB", (300, 200), "white")

	mask = Image.new("L", solution.size, color=255)
	draw = ImageDraw.Draw(mask)
	draw.rectangle((0,0,300,200), fill=0)
	solution.putalpha(mask)


	solution.paste(first, (0,0), first)
	solution.save("solution.png")
