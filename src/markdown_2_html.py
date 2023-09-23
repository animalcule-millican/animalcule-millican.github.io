#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert Markdown files to HTML files.

"""
import argparse
import markdown
import os


def arg_parser():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input directory containing Markdown files')
    parser.add_argument('-o', '--output', help='output directory for HTML files')
    return parser.parse_args()

def file_list(input_dir):
    """Return a list of Markdown files in the input directory."""
    return [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.txt') or f.endswith('.md')]

def markdown_2_html(input_file, output_dir):
    """Convert a Markdown file to HTML and return the HTML as a string."""
    # extract base name of file
    file_name = os.path.basename(input_file)
    # create output file name
    out_name = file_name.split('.')[0] + '.html'
    print(input_file)
    print(f"{output_dir}/{out_name}")
    # convert markdown to html
    with open(input_file, 'r') as in_handle, open(f"{output_dir}/{out_name}", 'w') as out_handle:
        markdown_text = in_handle.read()
        html = markdown.markdown(markdown_text)
        out_handle.write(html)

def main():
    args = arg_parser()
    # create output directory if it doesn't exist
    if not os.path.exists(args.output):
        os.mkdir(args.output)
    # get list of markdown files
    files = file_list(args.input)
    # convert each markdown file to html
    for f in files:
        markdown_2_html(f, args.output)

if __name__ == '__main__':
    main()