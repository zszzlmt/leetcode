class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local_part, domain_part = email.split("@")
            local_part = local_part.replace(".", "")
            local_part = local_part.split("+")[0]
            email_set.add(local_part + domain_part)
        return len(email_set)
