from IceCreamFlavor import *


def pop_ice_cream(ice_cream_inventory):
    PartyCake = IceCreamFlavor()
    ChocolateChipCookie = IceCreamFlavor()
    CookiesAndCream = IceCreamFlavor()
    CottonCandy = IceCreamFlavor()
    ChocolatePeanutButter = IceCreamFlavor()
    BlackRaspberry = IceCreamFlavor()
    ButterPecan = IceCreamFlavor()
    CookieDough = IceCreamFlavor()
    Mint = IceCreamFlavor()
    Coffee = IceCreamFlavor()
    Mochachino = IceCreamFlavor()
    Pistachio = IceCreamFlavor()
    Nutterbutter = IceCreamFlavor()
    Moosetracks = IceCreamFlavor()
    VanillaPeanutButter = IceCreamFlavor()
    Banana = IceCreamFlavor()
    BlueberryPie = IceCreamFlavor()
    RumRaisin = IceCreamFlavor()
    RainbowSherbet = IceCreamFlavor()
    CherryVanilla = IceCreamFlavor()
    VanillaChip = IceCreamFlavor()
    SweetAndSalty = IceCreamFlavor()
    ToastedCoconut = IceCreamFlavor()
    Chocolate = IceCreamFlavor()
    Vanilla = IceCreamFlavor()
    Strawberry = IceCreamFlavor()
    RockyRoad = IceCreamFlavor()
    JerseyShore = IceCreamFlavor()
    MidnightJerseyShore = IceCreamFlavor()
    ChocSoftServe = IceCreamFlavor()
    VanSoftServe = IceCreamFlavor()
    PineappleDole = IceCreamFlavor()
    StrawberryDole = IceCreamFlavor()

    Banana.name="Banana"
    Banana.description="Classic!"
    Banana.vendor="Vendor1"
    Banana.standard_amount=2
    Banana.price=60
    
    BlackRaspberry.name = "Black Raspberry"
    BlackRaspberry.description = "Fresh and seasonal berries"
    BlackRaspberry.vendor = "Vendor1"
    BlackRaspberry.standard_amount = 2
    BlackRaspberry.price = 60

    BlueberryPie.name="Blueberry Pie"
    BlueberryPie.description="Sweet cream ice cream with a granola swirl and crushed blueberries"
    BlueberryPie.vendor="Vendor1"
    BlueberryPie.standard_amount=2
    BlueberryPie.price=65
    BlueberryPie.wheat=True
    BlueberryPie.soy=True
    
    ButterPecan.name = "Butter Pecan"
    ButterPecan.description = "Classic"
    ButterPecan.vendor = "Vendor1" 
    ButterPecan.standard_amount = 2
    ButterPecan.price = 60
    ButterPecan.set_tree_nuts = True

    CherryVanilla.name="Cherry Vanilla"
    CherryVanilla.description="Cherry-infused vanilla base with crushed cherries"
    CherryVanilla.vendor="Vendor1"
    CherryVanilla.standard_amount=2
    CherryVanilla.price=60

    Chocolate.name="Chocolate"
    Chocolate.description="Classic!"
    Chocolate.vendor="Vendor1"
    Chocolate.standard_amount=6
    Chocolate.price=55

    ChocolateChipCookie.name = "Chocolate Chip Cookie"
    ChocolateChipCookie.description = "Brown sugar ice cream with chocolate chips"
    ChocolateChipCookie.vendor = "Vendor1"
    ChocolateChipCookie.standard_amount = 4
    ChocolateChipCookie.price = 65
    ChocolateChipCookie.soy = True

    ChocolatePeanutButter.name = "Chocolate Peanut Butter"
    ChocolatePeanutButter.description = "Rich chocolate base with a hard peanut butter swirl"
    ChocolatePeanutButter.vendor = "Vendor1"
    ChocolatePeanutButter.standard_amount = 4
    ChocolatePeanutButter.price = 60
    ChocolatePeanutButter.peanut = True

    Coffee.name = "Coffee"
    Coffee.description = "Classic! (contains caffeine)"
    Coffee.vendor = "Vendor1"
    Coffee.standard_amount = 4
    Coffee.price = 60

    CookieDough.name = "Cookie Dough"
    CookieDough.description = "Sweet cream ice cream  with mini cookie dough chunks"
    CookieDough.vendor = "Vendor1"
    CookieDough.standard_amount = 4
    CookieDough.price = 65
    CookieDough.setwheat = True
    CookieDough.setSoy = True

    CookiesAndCream.name = "Cookies and Cream"
    CookiesAndCream.description = "Sweet cream ice cream with crushed oreo pieces"
    CookiesAndCream.vendor = "Vendor1"
    CookiesAndCream.standard_amount = 6
    CookiesAndCream.price = 60
    CookiesAndCream.wheat = True
    CookiesAndCream.soy = True

    CottonCandy.name = "Cotton Candy"
    CottonCandy.description = "Just like the carnival!"
    CottonCandy.vendor = "Vendor3"
    CottonCandy.standard_amount = 2
    CottonCandy.price = 60
    CottonCandy.soy = True

    JerseyShore.name="Jersey Shore"
    JerseyShore.description="Vanilla ice cream with a salted caramel swirl"
    JerseyShore.vendor="Vendor1"
    JerseyShore.standard_amount=4
    JerseyShore.price=65

    MidnightJerseyShore.name="Midnight Jersey Shore"
    MidnightJerseyShore.description="Chocolate ice cream with a salted caramel swirl and brownie bits"
    MidnightJerseyShore.vendor="Vendor1"
    MidnightJerseyShore.standard_amount=4
    MidnightJerseyShore.price=65

    Mint.name = "Mint Chocolate Chip"
    Mint.description = "Green mint ice cream with mini chocolate chips"
    Mint.vendor = "Vendor1"
    Mint.standard_amount = 6
    Mint.price = 60
    
    Mochachino.name = "Mochachino"
    Mochachino.description = "Coffee and rich chocolate swirled"
    Mochachino.vendor = "Vendor1"
    Mochachino.standard_amount = 2
    Mochachino.price = 60

    Moosetracks.name="Moosetracks"
    Moosetracks.description = "Vanilla ice cream with a fudge swirl and mini peanut butter cups"
    Moosetracks.vendor="Vendor1"
    Moosetracks.standard_amount=2
    Moosetracks.price=65
    Moosetracks.peanuts=True
    Moosetracks.soy=True

    Nutterbutter.name = "Nutterbutter"
    Nutterbutter.description="Peanut butter ice cream with wafer bits"
    Nutterbutter.vendor="Vendor1"
    Nutterbutter.standard_amount=2
    Nutterbutter.price=65
    Nutterbutter.peanut=True
    Nutterbutter.wheat=True

    PartyCake.name = "Party Cake"
    PartyCake.description = "Birthday cake ice cream"
    PartyCake.vendor = "Vendor1"
    PartyCake.standard_amount = 2
    PartyCake.price = 60
    PartyCake.wheat = True
    PartyCake.soy = True

    Pistachio.name = "Pistachio"
    Pistachio.description = "Classic! (Pistachio Almondine)"
    Pistachio.vendor = "Vendor1"
    Pistachio.standard_amount = 2
    Pistachio.price = 60
    Pistachio.set_tree_nuts =True

    RainbowSherbet.name="Rainbow Sherbet"
    RainbowSherbet.description="Raspberry, Orange, and Lime swirled"
    RainbowSherbet.vendor="Vendor1"
    RainbowSherbet.standard_amount=4
    RainbowSherbet.price=65

    RockyRoad.name="Rocky Road"
    RockyRoad.description="Chocolate ice cream with a marshmallow swirl and chopped nuts"
    RockyRoad.vendor="Vendor1"
    RockyRoad.standard_amount=2
    RockyRoad.price=65
    RockyRoad.peanut=True
    RockyRoad.soy=True

    RumRaisin.name="Rum Raisin"
    RumRaisin.description="Rum infused base with raisins!"
    RumRaisin.vendor="Vendor1"
    RumRaisin.standard_amount=2
    RumRaisin.price=60

    Strawberry.name="Strawberry"
    Strawberry.description="Classic!"
    Strawberry.vendor="Vendor1"
    Strawberry.standard_amount=4
    Strawberry.price=55

    SweetAndSalty.name="Sweet and Salty"
    SweetAndSalty.description="Vanilla ice cream with a salted caramel swirl and pretzel pieces"
    SweetAndSalty.standard_amount=4
    SweetAndSalty.price=65
    SweetAndSalty.wheat=True
    SweetAndSalty.soy=True

    ToastedCoconut.name="Toasted Coconut"
    ToastedCoconut.description="Coconut ice cream with chocolate covered coconut flakes"
    ToastedCoconut.vendor="Vendor1"
    ToastedCoconut.standard_amount=4
    ToastedCoconut.price=65
    ToastedCoconut.set_tree_nuts=True

    Vanilla.name="Vanilla"
    Vanilla.description="Classic!"
    Vanilla.vendor="Vendor1"
    Vanilla.standard_amount=6
    Vanilla.price=55

    VanillaPeanutButter.name="Vanilla Peanut Butter"
    VanillaPeanutButter.description="Vanilla ice cream with a hard peanut butter swirl"
    VanillaPeanutButter.vendor="Vendor1"
    VanillaPeanutButter.standard_amount=4
    VanillaPeanutButter.price=60
    VanillaPeanutButter.peanut=True

    VanillaChip.name="Vanilla Chip"
    VanillaChip.description="Vanilla ice cream with mini chocolate chips"
    VanillaChip.vendor="Vendor1"
    VanillaChip.standard_amount=2
    VanillaChip.price=60

    ChocSoftServe.name="Chocolate Soft Serve"
    ChocSoftServe.description="Classic!"
    ChocSoftServe.vendor="Vendor4"
    ChocSoftServe.standard_amount=20
    ChocSoftServe.price=60

    VanSoftServe.name="Vanilla Soft Serve"
    VanSoftServe.description="Classic!"
    VanSoftServe.vendor="Vendor4"
    VanSoftServe.standard_amount=24
    VanSoftServe.price=60

    PineappleDole.name="Pineapple Dole Whip"
    PineappleDole.description="Vegan soft serve alternative"
    PineappleDole.vendor="Vendor4"
    PineappleDole.standard_amount=4
    PineappleDole.price=90

    StrawberryDole.name="Strawberry Dole Whip"
    StrawberryDole.description="Vegan soft serve alternative"
    StrawberryDole.vendor="Vendor4"
    StrawberryDole.standard_amount=4
    StrawberryDole.price=90

    ice_cream_inventory.append([Banana, BlackRaspberry, BlueberryPie, ButterPecan, Chocolate, ChocolateChipCookie, 
                                ChocolatePeanutButter, Coffee, CookieDough, CookiesAndCream, CottonCandy, CherryVanilla, 
                                Chocolate, JerseyShore, MidnightJerseyShore, Mint, Mochachino, Moosetracks, Nutterbutter, 
                                PartyCake, Pistachio, RainbowSherbet, RockyRoad, RumRaisin, Strawberry, SweetAndSalty, 
                                ToastedCoconut, Vanilla, VanillaChip, VanillaPeanutButter, ChocSoftServe, VanSoftServe,
                                PineappleDole, StrawberryDole])