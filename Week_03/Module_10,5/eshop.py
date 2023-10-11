class EShop:
    def __init__(self, shop_name, road, house_no, zip_code, city, state, country, tin):
        self.shop_name = shop_name
        self.road = road
        self.house_no = house_no
        self.zip_code = zip_code
        self.city = city
        self.state = state
        self.country = country
        self.tin = tin

    products = []
    customers = []      # List of Dictionaries
    sellers = []        # List of Dictionaries

    def shop_info(self):
        print(f'----- Company Information -----\n{self.shop_name}\n{self.road} {self.house_no}\n{self.zip_code} {self.city}\n{self.state} {self.country}\nTIN: {self.tin}')
