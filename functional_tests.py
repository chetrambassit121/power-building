# https://www.obeythetestinggoat.com/book/chapter_01.html

# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'Django' in browser.title 

# browser.quit()



# open up powerbuilding on gitbash ... run the server ... project should open on localhost8000
# open up on a seperate gitbash terminal .. run .. python functional_tests.py 
# this coding will open firefox and display our website in localhost:8000 
# ..........................................




















# https://www.obeythetestinggoat.com/book/chapter_02_unittest.html
# create a 'story', or a user interaction with website 

from selenium import webdriver
import unittest                              



class NewVistorTest(unittest.TestCase):     

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
        self.fail('Finish the test!')  

        # She is invited to enter a to-do item straight away
        
if __name__ == '__main__':  
    unittest.main()


