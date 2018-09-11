import os
def read_file(file_path):
    f = open(file_path, 'r')
    line_count = 0
    color_count = 0
    lines = []
    color = ''
    for line in f.readlines():
        if line_count <= 3:
            # First three lines should be the same
            lines.append(line)
        else:
            # Combine the rgb lines into one line
            if color_count == 2:
                color += line
            else:
                color += line.replace('\n', ' ')

            color_count += 1
            # Add the combined rgb into as a line
            if color_count == 3:
                lines.append(color)
                color_count = 0
                color = ''
        line_count += 1
    f.close()
    return lines

def write_file(file_path, lines):
    f = open(file_path, 'w+')
    for line in lines:
        f.write(line)
    f.close()

def format_images_test(image_directory='test-images', formatted_directory='formatted-images'):
    ''' Test function to format images in a directory and place them into another directory'''
    # For each file convert to custom ppm style
    for file in os.listdir(image_directory):
        formated_image = read_file(os.path.join(image_directory, file))
        write_file(os.path.join(formatted_directory, file), formated_image)
def format_images(first_image_path, second_image_path, formatted_directory='formatted-images'):
    if not os.path.exists(formatted_directory):
        os.makedirs(formatted_directory)
        
    formated_image = read_file(first_image_path)
    write_file(os.path.join(formatted_directory, os.path.basename(first_image_path)), formated_image)

    formated_image = read_file(second_image_path)
    write_file(os.path.join(formatted_directory, os.path.basename(second_image_path)), formated_image)

def save_images(images, meta_data, directory='morphed-images'):
    if not os.path.exists(directory):
        os.makedirs(directory)

    def convert_image_data(image):
        lines = []
        line = ''
        for h in range(len(image)):
            for w in range(len(image[h])):
                rgb = image[h][w]
                line = str(rgb.r) + ' ' + str(rgb.g) + ' ' + str(rgb.b) + '\n'
                lines.append(line)
        return lines

    data = []
    for i, image in zip(range(len(images)),images):
        data.extend(meta_data)
        data.extend(convert_image_data(image))
        write_file(os.path.join(directory, 'morphed-image-'+str(i)+'.ppm'), data)
        data.clear()


# Convert Gimp styled ppm file to have rgb pairs on same line
#format_images_test('test-images', 'formatted-images')