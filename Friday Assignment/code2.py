import re

text = """I know a set of email addresses 
that we can extract using expression1:
abc.df@somecompany.co.uk, abc@gmail.com, 
xyz.ab@tpa.com, dfg.gh@dp.cp.net .
But what about 11.234.abc.ghy@tp.edu, let's check."""

pattern = r'([a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z]+\.(com|uk|in))'
matches = re.findall(pattern, text)


emails = [match[0] for match in matches]
print(emails)