import unittest
import os

from meme import Meme


class TestMeme(unittest.TestCase):

    def test_create_random_meme(self):
        name = "Carolyn"
        random_meme = Meme.create_random_meme(name=name)
        generated_meme = random_meme.generate_file()

        self.assertIsInstance(random_meme.name, str)
        self.assertIsInstance(random_meme.caption, str)
        self.assertIsInstance(random_meme.image_url, str)
        self.assertIsInstance(generated_meme, str)
        assert os.path.exists(random_meme.image_url)
        assert os.path.exists(generated_meme)
        os.remove(generated_meme)


if __name__ == "__main__":
    unittest.main()
