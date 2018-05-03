#!/usr/bin/env python3

## Student:  Roy Tate (githubtater)


class Element:
    tagname = 'html'
    indent = ' '

    def __init__(self, content=None, *args):
        if content:
            self.content = [content]
        else:
            self.content = []
        self.attributes = args


    def append(self, string=None):
        self.content.append(string)

    def render(self, f):
        pass


class Html:
    pass


class Body:
    pass
