from collections import namedtuple
RGB = namedtuple('RGB', 'r g b')

#from graphics import Application
def blend_image(left_image_data, right_image_data, images, left=0, right=1):
    # Average images data and create new image
    image_data = [[0 for w in range(len(left_image_data[h]))] for h in range(len(left_image_data))]
    for h in range(len(image_data)):
        for w in range(len(image_data[h])):
            image_left_rgb = left_image_data[h][w]
            #print(image_left_rgb)
            image_right_rgb = right_image_data[h][w]
            r_avg = int((image_left_rgb.r + image_right_rgb.r)/2)
            g_avg = int((image_left_rgb.g + image_right_rgb.g)/2)
            b_avg = int((image_left_rgb.b + image_right_rgb.b)/2)
            image_data[h][w] = RGB(r=r_avg, g=g_avg, b=b_avg)
            
    # left_image_data[0][0] 
    #image_data = int((left+right)/2)

    # Store image and create more if needed
    mid = int((left+right)/2)
    if images[mid]:
        return images

    images[mid] = image_data
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
        meta_data = []
        for line in f.readlines():
            if line_count < 2:
                meta_data.append(line)
            if line_count == 2:
                # Width and Height line
                # Find all groups of numbers
                m = re.findall(r'\d+', line)
                width = int(m[0])
                height = int(m[1])
                meta_data.append(line)
            if line_count == 3:
                # Max brightness line
                max_brightness = int(line)
                meta_data.append(line)
            elif line_count > 3:
                if image_data == None:
                    # Create 2D list initialized with 0's
                    image_data = [[0 for w in range(width)] for h in range(height)]

                # Find all groups of numbers
                m = re.findall(r'\d+', line)
                # Set pixel rgb as tuple
                image_data[height_counter][width_counter] = RGB(r=int(m[0]), g=int(m[1]), b=int(m[2]))
                width_counter += 1
                if width_counter == width:
                    width_counter = 0
                    height_counter += 1

            line_count += 1
        # print(image_path)
        # print("Width: {}\nHeight: {}\nBrightness: {}\n".format(width, height, max_brightness))
        # print("First Pixel: {}".format(image_data[0][0]))
        f.close()
        return image_data, meta_data

    import os
    loaded_images = []
    meta_data = []
    # Get all files (2) in directory and load them
    for file in os.listdir(image_directory):
        if meta_data:
            loaded_images.append(load_image(os.path.join(image_directory, file))[0])
        else:
            image_data, meta_data = load_image(os.path.join(image_directory, file))
            loaded_images.append(image_data)

    return loaded_images, meta_data

#app = Application()

def begin(steps=2):
    from formatPPM import save_images
    # Load the two images to morph
    loaded_images, meta_data = load_images('formatted-images')

    # # Number of images in between the two provided images
    images = [image for image in loaded_images]
    # # Create list space to hold the generated in between images
    for x in range(steps):
        images.insert(x+1, None)

    #print(blend_image(images[0], images[steps+1], [10, None, None, 100], right=steps+1))
    # Morph the images
    morphed_images = blend_image(images[0], images[steps+1], images, right=steps+1)
    print("Done Morphing")
    # TODO: Save images as ppm files
    save_images(morphed_images, meta_data)
