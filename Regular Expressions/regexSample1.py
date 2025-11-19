import re
rePhone = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchObj = rePhone.search("My phone number is 503-262-4844")
print(matchObj.groups())

# a | character gives you an or possibility
rePhone2 = re.compile(r'(\d{3}-)|(\(\d{3}\))\d{3}-\d{4}')
matchObj2 = rePhone.search("My phone number is (503)262-4844")
print(matchObj.groups())

rePhone3 = re.compile(r'\(?\d{3}\)?-?\d{3}-?\d{4}')
matchObj3 = rePhone.search("My phone number is 5032624844")
print(matchObj.groups())