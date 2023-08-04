class VendingMachine:
    def __init__(
        self,
        cokeCount,
        pepsiCount,
        sodaCount,
        pennyCount,
        nickelCount,
        dimeCount,
        quarterCount,
    ) -> None:
        self.product = {}
        self.coin = {}
        self.money = []
        self.product["coke"] = [cokeCount, 25]
        self.product["pepsi"] = [pepsiCount, 35]
        self.product["soda"] = [sodaCount, 45]
        self.coin["penny"] = pennyCount
        self.coin["nickel"] = nickelCount
        self.coin["dime"] = dimeCount
        self.coin["quarter"] = quarterCount
        cur_product = self.get_product()
        balance = self.get_money(cur_product)
        x = ''
        while x not in ['Y',"N"]:
            x = input(" Do you wanna countinue the process [y or N]: ")
        if x == 'Y':
            print(f"Balance: {balance} and Product: {cur_product}")
        else:
            print(f"""
                  Process Canceled Here is Money: {self.money} 
                  and no {cur_product} for you""")            

    def get_product(self):
        ask = True
        while ask:
            x = input("Enter the Product: [Coke] [Pepsi] [Soda] ")
            if x in self.product.keys():
                ask = False
        return x

    def get_money(self, Product):
        price = self.product.get(Product)[1]
        while price > sum(self.money):
            x = int(input("Enter money:"))
            self.money.append(x)

        self.total = sum(self.money)
        balance = self.total - price
        if self.total >= price:
            balance_ = []
            print(
                f"""Price : {price} 
                    Product : {Product}  
                    MoneyEntered : {self.total}  
                    Balance : {balance}"""
            )
            while balance != 0:
                if balance >= 10:
                    balance_.append(10)
                    self.coin["dime"] -= 1
                    balance -= 10
                if balance >= 5:
                    balance_.append(5)
                    self.coin["nickel"] -= 1
                    balance -= 5
                if balance >= 1:
                    balance_.append(1)
                    self.coin["penny"] -= 1
                    balance -= 1
            return balance_
        else:
            print(
                f"""Price : {price} \n 
                    Product : {Product} \n 
                    MoneyEntered : {self.total} \n 
                    Extra need : {balance}"""
            )
            return self.money


VendingMachine(10, 10, 10, 10, 10, 10, 10)
