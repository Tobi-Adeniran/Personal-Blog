from django.test import TestCase

# Create your tests here.

#check if all numbers between 0 and 5 are even
class check_even_number_test(TestCase):
    def test_even(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

