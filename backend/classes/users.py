from pygments.lexer import default

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
    def __init__(self, firstname, surname, lastname, phone, paper_money ,role_id):
        self.firstname = firstname
        self.surname = surname
        self.lastname = lastname
        self.phone = phone
        self.role_id = role_id
        self.paper_money = paper_money
        self.role = Role.get_role_name(role_id)
        

    def user_permissioons(self):
        pass
        # if self.role == "Обычный_пользователь":