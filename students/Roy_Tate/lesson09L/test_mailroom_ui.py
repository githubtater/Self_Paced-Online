#!/usr/bin/python3

## Author/Student:  Roy Tate (githubtater)

import unittest
import mailroom_ui as mr

class TestMailroomUI(unittest.TestCase):

    def test_mailroom_(self):
        self.mr = mr.MailroomUI()
        assert isinstance(self.mr, mr.MailroomUI)