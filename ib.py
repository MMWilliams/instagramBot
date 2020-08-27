from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys
from time import sleep
import datetime

now = datetime.datetime.now()
time =now.strftime("%H:%M:%S")

print("Initiating instagram bot")
print(time)
#this bot outolikes pics with the reqpective hashtags
# Only run for 5 hours at a time
def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = "username" #your username
        self.password = "password" #your password

        self.driver = webdriver.Chrome(executable_path = '/Applications/chromedriver')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        sleep(4)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        sleep(5)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        sleep(5)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(60)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(10)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            sleep(60)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                sleep(random.randint(5, 10))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                #commenting on pictures as well
                #comment_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                #comment_button().click()
                #comment_content = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').send_keys("great photo")
                #comment_send = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').send_keys(KEYS.)

                #
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    sleep(1)
            except Exception as e:
                sleep(60)
            unique_photos -= 1

if __name__ == "__main__":

    username = "username"
    password = "password"
    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ['energy', 'renewableenergy', 'philly', 'apartment',
                'entrepreneur', 'solar', 'savings', 'personalfinance', 'america'
               ,'amazon','freedom','photooftheday','fashion','beautiful','happy',
                'cute','tesla','politics','freedom','picoftheday','leadership','tesla',
                'selfie','summer','art','instadaily','friends',
                'fitness','nature','shopping','electricity','style','health','spacex']

    #hashtags = ['fun', 'instagood', 'phila', 'selfie', 'me', 'success', 'philadelphia', 'cure', 'love', 'life', 'tbt',
    # 'artificialintelligenc', 'iphonesia', 'instamood', 'nofilter', 'happy', 'beautiful',
    # 'like4like', 'picoftheday', 'amazing', 'vscocam', 'followforfollow']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            sleep(10)
            ig = InstagramBot(username, password)
            ig.login()



#if (time == "19:30:00"):
#   print("sleep at:" & time)
#    #sys.exit
#    sleep(39600)
     #at 10pm  sleep for 11 hours
    #continues at 11am.

#if (time == "15:01:00"):
    #print("sleep at:" & time)
    #sleep(7200)
    # at 3pm sleep fo 2 hours
    #continue at 5pm


#if (time == "18:03:00"):
#    print("sleep at:" & time)
#    sleep(10800)
    # at 6pm sleep for 3 hours
    #continue at 9pm
