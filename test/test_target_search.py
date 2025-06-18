


class TestTargetSearch:

    def test_open_target(self,app):
        app.open_target_page.open_target_page()
        app.open_target_page.search_item()
        app.open_target_page.find_item()
        app.open_target_page.verify_page_title()


