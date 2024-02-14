from allure_commons._allure import step
from rutube_kids.helpers.application import app


def test_registration():
    with step('1. Open site'):
        app.simpple_users_params_page.open()
    with step('2. Selecting a section by age'):
        app.simpple_users_params_page.age_group()
    with step('3. Choose what you like'):
        app.simpple_users_params_page.you_like_channel()
    with step('4. Search'):
        app.simpple_users_search_page.search_result()
