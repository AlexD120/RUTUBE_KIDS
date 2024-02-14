import allure
from selene import have
from selene.support.shared.jquery_style import s


class SimpleUserSearchPage:

    def __init__(self):
        self.search_input = s('[data-testid="main-search_input"]')
        self.select_video_from_search = s(
            '[data-testid="video-results-page_video-card-container_14d4b993-3b96-44fa-9dd2-5b0411026222"]'
        )
        self.should_title_video = s(
            '[data-testid="video-info_title_14d4b993-3b96-44fa-9dd2-5b0411026222"]'
        )

    @allure.step('Search Video')
    def search_result(self):
        self.search_input.type('супер кот учим цифры').press_enter()
        self.select_video_from_search.should(have.text('УЧИМ ЦИФРЫ')).click()
        self.should_title_video.should(have.text('Три Кота Сидим дома с Супер котом'))
