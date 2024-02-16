# GildedRose class is instantiate to call update_quality method that calls the indivity update_item_quality method with a for loop. Each item has its methods with logic to update the quality and sell_in date
class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras" and item.quality > 50:
                    item.quality = 50
            self.update_item_quality(item)

    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes":
            self.update_backstage_passes(item)
        elif item.name == "Sulfuras":
            item.quality = 80
        elif item.name == "Normal Item":
            self.update_normal_item(item)
        elif item.name == "Conjured":
            self.update_conjured(item)


    # Item quality increases by 1 every day regardless of sell in date and goes upto 50
    def update_aged_brie(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
    
    # Item quality increase by 1 every day, increase by 2 if sell in less than 10 and increase by 3 if sll in less than 5. quality drops to 0 if sellin is less than 0
    def update_backstage_passes(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        if item.sell_in > 0 and item.quality < 50:
            if item.sell_in < 5:
                item.quality += 3
            elif item.sell_in < 10:
                item.quality += 2
            else:
                item.quality += 1


    # Item quality degrades by 1 every day and this runs until item quality reaches zero
    def update_normal_item(self, item):
        if item.sell_in > 0 and item.quality < 50:
            item.sell_in -= 1
            if item.quality > 0:
                item.quality -= 1
            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 1
    
    # Item quality degrades by 2 every day and this runs until item quality reaches zero
    def update_conjured(self, item):
        if item.sell_in > 0 and item.quality <= 50:
            item.sell_in -= 1
            if item.quality > 0:
                item.quality -= 2
            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 2


# The Item class is instantiated first by the main method with items and its attributes name, sell_in and quality
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# This is the main method, we are creating instances of Item class and passing to item list
# Then we create GildedRose class intance with items list which has the update quality methods and in turn respective item methods are called and updated
if __name__ == "__main__":
    items = [
        Item("Aged Brie", 0, 51),
        Item("Backstage passes", 4, 20),
        Item("Sulfuras", 10, 80),
        Item("Normal Item", 5, 25),
        Item("Conjured", 3, 50)   
    ]

    gilded_rose = GildedRose(items)

    print("current Items:")
    for item in items:
        print(item)

    gilded_rose.update_quality()

    print("\ncurrent Items after one day:")
    for item in items:
        print(item)