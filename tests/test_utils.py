import unittest
import os

from utils import random_caption, random_image_url


class TestRandomCaption(unittest.TestCase):

    def test_reads_from_file(self):
        caption = random_caption()
        self.assertIsInstance(caption, str)


class TestRandomImageUrl(unittest.TestCase):

    def test_reads_from_dir(self):
        image_url = random_image_url()
        self.assertIsInstance(image_url, str)
        assert os.path.exists(image_url)


if __name__ == "__main__":
    unittest.main()
