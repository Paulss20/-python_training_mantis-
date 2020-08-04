from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from selenium.webdriver.support.select import Select


class Application:

     def __init__(self, browser, base_url):
          if browser == "firefox":
               self.wd = webdriver.Firefox()
          elif browser == "chrome":
               self.wd = webdriver.Chrome()
          elif browser == "edge":
               self.wd = webdriver.Edge()
          elif browser == "ie":
               self.wd = webdriver.Ie()
          else:
               raise ValueError("Unrecognized browser %s" % browser)
          self.wd.implicitly_wait(5) # t.k. stranica obnovlayetsay ne dinamicheski, to v etom priloghenii takoi neobhodimosti net. Alexei razreshil ostavit
          self.session = SessionHelper(self)
          self.project = ProjectHelper(self)
          self.base_url = base_url

     def is_valid(self):
          try:
               self.wd.current_url
               return True
          except:
               return False


     def open_home_page(self):
          wd = self.wd
          wd.get(self.base_url)

     # def return_to_home_page(self):
     #      wd = self.wd
     #      wd.find_element_by_css_selector("a[href='my_view_page.php']").click()


     def destroy(self):
         self.wd.quit()




