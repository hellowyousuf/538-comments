import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
base_facebook = 

def fte_fetch_comments(url):

  driver.get(url)
  elem = driver.find_element_by_class_name("fte-expandable-title")
  elem2 = driver.find_element_by_class_name("entry-comments-content")

  elem.click()
  elem2.click()

  source = driver.page_source
  index = source.find("iframe id=\"")
  idstring = source[index:index+30]
  spl = idstring.split("\"")
  fid = spl[1]
  
  driver.switch_to.frame(fid)
  
  comments = driver.find_elements_by_class_name("postText")
