def blend_image(left_image_data, right_image_data, images, left=0, right=1):
    # Average images data and create new image

    image = int((left+right)/2)

    # Store image and create more if needed
    mid = int((left+right)/2)
    if images[mid]:
        return images

    images[mid] = image
    blend_image(images[left], images[mid], images, left, mid)
    blend_image(images[mid], images[right], images, mid, right)

    return images

def load_images(image_directory):
    def load_image(image_path):
        import re
        f = open(image_path, 'r')

        width = None 
        height = None 
        max_brightness = None
        image_data = None

        width_counter = 0
        height_counter = 0
        line_count = 0

        for line in f.readlines():
            if line_count == 1:
                # Width and Height line
                # Find all groups of numbers
                m = re.findall(r'\d+', line)
                width = int(m[0])
                height = int(m[1])
            if line_count == 2:
                # Max brightness line
                max_brightness = int(line)
            elif line_count > 2:
                if image_data == None:
                    # Create 2D list initialized with 0's
                    image_data = [[0 for w in range(width)] for h in range(height)]

                # Find all groups of numbers
                m = re.findall(r'\d+', line)
                # Set pixel rgb as tuple
                image_data[height_counter][width_counter] = (int(m[0]), int(m[1]), int(m[2]))
                width_counter += 1
                if width_counter == width:
                    width_counter = 0
                    height_counter += 1

            line_count += 1
        # print(image_path)
        # print("Width: {}\nHeight: {}\nBrightness: {}\n".format(width, height, max_brightness))
        # print("First Pixel: {}".format(image_data[0][0]))
        f.close()
        return image_data

    import os
    loaded_images = []
    # Get all files (2) in directory and load them
    for file in os.listdir(image_directory):
        loaded_images.append(load_image(os.path.join(image_directory, file)))

    return load_images
    
# Load the two images to morph
loaded_images = load_images('formatted-images')

# Number of images in between the two provided images
steps = 2
images = [loaded_images[0], loaded_images[1]]
# Create list space to hold the generated in between images
for x in range(steps):
    images.insert(x+1, None)

#print(blend_image(images[0], images[steps+1], [10, None, None, 10], right=steps+1))
# Morph the images
morphed_images = blend_image(images[0], images[steps+1], images, right=steps+1)

# TODO: Save images as ppm files
