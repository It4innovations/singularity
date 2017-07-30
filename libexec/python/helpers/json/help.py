#!/usr/bin/env python

'''

help.py: python help printer for Singularity help

This function will look for a runscript.help file in the
container base, and print to the console if provided.
If an app name is provided, it will look in the app folder
instead

If not, nothing is printed.

ENVIRONMENTAL VARIABLES that are used for this executable:

SINGULARITY_MOUNTPOINT

Copyright (c) 2017, Vanessa Sochat. All rights reserved.

'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                os.path.pardir,
                                os.path.pardir)))  # noqa

import optparse
from defaults import getenv
from message import bot


from message import bot
import json
import re


def HELP(filepath, pretty_print=False):
    '''HELP will print a help file to the console for a user,
    if the file exists. If pretty print is True, the file will be
    parsed into json.
    :param filepath: the file path to show
    :param pretty_print: if False, return all JSON API spec
    '''

    # Definition File
    if os.path.exists(filepath):
        bot.verbose2("Printing help")
        text = read_file(filepath, readlines=False)

        if pretty_print:
            bot.verbose2("Structured printing specified.")
            text = {"org.label-schema.usage.singularity.runscript.help": text}
            print_json(text, print_console=True)
        else:
            bot.info(text)
    else:
        bot.verbose2("Container does not have runscript.help")


def get_parser():

    parser = optparse.OptionParser(description="HELP printer")

    parser.add_option("--file",
                      dest='file',
                      help="Path to json file to retrieve from",
                      type=str,
                      default=None)

    return parser


def main():

    parser = get_parser()

    try:
        (args, options) = parser.parse_args()
    except Exception:
        sys.exit(0)

    structured = getenv("SINGULARITY_PRINT_STRUCTURED", None)

    if args.file is None:
        bot.error("Please provide a help --file to print.")
        sys.exit(1)

    HELP(filepath=args.file,
         pretty_print=structured)


if __name__ == '__main__':
    main()
