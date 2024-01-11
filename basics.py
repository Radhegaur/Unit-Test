import unittest
from collections import Counter

class TestSplitMethod(unittest.TestCase):
    def test_split_by_default(self):
        self.assertEqual('Python Test'.split(), ['Python', 'Test'])

    def test_split_by_comma(self):
        test = 'open,high,low,close'.split(',')
        expected = ['open', 'high', 'low', 'close']
        self.assertEqual(test, expected)

    def test_split_by_hash(self):
        actual = 'summer#time#vibe'.split('#')
        expected = ['summer', 'time','vibe']
        self.assertEqual(actual, expected)


class TestJoinMethod(unittest.TestCase):
    def test_join_with_space(self):

        self.assertEqual(' '.join(['python','3.8']), 'python 3.8')

    def test_join_with_comma(self):
        self.assertEqual(','.join(['radhe','shyam']), 'radhe,shyam')


    def test_join_with_newline(self):
        self.assertEqual('\n'.join(['open','high','low','close']), 'open\nhigh\nlow\nclose')


class TestInstance(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(isinstance((), tuple))

    def test_case_2(self):
        self.assertTrue(isinstance([], list))

    def test_case_3(self):
        self.assertTrue(isinstance({}, dict))

    def test_case_4(self):
        var1 = 4
        self.assertTrue(isinstance(var1, int))

    def test_case_5(self):
        var2 = 4,
        self.assertTrue(isinstance(var2, tuple))

    def test_case_6(self):
        cnt = Counter()
        self.assertTrue(isinstance( cnt, Counter))


class TestUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('summer'.upper(), 'SUMMER')
    def test_is_upper(self):
        self.assertTrue('SUMMER'.isupper())
        self.assertFalse('summer'.isupper())

class TestStartWithMethod(unittest.TestCase):
    def test_startwith_one_latter(self):
        self.assertTrue('unittest'.startswith('u'))
        self.assertFalse('unittest'.startswith('U'))

    def test_start_with_4latter(self):
        self.assertTrue('http://thetechieman.com'.startswith('http'))
        self.assertFalse('www.thetechieman.com'.startswith('http'))

#TODO: same we can do for ends with

class TestLstripMethod(unittest.TestCase):
    def test_lstrip_with_space(self):
        self.assertEqual(' price,volume '.lstrip(), 'price,volume ')

    def test_lstrip_with_newline(self):
        self.assertEqual('\nprice,volume\n'.lstrip(), 'price,volume\n')
#TODO: write for strip and rstrip



"--------------------------------------------------------------------------"

class StringReverse:
    def reverse(self, string):
        return string[::-1]

class TestStringReverse(unittest.TestCase):
    def test_reverse(self):
        #creating new instace for stringreverse class
        reverser = StringReverse()

        #Test that 'hello' reverse is 'olleh'
        self.assertEqual(reverser.reverse('hello'), 'olleh')

        #Test that '12345' reverse is '54321'
        self.assertEqual(reverser.reverse('12345'), '54321')

        #Test that ""(empty string) reverse is ""
        self.assertEqual(reverser.reverse(""), "")


"--------------------------------------------------------------------------------"
class Rectangle:
    def __init__(self, width, height):
        self._validate_params(width, height)
        self.width = width
        self.height =  height

    def _validate_params(self, width, height):
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("width must be positive number")

        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("height must be positive number")


    def area(self):
        return self.width * self.height

class TestRectangle(unittest.TestCase):
    def test_area_with_non_zero_dim(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_area_with_zero_dim(self):
        rect = Rectangle(0, 0)
        self.assertEqual(rect.area(), 0)

    def test_area_with_negative_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_area_with_negative_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_area_with_float_dim(self):
        rect = Rectangle(3.5, 2.5)
        self.assertEqual(rect.area(), 8.75)


    def test_area_with_large_dim(self):
        rect = Rectangle(1000000, 1000000)
        self.assertEqual(rect.area(), 1000000000000)

'----------------------------------------------------------------------'

class TempratureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5)+32

class TestTempratureConverter(unittest.TestCase):
    def test_celsuis_to_farhenheit(self):
        c = TempratureConverter()
        self.assertAlmostEqual(c.celsius_to_fahrenheit(0), 32, delta=0.5)
        self.assertAlmostEqual(c.celsius_to_fahrenheit(100), 212, delta=0.5)
        self.assertAlmostEqual(c.celsius_to_fahrenheit(-40), -40, delta=0.5)





if __name__=='__main__':
    unittest.main()