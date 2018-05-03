
#!/usr/bin/python3.6 pytest

# Author: Roy Tate (githubtater)

import unittest
import html_render as hr


class TestHTMLRender(unittest.TestCase):
    test_string = '<<TEST_STRING_FOR_TEXT_INSERTION_5599>>'

    def test_verify_element_class_attributes(self):
        element_attr = hr.Element()
        self.assertEqual(element_attr.tagname, 'html')
        self.assertEqual(element_attr.indent, ' ')

    def test_element_class_append(self):

        element = hr.Element()
        element.append(self.test_string)
        self.assertEqual(element.content[-1], self.test_string)

    def test_element_class_accepts_kwargs(self):
        kwarg1 = '1'
        kwarg2 = 'first'
        element_attr = hr.Element(self.test_string, kwarg1, kwarg2)
        self.assertEquals(element_attr.attributes, (kwarg1, kwarg2))


