from typing import Final
from unittest import TestCase

from constant_class import Constant, MixedConstant, StrConstant
from constant_class.meta_class import MetaConstant


class Foo(Constant):
    BAR: Final = 'bar1'
    ABA: Final = 'ABA2'


class Bar(MixedConstant):
    TOR: Final = 'tor1'
    bla: Final = 2


class ConstantUnitTests(TestCase):
    def test_attribute_change(self):
        with self.assertRaises(AttributeError):
            Foo.BAR = 'bla'
            Bar.TOR = 'foo'

    def test_attribute_delete(self):
        with self.assertRaises(AttributeError):
            del Foo.BAR
            del Bar.TOR

    def test_repr_constant(self):
        self.assertEqual(str(Foo), 'Foo(BAR=bar1, ABA=ABA2)')
        self.assertEqual(str(Bar), 'Bar(TOR=tor1, bla=2)')

    def test_items(self):
        self.assertEqual(Foo.items, [('BAR', 'bar1'), ('ABA', 'ABA2')])
        self.assertEqual(Bar.items, [('TOR', 'tor1'), ('bla', 2)])

    def test_values(self):
        self.assertEqual(Foo.values, ['bar1', 'ABA2'])
        self.assertEqual(Bar.values, ['tor1', 2])

    def test_keys(self):
        self.assertEqual(Foo.keys, ['BAR', 'ABA'])
        self.assertEqual(Bar.keys, ['TOR', 'bla'])

    def test_to_dict(self):
        self.assertEqual(Foo.to_dict, {'BAR': 'bar1', 'ABA': 'ABA2'})
        self.assertEqual(Bar.to_dict, {'TOR': 'tor1', 'bla': 2})

    def test_get(self):
        self.assertEqual(Foo.get('BAR'), 'bar1')
        self.assertEqual(Bar.get('TOR'), 'tor1')

    def test_has_key(self):
        self.assertTrue(Foo.has_key('BAR'))  # noqa
        self.assertTrue(Bar.has_key('TOR'))  # noqa

    def test_has_value(self):
        self.assertTrue(Foo.has_value('bar1'))
        self.assertTrue(Bar.has_value('tor1'))

    def test_len(self):
        self.assertEqual(len(Foo), 2)
        self.assertEqual(len(Bar), 2)

    def test_contains(self):
        self.assertIn('BAR', Foo)
        self.assertIn('TOR', Bar)

    def test_getitem(self):
        self.assertEqual(Foo['BAR'], 'bar1')
        self.assertEqual(Bar['TOR'], 'tor1')

    def test_iter(self):
        self.assertListEqual([c for c in Foo], ['BAR', 'ABA'])
        self.assertListEqual([c for c in Bar], ['TOR', 'bla'])

    def test_no_members(self):
        with self.assertRaises(AssertionError):
            class Cat(Constant):
                pass

            class Dog(MixedConstant):
                pass

    def test_bad_name(self):
        with self.assertRaises(AssertionError):
            class Cat(Constant):
                BAR = 'bar1'
                mama = 'ma'

        class Dog(MixedConstant):
            OOF: Final = 'foo'
            bla: Final = 'bla2'

    def test_sub_classing_from_meta_constant(self):
        with self.assertRaises(TypeError):
            class Bla(MetaConstant):
                pass

    def test_no_final_in_constant(self):
        with self.assertRaises(AssertionError):
            class Dog(Constant):
                OOF = 'foo'
                BLA: Final = 'bla2'

    def test_no_final_in_constant_when_allowed(self):
        class Dog(MixedConstant):
            OOF = 'foo'
            BLA: Final = 'bla2'

    def test_bad_type_in_constant(self):
        with self.assertRaises(AssertionError):
            class Dog(StrConstant):
                OOF: Final = 'foo'
                BAR: Final = 55

    def test_immutable_type_in_constant(self):
        with self.assertRaises(AssertionError):
            class Dog(Constant):
                OOF: Final = [1, 2, 3]
                BAR: Final = 55

    def test_immutable_type_in_constant_when_allowed(self):
        class Dog(MixedConstant):
            OOF: Final = [1, 2, 3]
            BAR: Final = 55
