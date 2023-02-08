#!/bin/python3


import re


def validate_html(html):
    '''
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    tags = _extract_tags(html)
    if len(html) == 0:
        return True
    if len(tags) < 2:
        return False
    stack = []
    for tag in tags:
        if tag[1] != '/':
            stack.append(tag[1:-1])
        else:
            if not stack:
                return False
            if stack[-1] == tag[2:-1]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    '''
    return re.findall(r'<[^>]*>', html)
    '''

    tags = re.findall(r'<[^>]*>', html)
    individual_tag = ''
    filtered_tags = []
    for tag in tags:
        if ' ' in tag and '/' not in tag or 'href' in tag:
            for char in tag:
                if char != ' ':
                    individual_tag += str(char)
                else:
                    individual_tag += '>'
                    filtered_tags.append(individual_tag)
                    individual_tag = ''
                    break
        else:
            filtered_tags.append(tag)
    print("filtered_tags=", filtered_tags)
    return filtered_tags
