#!/usr/bin/env python3

"""
usage: url2domain [-h] [-o OUTPUT_NAME] [-a ALIASES] [-d MAX_DEPTH]
                  input_name

positional arguments:
  input_name            Input file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_NAME, --output_name OUTPUT_NAME
                        Output file name
  -a ALIASES, --aliases ALIASES
                        Domain aliases to replace (JSON format)
  -d MAX_DEPTH, --max-depth MAX_DEPTH
                        Maximum domain depth to consider (optional)
"""

import json
from argparse import ArgumentParser
from os.path import basename, splitext
from typing import Union
# from urllib.parse import urlparse
# from tldextract import extract as tld

ALIASES = {
    # 'fb.me': 'facebook.com',
    # 't.co':  'twitter.com',
    # 'youtu.be': 'youtube.com',
}


def url2domain(url: Union[str, list], aliases=ALIASES, max_depth: int = None) -> list:
    return [
        aliases.get(
            url,
            url
        )\
        for url in [
            '.'\
            .join(
                url
                .split('://', 1)[-1]
                .split('?', 1)[0]
                .split('#', 1)[0]
                .split('&', 1)[0]
                .split('/', 1)[0]
                .split('.')[-(max_depth or 0):]
            )\
            .replace('www.', '')
            # urlparse(url).netloc,    # Slower, better results
            # '%s.%s' % tld(url)[1:],  # Slowest, best results
            for url in (
                url if type(url) == list else [url]
            )
        ]
    ]


def readfile(file_name: str):
    with open(file_name, "r", errors="ignore") as f:
        return list(x.rstrip() for x in f.readlines())


def writefile(file_name: str, urls: list):
    with open(file_name, "w", errors="ignore") as f:
        list(f.write(f"{url}\n") for url in urls)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("input_name",
                        action="store",
                        help="Input file name")

    parser.add_argument("-o", "--output_name",
                        action="store",
                        help="Output file name")

    parser.add_argument("-a", "--aliases",
                        action="store",
                        default={},
                        help=f"Domain aliases to replace (JSON format)",
                        type=json.loads)

    parser.add_argument("-d", "--max-depth",
                        action="store",
                        default=None,
                        help=f"Maximum domain depth to consider (optional)",
                        type=int)

    args = vars(parser.parse_args())

    input_name = args.pop("input_name")
    output_name = args.pop("output_name")

    if not output_name:
        name, ext = splitext(basename(input_name))
        output_name = f"{name}_DOMAINS{ext}"

    writefile(
        output_name,
        url2domain(
            readfile(input_name),
            **args
        )
    )
