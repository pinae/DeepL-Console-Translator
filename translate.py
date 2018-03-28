#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
import argparse
import re
import requests

DEEP_L = 'https://deepl.com/jsonrpc'


def main():
    parser = argparse.ArgumentParser(
        description='Translate sentences using the DeepL API.')
    parser.add_argument(
        '-t', '--target',
        default='EN',
        dest='target_lang',
        choices=['EN', 'DE', 'FR', 'ES', 'IT', 'NL', 'PL'],
        help="The language to translate into. Defaults to English.")
    parser.add_argument(
        '-s', '--source',
        default='auto',
        dest='source_lang',
        choices=['DE', 'EN', 'FR', 'ES', 'IT', 'NL', 'PL', 'auto'],
        help="The language to translate from. Defaults to 'auto'.")
    parser.add_argument(
        'text',
        nargs='+',
        help="The text to be translated.")
    args = parser.parse_args()

    text = " ".join(args.text)
    split_pattern = re.compile(r"([^\.!\?;]+[\.!\?;]*)")
    sentences = [s for s in split_pattern.split(text) if len(s) > 0]
    payload = {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "id": 1,
        "params": {
            "jobs": [{"kind": "default", "raw_en_sentence": s} for s in sentences],
            "lang": {"user_preferred_langs": ["EN", "DE"],
                     "source_lang_user_selected": args.source_lang,
                     "target_lang": args.target_lang},
            "priority": 1}}

    req = requests.post(DEEP_L, json=payload)

    if req.ok:
        translations = req.json()['result']['translations']
    else:
        print("There was an error during the call: {}".format(req.status_code))
        import sys
        sys.exit(1)

    print(" ".join(
        sorted(t['beams'], key=lambda b: -1 *
               b['score'])[0]['postprocessed_sentence']
        for t in translations))


if __name__ == '__main__':
    main()
