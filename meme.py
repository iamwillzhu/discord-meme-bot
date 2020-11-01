import os
from PIL import Image, ImageFont, ImageDraw
from utils import random_caption, random_image_url

GENERATED_MEMES_DIR = "generated-memes"


class Meme:

    def __init__(self, name: str, caption: str, image_url: str):
        self.name = name
        self.caption = caption
        self.image_url = image_url

    # TODO: figure out how to format the image

    def generate_file(self) -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        generated_memes_dir_path = dir_path + "/" + GENERATED_MEMES_DIR
        if not os.path.exists(generated_memes_dir_path):
            os.mkdir(generated_memes_dir_path)

        with Image.open(self.image_url) as image:
            size = image.size
            font_size = int(size[1] / 5)
            font = ImageFont.truetype("impact.ttf", font_size)

            edit = ImageDraw.Draw(image)

            top_text_size = font.getsize(self.name)
            bottom_text_size = font.getsize(self.caption)

            top_text_position_x = (size[0] / 2) - (top_text_size[0] / 2)
            top_text_position_y = 0
            top_text_position = (top_text_position_x, top_text_position_y)

            bottom_text_position_x = (size[0] / 2) - (bottom_text_size[0] / 2)
            bottom_text_position_y = size[1] - bottom_text_size[1] - 10
            bottom_text_position = (
                bottom_text_position_x, bottom_text_position_y)

            edit.text(top_text_position, self.name, (255, 255, 255), font=font)
            edit.text(bottom_text_position, self.caption,
                      (255, 255, 255), font=font)

            generated_meme_file_path = generated_memes_dir_path + '/meme.jpg'

            image.save(generated_meme_file_path)

            return generated_meme_file_path

    @classmethod
    def create_random_meme(cls, name: str):
        caption = random_caption()
        image_url = random_image_url()
        return cls(name=name, caption=caption, image_url=image_url)
