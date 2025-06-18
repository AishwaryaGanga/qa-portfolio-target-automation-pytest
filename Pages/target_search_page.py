import time

from selenium.webdriver.common.by import By
from Pages.basepage import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenTargetPage(Page):

    SEARCH_TAB = (By.ID, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test *= 'SearchButton']")
    HOVER_TO = (By.CSS_SELECTOR, "[title *= 'Fluoride-Free Baby Toothpaste Pear']")
    PRODUCT_TITLE = (By.ID, "pdp-product-title-id")

    def open_target_page(self):
        self.open_url(self.base_url)

    def search_item(self):
        self.input_text("Dr. Brown's Toddler Toothbrush with Soft Bristles", *self.SEARCH_TAB)
        self.click(*self.SEARCH_BUTTON)

    def find_item(self):

        # Scroll to bottom just in case (optional)
        time.sleep(40)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(35)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(35)

        # Wait until the item is visible
        locate_the_item = self.wait.until(EC.visibility_of_element_located(self.HOVER_TO))
        item = (locate_the_item).text
        print(item)

        # # Scroll item into view (fixed typo)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locate_the_item)
        time.sleep(4)
        #
        # # Hover over the item
        ActionChains(self.driver).move_to_element(locate_the_item).perform()
        time.sleep(10)

        # Click the item
        #self.click(*self.HOVER_TO)

        element = self.wait.until(EC.element_to_be_clickable(self.HOVER_TO))

        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(4)

    def verify_page_title(self):
        # self.verify_partial_text('Fluoride-Free Baby Toothpaste Pear & Apple Flavor', *self.PRODUCT_TITLE)
        # title = (self.PRODUCT_TITLE).text
        # print(title)
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLE))
        title = self.find_element(*self.PRODUCT_TITLE).text
        assert "Fluoride-Free Baby Toothpaste Pear & Apple Flavor" in title, f"Title mismatch: {title}"





