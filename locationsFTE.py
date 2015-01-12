import requests
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

driver = webdriver.Firefox()
base_facebook = "https://graph.facebook.com/v1.0/"


urls = ["http://fivethirtyeight.com/datalab/everything-steven-soderbergh-watched-and-read-in-2014/","http://fivethirtyeight.com/datalab/chris-christie-2016-president-republican-primary-overrated/","http://fivethirtyeight.com/datalab/13-nba-teams-have-benches-better-than-the-knicks/","http://fivethirtyeight.com/features/how-much-fuel-we-need-to-leave-buried-to-beat-climate-change/", "http://fivethirtyeight.com/datalab/chris-christie-2016-president-republican-primary-overrated/"]

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
  commenters = driver.find_elements_by_class_name("profileName")
  locations = driver.find_elements_by_class_name("uiLinkSubtle") 

  morec = True
  while morec:
    try:
      morec = driver.find_element_by_class_name("pam")
      morec.click()
      time.sleep(2)
  
      comments = driver.find_elements_by_class_name("postText")
      commenters = driver.find_elements_by_class_name("profileName")
      locations = driver.find_elements_by_class_name("uiLinkSubtle") 
    except:
      return comments, commenters, locations

  return comments, commenters, locations

def print_coms(comments, commenters, locations):

  coms = []
  ppl = []
  locs = []

  for com in comments:
    text = com.text
    print text
    coms.append(text)

  for com in commenters:
    per = com.get_attribute("href")
    print per
    ppl.append(per)

  for loc in locations:
    l = loc.text
    locs.append(l)

  return coms, ppl, locs

def write(comments, commenters, locs):

  zipped = (zip(commenters, comments, locs))
  print zipped
  return zipped

def write_coms(zipped, url, outfile):
  names = []
  text = []
  f = open(outfile, "a")
  writer = csv.writer(f)


  for fid, com, loc in zipped:
    try:
      if len(fid) > 100:
        continue

      fid = fid.split("/")[-1]
    
    except:
      continue


    fb_url = base_facebook + fid
     
    try:
      fbinfo = requests.get(fb_url).json()    
      print fbinfo      
      tup = (fbinfo["name"],fbinfo["gender"],fid,loc,url, str(com))
      if len(tup) < 4:
        continue
 
      writer.writerow(tup)
    

    except:
      print "Error", sys.exc_info()[0]

    f.flush()

for url in urls:

  c, cs, locs = fte_fetch_comments(url)
  c, cs, locs = print_coms(c, cs, locs)
  zi = write(c,cs, locs)
  write_coms(zi, url, "com7.csv")
  print len(c)
  print len(cs)
  print len(locs)
