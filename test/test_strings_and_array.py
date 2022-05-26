
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
    