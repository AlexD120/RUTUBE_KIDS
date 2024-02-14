from rutube_kids.page.selecting_parameters_site_page import SimpleUserParametersPage
from rutube_kids.page.simple_user_search_page import SimpleUserSearchPage


class ApplicationUa:
    def __init__(self):
        self.simpple_users_params_page = SimpleUserParametersPage()
        self.simpple_users_search_page = SimpleUserSearchPage()


app = ApplicationUa()
