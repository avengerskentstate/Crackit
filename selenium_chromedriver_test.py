import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Crackit_TestCase(unittest.TestCase):
    
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://crackit.pythonanywhere.com/")
        

    def tearDown(self):
        self.driver.close()
     
    

    def test_001_game_rules_help_page_exists(self):
      self.driver.find_element_by_class_name("btn-warning").click()
      header1=self.driver.find_element_by_tag_name("button")
      s='PLAY'
      self.assertEqual(s,(header1.text))
      time.sleep(5)


    def test_002__game_play_button(self):
      self.driver.find_element_by_class_name("btn-warning").click()
      header2=self.driver.find_element_by_tag_name("button")
      s='PLAY'
      self.assertEqual(s,(header2.text))
      time.sleep(3)
      self.driver.find_element_by_class_name("btn-warning").click()
      header3=self.driver.find_element_by_tag_name("button")
      s1=''
      self.assertEqual(s1,(header3.text))	
      time.sleep(20)


    def test_03_game_quit_button_exists(self):
      self.driver.find_element_by_class_name("btn-warning").click()
      header2=self.driver.find_element_by_tag_name("button")
      s='PLAY'
      self.assertEqual(s,(header2.text))
      time.sleep(3)
      self.driver.find_element_by_class_name("btn-danger").click()
      header3=self.driver.find_element_by_tag_name("button")
      s1=''
      self.assertEqual(s1,(header3.text))	
      time.sleep(5)

    
   
   
	  
if __name__ == "__main__":
    unittest.main(verbosity=2)