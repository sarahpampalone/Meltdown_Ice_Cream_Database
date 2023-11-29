from Topping import *


def pop_topping(topping_inventory):
    RainbowSprinkles = Topping()
    ChocolateSprinkles = Topping()
    HotFudge = Topping()
    Caramel = Topping()
    PeanutButter = Topping()
    Marshmallow = Topping()
    ChocolateSyrup = Topping()
    VanillaSyrup = Topping()
    CherrySyrup = Topping()
    CoffeeSyrup = Topping()
    Strawberries = Topping()
    Pineapple = Topping()
    CookieDoughPieces = Topping()
    MMs = Topping()
    ReecesPieces = Topping()
    GummyBears = Topping()
    Oreos = Topping()
    Heath = Topping()
    ChocChips = Topping()
    Cherries = Topping()
    WhippedCream = Topping()
    PBCups = Topping()
    SugarCone = Topping()
    WaferCone = Topping()
    WaffleCone = Topping()
    Malt = Topping()

    RainbowSprinkles.name = "Rainbow Sprinkles"
    RainbowSprinkles.temp = "Room"
    RainbowSprinkles.vendor = "Vendor4"
    RainbowSprinkles.standard_amount = 4
    RainbowSprinkles.price = 60 / 4
    RainbowSprinkles.wheat = True
    RainbowSprinkles.soy = True

    ChocolateSprinkles.name = "Chocolate Sprinkles"
    ChocolateSprinkles.temp = "Room"
    ChocolateSprinkles.vendor = "Vendor4"
    ChocolateSprinkles.standard_amount = 4
    ChocolateSprinkles.price = 60/4
    ChocolateSprinkles.wheat = True
    ChocolateSprinkles.soy = True

    Caramel.name = "Caramel"
    Caramel.temp = "Room"
    Caramel.vendor = "Vendor4"
    Caramel.standard_amount = 2
    Caramel.price = 22

    Cherries.name = "Cherries"
    Cherries.temp = "Fridge"
    Cherries.vendor = "Vendor4"
    Cherries.standard_amount = 2
    Cherries.price = 68/4

    CherrySyrup.name = "Cherry Syrup"
    CherrySyrup.temp = "Room"
    CherrySyrup.vendor = "Vendor4"
    CherrySyrup.standard_amount = 1
    CherrySyrup.price = 20

    ChocChips.name = "Chocolate Chips"
    ChocChips.temp = "Fridge"
    ChocChips.vendor = "Vendor4"
    ChocChips.standard_amount = 1
    ChocChips.price = 80
    ChocChips.milk = True

    ChocolateSyrup.name = "Chocolate Syrup"
    ChocolateSyrup.temp = "Room"
    ChocolateSyrup.vendor = "Vendor4"
    ChocolateSyrup.standard_amount = 3
    ChocolateSyrup.price = 60/4
    ChocolateSyrup.milk = True

    CoffeeSyrup.name = "Coffee Syrup"
    CoffeeSyrup.temp = "Room"
    CoffeeSyrup.vendor = "Vendor4"
    CoffeeSyrup.standard_amount = 1
    CoffeeSyrup.price = 20

    CookieDoughPieces.name = "Cookie Dough Pieces"
    CookieDoughPieces.temp = "Fridge"
    CookieDoughPieces.vendor = "Vendor4"
    CookieDoughPieces.standard_amount = 2
    CookieDoughPieces.price = 35
    CookieDoughPieces.wheat = True
    CookieDoughPieces.soy = True

    GummyBears.name = "Gummy Bears"
    GummyBears.temp = "Room"
    GummyBears.vendor = "Vendor4"
    GummyBears.standard_amount = 1
    GummyBears.price = 72/4
    GummyBears.soy = True

    Heath.name = "Heath"
    Heath.temp = "Fridge"
    Heath.vendor = "Vendor4"
    Heath.standard_amount = 1
    Heath.price = 26
    Heath.milk = True
    Heath.wheat = True

    HotFudge.name = "Hot Fudge"
    HotFudge.temp = "Hot"
    HotFudge.vendor = "Vendor4"
    HotFudge.standard_amount = 4
    HotFudge.price = 18
    HotFudge.milk = True

    Malt.name = "Malt Powder"
    Malt.temp = "Room"
    Malt.vendor = "Vendor4"
    Malt.standard_amount = 1
    Malt.price = 15

    Marshmallow.name = "Marshmallow"
    Marshmallow.temp = "Room"
    Marshmallow.vendor = "Vendor4"
    Marshmallow.standard_amount = 2
    Marshmallow.price = 12
    Marshmallow.soy = True
    
    MMs.name = "M&Ms"
    MMs.temp = "Room"
    MMs.vendor = "Vendor4"
    MMs.standard_amount = 2
    MMs.price = 32
    MMs.milk = True

    Oreos.name = "Oreos"
    Oreos.temp = "Room"
    Oreos.vendor = "Vendor4"
    Oreos.standard_amount = 2
    Oreos.price = 56/4
    Oreos.wheat = True
    Oreos.soy = True

    PeanutButter.name = "Peanut Butter"
    PeanutButter.temp = "Room"
    PeanutButter.vendor = "Vendor4"
    PeanutButter.standard_amount = 2
    PeanutButter.price = 16
    PeanutButter.peanut = True

    PBCups.name = "Peanut Butter Cups"
    PBCups.temp = "Fridge"
    PBCups.vendor = "Vendor4"
    PBCups.standard_amount = 2
    PBCups.price = 28
    PBCups.peanut = True
    PBCups.milk = True

    Pineapple.name = "Pineapple"
    Pineapple.temp = "Fridge"
    Pineapple.vendor = "Vendor4"
    Pineapple.standard_amount = 1
    Pineapple.price = 66/6

    ReecesPieces.name = "Reece's Pieces"
    ReecesPieces.temp = "Room"
    ReecesPieces.vendor = "Vendor4"
    ReecesPieces.standard_amount = 2
    ReecesPieces.price = 30
    ReecesPieces.peanut = True
    ReecesPieces.milk = True

    Strawberries.name = "Strawberries"
    Strawberries.temp = "Fridge"
    Strawberries.vendor = "Vendor4"
    Strawberries.standard_amount = 1
    Strawberries.price = 15

    VanillaSyrup.name = "Vanilla Syrup"
    VanillaSyrup.temp = "Room"
    VanillaSyrup.vendor = "Vendor4"
    VanillaSyrup.standard_amount = 1
    VanillaSyrup.price = 52/4
    
    WhippedCream.name = "Whipped Cream"
    WhippedCream.temp = "Fridge"
    WhippedCream.vendor = "Vendor4"
    WhippedCream.standard_amount = 6
    WhippedCream.price = 55
    WhippedCream.milk = True

    SugarCone.name = "Sugar Cone"
    SugarCone.temp = "Room"
    SugarCone.vendor = "Vendor2"
    SugarCone.standard_amount = 2
    SugarCone.price = 82
    SugarCone.wheat = True

    WaferCone.name = "Wafer Cone"
    WaferCone.temp = "Room"
    WaferCone.vendor = "Vendor2"
    WaferCone.standard_amount = 3
    WaferCone.price = 72
    WaferCone.wheat = True

    WaffleCone.name = "Waffle Cone"
    WaffleCone.temp = "Room"
    WaffleCone.vendor = "Vendor2"
    WaffleCone.standard_amount = 2
    WaffleCone.price = 56
    WaffleCone.wheat = True

    topping_inventory.append([
        RainbowSprinkles, ChocolateSprinkles, Caramel, Cherries, CherrySyrup, ChocChips, ChocolateSyrup,
        CoffeeSyrup, CookieDoughPieces, GummyBears, Heath, HotFudge, MMs, Malt, Marshmallow, Oreos, PBCups, 
        PeanutButter, Pineapple, ReecesPieces, Strawberries, VanillaSyrup, WhippedCream, SugarCone, WaffleCone, WaferCone
    ])