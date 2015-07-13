from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# The app says to enter an item!
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# I type in "Water the garden"
		inputbox.send_keys('Water the garden')

		# When I hit enter, the page updates and the page lists "1: Water the garden" as an item on the to do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Water the garden' for row in rows)
		)

		# There's still a text box
		# I enter "Fly spray Jesse"
		self.fail('Finish the test!')

		# The page updates again and then both items show up

		# There is some text telling me that I have my own special URL to visit

		# My URL has my saved to do list!

if __name__ == '__main__':
	unittest.main(warnings='ignore')
