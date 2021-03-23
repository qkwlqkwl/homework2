from homework.appium_work1.pages.app import App


class TestAddMember:
    def setup(self):
        self.app = App()

    def test_addMember(self):
        add = self.app.goto_main().goto_maillist_page().goto_addmember_page().addmember()
        add.addMemberText()
        add.varity_ok()
