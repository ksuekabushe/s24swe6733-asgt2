import unittest
from refactored_gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
        # Test aged brie that date decrease by 1 and quality Increases by 1
        def test_aged_brie(self):
            item = Item ("Aged Brie", 10, 20)
            gilded_rose = GildedRose([item])

            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, 9)
            self.assertEquals(item.quality, 21)

            item = Item ("Aged Brie", 0, 51)
            gilded_rose = GildedRose([item])

            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, -1)
            self.assertEquals(item.quality, 50)

        
        # Test backstage passes without any change
        def test_backstage_passes(self):
            item = Item("Backstage passes", 20, 20)
            gilded_rose = GildedRose([item])

            # Test quality increase by 1 after one day
            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, 19)
            self.assertEqual(item.quality, 21)


            # Quality increases by 2 when there are 10 days or less
            item = Item("Backstage passes", 9, 20)
            gilded_rose = GildedRose([item])
            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, 8)
            self.assertEqual(item.quality, 22)


            # Quality increases by 3 when there are 5 days or less
            item = Item("Backstage passes", 4, 20)
            gilded_rose = GildedRose([item])
            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, 3)
            self.assertEqual(item.quality, 23)

        # Test sulfuras that nothing changes
        def test_sulfuras(self):
            item = Item("Sulfuras", 0, 80)
            gilded_rose = GildedRose([item])
            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, 0)
            self.assertEqual(item.quality, 80)
        
        # item quality reduces by 1 eash day
        def test_normal_item(self):
            item = Item("Normal Item", 10, 20)
            gilded_rose = GildedRose([item])
            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, 9)
            self.assertEqual(item.quality, 19)
        
        # Its quality reduces by 2 each day
        def test_conjured(self):
            item = Item("Conjured", 20, 50)
            gilded_rose = GildedRose([item])
            gilded_rose.update_quality()
            self.assertEqual(item.sell_in, 19)
            self.assertEqual(item.quality, 48)


if __name__ == '__main__':
    unittest.main()