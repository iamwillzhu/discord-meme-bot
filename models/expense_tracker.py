from dataclasses import dataclass
from models.user import User
from typing import List


@dataclass
class ExpenseTracker:
    users: List[User]

    def pay_user(self, caller: str, receiver: str, amount: int) -> None:
        caller_user = None
        receiver_user = None
        for user in self.users:
            if user.name == caller:
                caller_user = user
            elif user.name == receiver:
                receiver_user = user

        if caller_user is not None and receiver_user is not None:
            caller_user.expenses[receiver] -= amount
            receiver_user.expenses[caller] += amount

    def request_user(self, caller: str, receiver: str, amount: int):
        caller_user = None
        receiver_user = None
        for user in self.users:
            if user.name == caller:
                caller_user = user
            elif user.name == receiver:
                receiver_user = user

        if caller_user is not None and receiver_user is not None:
            caller_user.expenses[receiver] += amount
            receiver_user.expenses[caller] -= amount
