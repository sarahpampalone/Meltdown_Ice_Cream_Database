class Topping:
    def __init__(self):
        # BASE
        self.name = ""
        self.temp = ""
        self.vendor = ""
        self.in_stock = True

        # PRICING AND ORDERING
        self.standard_amount = 0
        self.price = 0
        self.current = 0
        self.old = 0

        # ALLERGENS
        self.peanut = False
        self.milk = False
        self.treenut = False
        self.wheat = False
        self.soy = False