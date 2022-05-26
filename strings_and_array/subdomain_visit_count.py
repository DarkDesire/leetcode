from typing import *

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_to_count_map = {}
        for pair in cpdomains:
            count, domain = pair.split(' ',2)
            subdomains = domain.split('.')
            for idx in range(0, len(subdomains)):
                subdomain = '.'.join(subdomains[idx:])
                domain_to_count_map[subdomain] = domain_to_count_map.get(subdomain, 0) + int(count)
            
        return [f'{count} {domain}' for domain, count in domain_to_count_map.items()]