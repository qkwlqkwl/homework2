from homework.appium_work1.pages.app import App


class TestSign:
    def setup(self):
        self.app = App()

    def test_sign(self):
        self.app.goto_main().goto_maillist_page().goto_addmember_page().addmember().addMemberText()
