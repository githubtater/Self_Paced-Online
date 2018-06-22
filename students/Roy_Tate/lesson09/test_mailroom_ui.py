#!/usr/bin/python3

## Author/Student:  Roy Tate (githubtater)

import unittest
import mailroom_ui as ui

class TestMailroomUI(unittest.TestCase):

    def test_mailroom_(self):
        self.collection = ui.MailroomUI()
        self.ui = ui.MailroomUI()
        assert isinstance(self.ui, ui.MailroomUI)



if __name__=="__main__":
    unittest.main()