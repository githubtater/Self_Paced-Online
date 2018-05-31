
#!/usr/bin/python3.6 pytest

# Author: Roy Tate (githubtater)

import unittest
import html_render as hr
from io import StringIO

class TestHTMLRender(unittest.TestCase):
    test_string = '<<TEST_STRING_FOR_TEXT_INSERTION_5599>>'

    def test_verify_element_class_attributes(self):
        element_attr = hr.Element()
        self.assertEqual(element_attr.tag, '')
        self.assertEqual(element_attr.indent, '    ')

    def test_element_class_appends_string(self):
        element = hr.Element()
        element.append(self.test_string)
        self.assertEqual(element.content[-1], self.test_string)

    def test_element_class_accepts_kwargs(self):
        kwarg1 = '1'
        kwarg2 = 'first'
        element_attr = hr.Element(self.test_string, kwarg1, kwarg2)
        self.assertEquals(element_attr.args, (kwarg1, kwarg2))

    def test_element_class_renders_correctly(self):
        pass


    def test_html_class(self):
        new_html = hr.Html()
        assert isinstance(new_html, hr.Html)


    def test_body_class(self):
        new_body = hr.Body()
        assert isinstance(new_body, hr.Body)