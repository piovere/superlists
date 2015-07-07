from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setup(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# The app says to enter an item!

		# I type in "Water the garden"

		# When I hit enter, the page updates and the page lists "1: Water the garden" as an item on the to do list

		# There's still a text box
		# I enter "Fly spray Jesse"

		# The page updates again and then both items show up

		# There is some text telling me that I have my own special URL to visit

		# My URL has my saved to do list!

if __name__ == '__main__':
	unittest.main(warnings='ignore')
