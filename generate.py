#!/usr/bin/python3

import argparse
import os
import xml.etree.ElementTree as ET
import random
import sys

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
logger = logging.getLogger('RTB')


def read_files(directory='icons'):
    logger.debug(f'Reading from directory {directory}')
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('svg')]
    logger.debug(f'Found {len(files)} svg files')
    return files


def pick_items(files, count=25):
    sample = random.sample(files, count)
    logger.debug(f'Files chosen: {", ".join(sample)}')
    return sample


def item_content(item):
    try:
        tree = ET.parse(item)
        root = tree.getroot()
        content = []
        for child in root.findall('{http://www.w3.org/2000/svg}g'):
            content += ET.tostring(child).decode('utf-8').split('\n')
        return content
    except ET.ParseError as e:
        logger.error(f'Failed to parse {item}, error message:')
        logger.error(e)


def replace_in_template(items, template='template.svg.tmpl'):
    with open(template) as t:
        lines = [line.strip() for line in t.readlines()]
        marker = lines.index('@INSERT@')

        header = lines[:marker]
        footer = lines[marker + 1:]
        body = []

        x, y = 0, 0
        spacing = 36

        for item in items:
            logger.debug(f'Processing {item}')
            content = item_content(item)
            body.append(f'<g id="g-{item}" transform="translate({x * spacing}, {y * spacing})">')
            body.append(f'<!-- {item} -->')
            body += item_content(item)
            body.append(f'<!-- /{item} -->')
            body.append(f'</g>')
            x += 1
            if x % 5 == 0:
                y += 1
                x = 0

        return header + body + footer


def write_output(content, outfile='output/rtb.svg'):
    open(outfile, 'w').write('\n'.join(content))
    logger.info(f'Written to {outfile}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Road Trip Bingo generator")
    parser.add_argument('--count', type=int, nargs=1, default=10,
                        help='The number of files to generate (default: 10)')
    parser.add_argument('--output', type=str, nargs=1, default='output',
                        help='The directory to write the results to')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    files = read_files()
    for i in range(args.count[0]):
        items = pick_items(files)
        output = replace_in_template(items)
        fname = os.path.join(args.output, f'rtb-{i}.svg')
        write_output(output, outfile=fname)
