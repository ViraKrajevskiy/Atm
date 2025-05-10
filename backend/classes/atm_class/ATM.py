from Atm.backend.classes.bank_class.Card_and_money import CardMoney


class Atm:
    STATUS = {
        1: "Active",
        2: "Not Active"
    }

    def __init__(self, balance: int, card: CardMoney, status_id: int = 1):
        if status_id not in self.STATUS:
            raise ValueError(f"Неверный статус: {status_id}. Допустимые: {list(self.STATUS.keys())}")

        self.balance = balance
        self.card = card  # Экземпляр CardMoney — обязательно
        self.status_id = status_id
        self.status = self.STATUS[status_id]

    def __str__(self):
        return (f"Банкомат (Статус: {self.status}, Баланс: {self.balance} сум, "
                f"Карта: {self.card.card_name} #{self.card.card_number})")

    def activate(self):
        self.status_id = 1
        self.status = self.STATUS[1]

    def deactivate(self):
        self.status_id = 2
        self.status = self.STATUS[2]

    def deposit_cash(self, amount: int):
        if self.status_id != 1:
            raise Exception("Банкомат неактивен")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount

    def withdraw_cash(self, amount: int):
        if self.status_id != 1:
            raise Exception("Банкомат неактивен")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.balance:
            raise Exception("Недостаточно средств в банкомате")
        self.balance -= amount
        return amount
