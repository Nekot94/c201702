import re
url = input()
q = input()
res = re.search(r"(?<=(\&|\?){}=)[^\&\?\=\#\n]+(?=\&|)".format(q), url)
if res:
    print(res.group(0))
