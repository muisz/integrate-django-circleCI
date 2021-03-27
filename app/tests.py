from django.test import TestCase
from django.conf import settings

# Create your tests here.
class AppTestCase(TestCase):
	def testEnv(self):
		self.assertEqual(settings.NAME, 'Abdul')