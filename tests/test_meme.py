import unittest

from meme import Meme


class TestMeme(unittest.TestCase):

    def test_create_random_meme(self):
        name = "William"
        random_meme = Meme.create_random_meme(name=name)

        print(random_meme.name)
        print(random_meme.caption)
        print(random_meme.image_url)
        self.assertIsInstance(random_meme.name, str)
        self.assertIsInstance(random_meme.caption, str)
        self.assertIsInstance(random_meme.image_url, str)
        print(random_meme.generate_file())


if __name__ == "__main__":
    unittest.main()
