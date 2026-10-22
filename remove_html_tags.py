import re
def strip_tags(html):
    pattern = '<.*?>'
    html = re.sub(pattern,"",html)
    

    return html
