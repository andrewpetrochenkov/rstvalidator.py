#!/usr/bin/env python
"""validate .rst files"""
# -*- coding: utf-8 -*-
import os
import sys
from docutils import utils
from docutils.core import publish_parts
import public

"""
'pygments' required
"""

reports = []

orignal_system_message = utils.Reporter.system_message


def rst2html(value):
    """ Run rst2html translation """
    parts = publish_parts(source=value, writer_name="html4css1")
    return parts['whole']


def system_message(self, level, message, *children, **kwargs):
    args = [self, level, message] + list(children)
    result = orignal_system_message(*args, **kwargs)
    if level >= self.WARNING_LEVEL:
        # All reST failures preventing doc publishing go to reports
        # and thus will result to failed checkdocs run
        sys.modules[__name__].reports.append(message)
    return result


@public.add
def rstvalidator(path):
    """validate .rst file"""
    sys.modules[__name__].reports = []

    text = open(path).read()
    # Monkeypatch docutils for simple error/warning output support
    utils.Reporter.system_message = system_message
    old_stderr = sys.stderr
    sys.stderr = open(os.devnull, "w")
    try:
        rst2html(text)
        utils.Reporter.system_message = orignal_system_message
        return reports
    finally:
        sys.stderr.close()
        sys.stderr = old_stderr
