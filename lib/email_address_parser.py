# your code goes here!
import re

class EmailAddressParser:
    # mail_filter = r"\w+@\w+\.\w+"
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    def __init__(self,emails):
        self.emails = emails

    def parse(self):
        # pattern = re.compile(EmailAddressParser.mail_filter)
        # valid = pattern.match(self.email)
        # return valid

        strings = re.split(r',|\s', self.emails)
        parsed_emails = set()
        for string in strings:
            
            if self.email_regex.fullmatch(string):                
                parsed_emails.add(string)

        return sorted(list(parsed_emails))