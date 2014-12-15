# -*- coding: utf-8 -*-

import yaml
import markdown

# Expects a multi-line string as parameter
# extracts two sections: the one between the first and the second line equal to '---' and the one after the second line equal to '---'
# The first section is assumed to be yaml and converted to a dictionary, the second section is assumed to be markdown and converted to html
# the results are returned as a tuple
def convert(input):

    lines = input.splitlines()
    i = 0

    # find the start of the yaml section
    try:
        while lines[i].strip() != '---':
            i += 1
    except(IndexError):
        print "Malformed input"
        exit(0)

    yaml_start = i + 1
    i += 1

    # find the end of the yaml section (and the beginning of the markdown section)
    try:
        while lines[i].strip() != '---':
            i += 1
    except(IndexError):
        print "Malformed input"
        exit(0)

    yaml_end = i
    md_start = i + 1

    # create return values and return them    
    yaml_lines = input.splitlines()[yaml_start:yaml_end]
    yaml_section = '\n'.join(yaml_lines)
    
    md_lines = input.splitlines()[md_start:]
    md_section = '\n'.join(md_lines)

    dictionary = yaml.load(yaml_section)
    html = markdown.markdown(md_section)

    return dictionary, html

    

    
