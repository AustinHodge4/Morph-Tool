def read_file(file_path):
    f = open(file_path, 'r')
    line_count = 0
    color_count = 0
    lines = []
    color = ''
    for line in f.readlines():
        if line_count < 3:
            lines.append(line)
        else:
            if color_count < 3:
                if color_count == 2:
                    color += line
                else:
                    color += line.replace('\n', ' ')

                color_count += 1
            else:
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

def format_images(image_directory, formatted_directory):
    import os
    for file in os.listdir(image_directory):
        formated_image = read_file(os.path.join(image_directory, file))
        write_file(os.path.join(formatted_directory, file), formated_image)


format_images('test-images', 'formatted-images')