#!/usr/bin/python3

## Author/Student:  Roy Tate (githubtater)


import unittest
import classmailroom as cm


class MailroomTest(unittest.TestCase):


    def setUp(self):
        pass

    def test_new_donor_creation(self):
        donor1 = cm.Donor('bobby jones', 1000)
        self.assertEqual(donor1.name, 'Bobby Jones')
        self.assertEqual(sum(donor1.donations), 1000)

    def test_new_donation_added_to_current_donor(self):
        donor1 = cm.Donor('bobby jones', 1000)
        self.assertEqual(donor1.name, 'Bobby Jones')
        self.assertEqual(sum(donor1.donations), 1000)
        donor1.add_donation(2122)
        self.assertEqual(sum(donor1.donations), 3122)



if __name__ == "__main__":
    unittest.main()