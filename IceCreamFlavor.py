class IceCreamFlavor:
    def __init__(self):
        # BASE
        self.name = ""
        self.description = ""
        self.vendor = ""
        self.in_stock = False

        # PRICING AND ORDERING
        self.standard_amount = 0
        self.price = 0

        # ALLERGIES
        self.peanut = False
        self.milk = True
        self.treenut = False
        self.wheat = False
        self.soy = False
