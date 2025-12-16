from core.base_page import BasePage
from playwright.sync_api import Page, expect

class TwitterPage(BasePage):

    URL = "https://x.com/orangehrm?lang=en"
    TITLE_UNDER_AVATAR = "(//span[normalize-space()='OrangeHRM'])[4]"
    X_TOP_LEFT = "//a[@aria-label='X']"

    def __init__(self, page:Page):
        super().__init__(page)  
        self.top_left_x_icon = page.locator(self.X_TOP_LEFT)
        self.title_under_avatar = page.locator(self.TITLE_UNDER_AVATAR)

    def assert_x_icon_visible(self):
        expect(self.top_left_x_icon).to_be_visible(timeout=10000)

    def assert_orangehrm_title_visible(self):
        expect(self.title_under_avatar).to_be_visible(timeout=10000)