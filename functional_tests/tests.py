from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep


class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get(self.live_server_url)

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

		# When I hit enter, I go to a new page and it lists "1: Water the garden"
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')

		self.check_for_row_in_list_table('1: Water the garden')

		# There's still a text box
		# I enter "Fly spray Jesse"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Fly spray Jesse')
		inputbox.send_keys(Keys.ENTER)

		# The page updates again and then both items show up
		self.check_for_row_in_list_table('1: Water the garden')
		self.check_for_row_in_list_table('2: Fly spray Jesse')

		# Now there is a new user named Francis

		# Francis has a new browser session, clean of Edith's cookies
		self.browser.quit()
		self.browser = webdriver.Firefox()

		# Francis visits the home page and DOES NOT see Edith's list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_elements_by_tag_name('body').text
		self.assertNotIn('Water the garden', page_text)
		self.assertNotIn('Fly spray Jesse', page_text)

		# Seeing a blank page, Francis enters a new item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		# Now Francis has his own URL too. It is different from Edith's
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		# None of Edith's list appears in Francis' list, but his stuff is there
		page_text = self.browser.find_element_by_tag_name('body')
		self.assertNotIn(page_text, 'Water the garden')
		self.assertIn(page_text, 'Buy milk')
