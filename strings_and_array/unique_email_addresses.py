from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local_name, domain_name = email.split('@',2)
            if '@' in local_name or '@' in domain_name: # Each emails[i] contains exactly one '@' character.
                continue
            if local_name == '' or domain_name == '': # All local and domain names are non-empty.
                continue 
            if local_name.startswith('+'): # Local names do not start with a '+' character.
                continue
            if not domain_name.endswith(".com"): # Domain names end with the ".com" suffix.
                continue 
            
            local_name = local_name.replace('.','')
            local_name_cleared = local_name.split('+')[0]
            
            if email not in email_set:
                email_set.add(f'{local_name_cleared}@{domain_name}')
        return len(email_set)
