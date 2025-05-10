from Atm.backend.classes.bank_class.Card_and_money import CardMoney, Money, Account


class Role:
    roles = {
        1: "Обычный_пользователь",
        2: "Инкассатор",
        3: "Работник_банка"
    }

    @classmethod
    def get_role_name(cls, role_id):
        return cls.roles.get(role_id, "Неизвестная_роль")


class BaseUser:
    def __init__(self, firstname, surname, lastname, phone, paper_money, role_id, card: CardMoney, wallet: list[Money] , account:Account ):
        if role_id not in Role.roles:
            raise ValueError(f"Неверный role_id: {role_id}. Допустимые значения: {list(Role.roles.keys())}")

        self.firstname = firstname
        self.surname = surname
        self.lastname = lastname
        self.phone = phone
        self.role_id = role_id
        self.paper_money = paper_money
        self.role = Role.get_role_name(role_id)

        self.card = card
        self.wallet = wallet
        self.account = account

    def __str__(self):
        return f"{self.firstname} {self.surname} ({self.role})"

    def user_permissions(self):
        pass  # позже добавим

    # Метод для проверки общей суммы средств (карт + наличные)
    def total_balance(self):
        return self.card.balance + sum(m.total_balance() for m in self.wallet)
