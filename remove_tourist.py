from PIL import Image

# Author: Albert Jozsa-Kiraly
# This function takes the list of images, and the width and the height of them.
# It goes through the width and height, then iterates through each image.
# The RGB values at the same coordinates from each image are fetched and stored
# in a list. These RGB values are separated into 3 lists (red, green, and blue),
# the lists are sorted, and the median of each is calculated. The new RGB value,
# using the medians, is created, and the new pixel with this RGB value is put
# in the new image.
def remove_tourist(image_list, width, height):

	# Create the new Image object
	new_image = Image.new("RGB", (width, height), "white")

	x = 0
	y = 0

	# Iterate through the width and the height of all images
	for x in range(width):
		for y in range(height):

			# This will store the RGB values at the current coordinate of each image
			current_coordinate_rgbs = []

			# Iterate through the list of images. For each image,
			# get the RGB values from the current coordinate, and store them
			# in the current_coordinate_rgbs list.
			for current_image in image_list:
				color = current_image.getpixel((x, y))
				current_coordinate_rgbs.append(color)

			# Separate the RGB values of the current coordinate into 3 lists.
			# Then sort the lists. 
			reds = []
			greens = []
			blues = []

			for pixel in current_coordinate_rgbs:
				reds.append(pixel[0])
				greens.append(pixel[1])
				blues.append(pixel[2])

			reds.sort()
			greens.sort()
			blues.sort()

			# Calculate the median of each list
			median_red = reds[int(round(len(reds)+1)/2)]
			median_green = greens[int(round(len(greens)+1)/2)]
			median_blues = blues[int(round(len(blues)+1)/2)]

			# Create the new RGB value using the 3 median values
			median_color = (median_red, median_green, median_blues)

			# Put the pixel with the median RGB value on the new image
			new_image.putpixel((x,y), median_color)

		y+=1
	x+=1

	new_image.save("removed_tourist.png")

# Load the 9 images as Pillow Image objects and put them in a list.
# Assume the images are in the same folder as this py file.
image1 = Image.open("1.png")
image2 = Image.open("2.png")
image3 = Image.open("3.png")
image4 = Image.open("4.png")
image5 = Image.open("5.png")
image6 = Image.open("6.png")
image7 = Image.open("7.png")
image8 = Image.open("8.png")
image9 = Image.open("9.png")

image_list = [image1, image2, image3, image4, image5, image6, image7,
image8, image9]

# Call the function which produces a new image without the tourist on it.
# Use the size of one of the images. Assume all images have the same size.
remove_tourist(image_list, image1.width, image1.height)
