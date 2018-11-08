from unittest import TestCase
from whenthen import WhenThen

class WhenThenTest(TestCase):
    def whenthen(func):
        return WhenThen(func)

    @whenthen
    def funny(x):
        x = x+2
        return x
        
    def test_base(self):
        self.assertEqual(5, self.funny(3))

    def test_main_functional(self):
        self.assertEqual(5, self.funny(3))
        self.assertEqual(6, self.funny(4))
        self.assertEqual(430, self.funny(428))
        @self.funny.when
        def funny(x):
            return x == 1

        @self.funny.then
        def funny(x):
            return 21

        @self.funny.when
        def funny(x):
            return x == 2

        @self.funny.then
        def funny(x):
            return 22

        self.assertEqual(6, self.funny(4))
        self.assertEqual(21, self.funny(1))
        self.assertEqual(5, self.funny(3))
        self.assertEqual(22, self.funny(2))
        
        @self.funny.when
        def funny(x):
            return x == 3

        @self.funny.then
        def funny(x):
            return 23

        self.assertEqual(23, self.funny(3))

    def test_then_errors(self):
        
        @self.funny.then
        def funny(x):
            return x == 1

        with self.assertRaises(ValueError):
            @self.funny.then
            def funny(x):
                return x == 2
        
    def test_when_errors(self):
        
        @self.funny.when
        def funny(x):
            return x == 1

        with self.assertRaises(ValueError):
            @self.funny.when
            def funny(x):
                return x == 2
