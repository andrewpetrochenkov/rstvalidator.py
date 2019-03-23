#!/usr/bin/env python
"""validate .rst file(s)"""
# -*- coding: utf-8 -*-
import click
import sys
import rstvalidator

MODULE_NAME = "rstvalidator"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME


@click.command()
@click.argument('paths', nargs=-1, required=True)
def _cli(paths):
    for path in paths:
        reports = rstvalidator.rstvalidator(path)
        if reports:
            print(path)
            print("\n".join(map(str, reports)))
            sys.exit(1)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
