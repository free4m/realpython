import unittest


def hello(name):
    if name == 'Maria':
        return f'Yo, {name}'
    return f'Hello, {name}!'


class TestExample(unittest.TestCase):

    def test_hello_return_value(self):
        result = hello('Aleah')
        self.assertIsInstance(result, str)

    def test_hello_with_maria(self):
        result = hello('Tom')
        self.assertTrue(result.startswith('Yo'))
