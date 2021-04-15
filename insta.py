## Program runs and is up to date as of 4/15/2021. Instagram may change its front-end in the 
## future leading to bugs.

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

class InstaBot:
    def __init__(self, username, password):
        """
        init chrome driver binary path and get username and password from user
        """
        self.chrome_options = Options()
        self.chrome_options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.exepath = 'E:/Personal Projects/insta unfollow finder/chromedriver.exe'
        self.driver = webdriver.Chrome(options=self.chrome_options,executable_path=self.exepath)
        self.username = username ## Saving a reference to our username and password
        self.password = password ## incase we need it in other methods.
		
		
    def login_insta(self):
        """
        login into instagram and prepair instagram for progress
        """
        self.driver.get("https://instagram.com") ## Opens up IG with the chrome driver. 
        sleep(3) ## Wait for login page to load up. 
        username_field = self.driver.find_element_by_xpath("//input[@name=\'username\']")\
        	.send_keys(username)
        password_field = self.driver.find_element_by_xpath("//input[@name=\'password\']")\
        	.send_keys(password)
        login_submit = self.driver.find_element_by_xpath("//button[@type='submit']")\
        	.click()        
        sleep(3) ## Waiting for the 'Do you want to save your login info' banner.   
        dont_save_info = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        	.click()    
        sleep(3) ## Waiting for the 'Turn on notifications?' banner.    
        disable_notifications = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        	.click()    
    def get_unfollowers(self):
        """
        find and get all followers and followings and finaly print all of unfollowers them
        """
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        """
        find all of followers and followings by scrolling
        """
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

# Main
username, password = "username","password" #Put your username and password here
my_bot = InstaBot(username, password)
my_bot.login_insta()
my_bot.get_unfollowers()
