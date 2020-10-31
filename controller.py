from dataclasses import dataclass
from models.expense_tracker import ExpenseTracker
from view import View


@dataclass
class Controller:
    model: ExpenseTracker
    view: View

    def pay_user(self, caller: str, receiver: str, amount: int):
        self.model.pay_user(caller=caller, receiver=receiver, amount=amount)
        return self.view.display_pay_user(
            caller=caller, receiver=receiver, amount=amount)

    def request_user(self, caller: str, receiver: str, amount: int):
        self.model.request_user(
            caller=caller, receiver=receiver, amount=amount)
        return self.view.display_request_user(
            caller=caller, receiver=receiver, amount=amount)
