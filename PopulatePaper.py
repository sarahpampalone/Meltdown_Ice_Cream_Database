from Paper import *

def pop_paper(paper_inventory):
    #CREATES INSTANCES OF EACH ITEM
    SmallCups = Paper()
    MediumCups = Paper()
    LargeCups = Paper()
    SmallLids = Paper()
    MediumLids = Paper()
    LargeLids = Paper()
    SmallBoats = Paper()
    LargeBoats = Paper()
    Spoons = Paper()
    Napkins = Paper()
    MilkshakeCups = Paper()
    MilkshakeLids = Paper()
    Straws = Paper()

    #SETS ATTRIBUTE VALUES
    SmallCups.name = "Small Cups"
    SmallCups.details = "8oz"
    SmallCups.vendor = "Vendor2"
    SmallCups.standard_amount = 4
    SmallCups.price = 80

    MediumCups.name = "Medium Cups"
    MediumCups.details = "12oz"
    MediumCups.vendor = "Vendor2"
    MediumCups.standard_amount = 4
    MediumCups.price = 80

    LargeCups.name = "Large Cups"
    LargeCups.details = "16oz"
    LargeCups.vendor = "Vendor2"
    LargeCups.standard_amount = 4
    LargeCups.price = 80

    SmallLids.name = "Small Lids"
    SmallLids.vendor = "Vendor2"
    SmallLids.standard_amount = 4
    SmallLids.price = 50

    MediumLids.name = "Medium Lids"
    MediumLids.vendor = "Vendor2"
    MediumLids.standard_amount = 4
    MediumLids.price = 50

    LargeLids.name = "Large Lids"
    LargeLids.vendor = "Vendor2"
    LargeLids.standard_amount = 4
    LargeLids.price = 50

    SmallBoats.name = "Small Boats"
    SmallBoats.details = "16oz"
    SmallBoats.vendor = "Vendor2"
    SmallBoats.standard_amount = 3
    SmallBoats.price = 80

    LargeBoats.name = "Large Boats"
    LargeBoats.details = "16oz"
    LargeBoats.vendor = "Vendor2"
    LargeBoats.standard_amount = 3
    LargeBoats.price = 80

    Spoons.name = "Spoons"
    Spoons.vendor = "Vendor2"
    Spoons.standard_amount = 3
    Spoons.price = 40

    Napkins.name = "Napkins"
    Napkins.vendor = "Vendor2"
    Napkins.standard_amount = 5
    Napkins.price = 40

    MilkshakeCups.name ="Milkshake Cups"
    MilkshakeCups.details = "16oz"
    MilkshakeCups.vendor = "Vendor2"
    MilkshakeCups.standard_amount = 4
    MilkshakeCups.price = 60

    MilkshakeLids.name = "Milkshake Lids"
    MilkshakeLids.vendor = "Vendor2"
    MilkshakeLids.standard_amount = 4
    MilkshakeLids.price = 60

    Straws.name = "Straws"
    Straws.vendor = "Vendor2"
    Straws.standard_amount = 4
    Straws.standard_amount = 40

    #POPULATES ARRAY
    paper_inventory.append([
        SmallCups, MediumCups, LargeCups, SmallLids, MediumLids, LargeLids, SmallBoats, LargeBoats, Spoons, Napkins, MilkshakeCups, MilkshakeLids, Straws
    ])
