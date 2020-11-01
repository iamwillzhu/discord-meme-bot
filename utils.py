import random
import os
CAPTION_FILE = "captions.txt"
IMAGES_DIR = "images"


# (Waterman's "Reservoir Algorithm") from Knuth's "The Art of Computer Programming" R(3.4.2)
def random_caption() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = dir_path + "/" + CAPTION_FILE
    f = open(file_path)
    line = next(f)
    for num, current_line in enumerate(f, 2):
        if random.randrange(num):
            continue
        line = current_line.strip()

    f.close()
    return line


def random_image_url() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_dir_path = dir_path + "/" + IMAGES_DIR
    images = os.listdir(image_dir_path)
    image_file = random.choice(images)

    return image_dir_path + "/" + image_file
