import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
base_facebook = "http://graph.facebook.com"

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
  commenters = driver.find_elements_by_class_name("postActor")

  morec = driver.find_element_by_class_name("pam")
  morec.click()

  
  comments = driver.find_elements_by_class_name("postText")
  commenters = driver.find_elements_by_class_name("postActor")
 
  return comments, commenters

def print_coms(comments, commenters):

  for com in comments:
    print com.text

  for com in commenters:
    print com.get_attribute("href")

c, cs = fte_fetch_comments("http://fivethirtyeight.com/datalab/chris-christie-2016-president-republican-primary-overrated/")

print_coms(c, cs) 
