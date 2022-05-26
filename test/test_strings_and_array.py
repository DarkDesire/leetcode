
import unittest

class Test_VerifyingAnAlienDirectory(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        
        from strings_and_array.verifying_an_alien_directory import Solution
        self.s = Solution()

    def test_1(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertEqual(self.s.isAlienSorted(words, order), True)
    
    def test_2(self):
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertEqual(self.s.isAlienSorted(words, order), False)
    
    def test_3(self):
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.s.isAlienSorted(words, order), False)

    def test_4(self):
        words = ["kuvp", "q"]
        order = "ngxlkthsjuoqcpavbfdermiywz"
        self.assertEqual(self.s.isAlienSorted(words, order), True)

    def test_5(self):
        words = ["a", "b"]
        order = "cdefghijklmnopqrstuvwxyzab"
        self.assertEqual(self.s.isAlienSorted(words, order), True)

    def test_6(self):
        words = ["xn", "xc"]
        order = "xcnglkthsjuoqpavbfermiywzd"
        self.assertEqual(self.s.isAlienSorted(words, order), False)


class Test_UniqueEmailAddresses(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        
        from strings_and_array.unique_email_addresses import Solution
        self.s = Solution()

    def test_1(self):
        test1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        self.assertEqual(self.s.numUniqueEmails(test1), 2)
    
    def test_2(self):
        test2 = ["test.gmail+alex@leetcode.com","test.gmail+david@leetcode.com","anna.e.mail+bob.cathy@leetcode.com"]
        self.assertEqual(self.s.numUniqueEmails(test2), 2)
    
class Test_SubdomainVisitCount(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        
        from strings_and_array.subdomain_visit_count import Solution
        self.s = Solution()

    def test_1(self):
        input = ["9001 discuss.leetcode.com"]
        self.assertEqual(self.s.subdomainVisits(input), ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"])
        
    def test_2(self):
        input = ["900 google.mail.com"]
        self.assertEqual(self.s.subdomainVisits(input), ["900 google.mail.com", "900 mail.com", "900 com"])
    
    def test_3(self):
        input = ["1 a.b.c"]
        self.assertEqual(self.s.subdomainVisits(input), ["1 a.b.c", "1 b.c", "1 c"])
    
    def test_4(self):
        input = ["2 abc.d.ef"]
        self.assertEqual(self.s.subdomainVisits(input), ["2 abc.d.ef", "2 d.ef", "2 ef"])
    
    def test_5(self):
        input = ["2 abc.d.ef", "2 ghi.j.k"]
        self.assertEqual(self.s.subdomainVisits(input), ["2 abc.d.ef", "2 d.ef", "2 ef", "2 ghi.j.k", "2 j.k", "2 k"])
    
    def test_6(self):
        input = ["1 a.b.c", "2 ab.c"]
        self.assertEqual(self.s.subdomainVisits(input), ['1 a.b.c', '1 b.c', '3 c', '2 ab.c'])
        