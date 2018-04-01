from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = defaultdict(int)
        for domain in cpdomains:
            value, s = domain.split(' ')
            tmp = s
            while True:
                d[tmp] += int(value)
                pos = tmp.find('.')
                if pos != -1:
                    tmp = tmp[pos + 1:]
                    continue
                else:
                    break
        return [str(v) + ' ' + k for k, v in d.items()]

