#!/usr/bin/python3

## Author/Student:  Roy Tate (githubtater)

import unittest
import mailroom_backend as mb
import mailroom_ui as ui

class TestMailroomBackend(unittest.TestCase):

    def setUp(self):
        self.collection = mb.DonorCollection()

    def test_donor_collection_instance_created(self):
        assert isinstance(self.collection, mb.DonorCollection)

    def test_donor_can_be_added(self):
        self.collection.add('Fred Flintstone', 999)
        self.assertEqual(self.collection.donors['Fred Flintstone'], 'this')



if __name__=="__main__":
    unittest.main()