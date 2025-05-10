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

class CardMoney:
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


class Account:
    _id_counter = count(1)

    def __init__(self, user, card: CardMoney, wallet: list[Money]):
        if user.role_id != 1:
            raise ValueError("Только обычный пользователь может иметь Account")
        self.account_id = next(Account._id_counter)
        self.user = user  # экземпляр BaseUser
        self.card = card  # экземпляр CardMoney
        self.wallet = wallet  # список экземпляров Money

    def total_cash(self):
        return sum(m.total_balance() for m in self.wallet)

    def __str__(self):
        return (f"Аккаунт #{self.account_id} — {self.user.firstname} {self.user.surname} ({self.user.role})\n"
                f"Баланс карты: {self.card.balance} сум\n"
                f"Наличные: {self.total_cash()} сум")

