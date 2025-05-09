from itertools import count

class MoneyNominal:
    Money_nominal = {
        1000:"1000 сум",
        2000:"2000 сум",
        5000:"5000 сум",
        10000:"10000 сум",
        20000:"20000 сум",
        50000:"50000 сум",
        100000:"100000 сум",
        200000:"200000 сум"
    }

    @classmethod
    def get_money_nominal(cls,money_nomi):
        return cls.Money_nominal.get(money_nomi,"Неизвестный_номинал")

class CardAndMoney:
    def __init__(self,card_id , card_name, card_number, card_work_time, password, balance, card_type, phone_number):
        self.card_id = card_id
        self.card_name = card_name
        self.card_number = card_number
        self.card_work_time = card_work_time
        self.password = password
        self.balance = balance
        self.card_type = card_type
        self.phone_number = phone_number

class Money:
    def __init__(self, user_money_balance, money_nomi, count):
        self.user_money_balance = user_money_balance
        self.money_nomi = money_nomi
        self.count = count
        self.money = MoneyNominal.get_money_nominal(money_nomi)

    def total_balance(self):
        return self.money_nomi * self.count

    def __str__(self):
        return f"{self.count} x {self.money} = {self.total_balance()} сум"