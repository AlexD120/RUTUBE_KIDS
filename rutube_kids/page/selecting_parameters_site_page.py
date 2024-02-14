import allure
from selene import browser, have
from selene.support.shared.jquery_style import s


class SimpleUserParametersPage:
    def __init__(self):
        self.accept_cookies = s(
            '[data-testid="accept-cookie-notification_agree-button"]'
        )
        self.choosing_age_group = s(
            '[data-testid="onboarding-form_age-selection-card_AGE_GROUP_8"]'
        )
        self.should_you_like_title = s(
            '[data-testid="onboarding-form_what-do-you-like_title"]'
        )
        self.favorite_channel = s(
            '[data-testid="onboarding-form_favorite-card_49062efa-a118-46b2-b035-347fa29309a6"]'
        )
        self.start_viewing_button = s(
            '[data-testid="onboarding-form_start-watch-button"]'
        )

    @allure.step('Open main page')
    def open(self):
        browser.open('https://kids.rutube.ru/onboarding')
        return self

    @allure.step('')
    def age_group(self):
        self.accept_cookies.click()
        self.choosing_age_group.click()

    @allure.step('')
    def you_like_channel(self):
        self.should_you_like_title.should(have.text('Выбери, что тебе нравится'))
        self.favorite_channel.click()
        self.start_viewing_button.click()
