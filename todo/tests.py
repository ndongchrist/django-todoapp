from django.test import TestCase

# Write a test that will fail no matter what
class FailingTest(TestCase):
    def test_fail(self):
        self.assertEqual(1, 1, "This test is designed to fail")