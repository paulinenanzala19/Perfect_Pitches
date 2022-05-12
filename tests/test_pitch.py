import unittest
from app.models import Pitch
from app import db

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id = 1, title = 'Amazing', pitch_content = 'Kwani wewe ni WIFI juu how i feel connected wueeeeh!', category = 'Pickuplines Line', upvote = 5, downvote = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))