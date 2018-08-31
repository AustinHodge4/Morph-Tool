def blend_image(left_image_data, right_image_data, steps=1):
    # Load images

    # Average images

    # Create new Image
    pass

def load_images(image_directory):
    def load_image(image_path):
        import re
        f = open(image_path, 'r')
        line_count = 0
        width = None 
        height = None 
        max_brightness = None
        for line in f.readlines():
            if line_count == 1:
                m = re.findall(r'\d+', line)
                width = int(m[0])
                height = int(m[1])
            if line_count == 2:
                max_brightness = int(line)
            elif line_count > 4:
                break
            line_count += 1
        print("Width: {}\nHeight: {}\nBrightness: {}\n".format(width, height, max_brightness))
        f.close()

    import os
    images = []
    for file in os.listdir(image_directory):
        images.append(load_image(os.path.join(image_directory, file)))

    blend_image(images[0], images[1])

load_images('formatted-images')
