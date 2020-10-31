class View:

    @staticmethod
    def display_pay_user(caller: str, receiver: str, amount: int):
        # TODO: return in a discord embed format
        return f"{caller} paid {receiver} {amount} dollars"

    @staticmethod
    def display_request_user(caller: str, receiver: str, amount: int):
        return f"{caller} requests {amount} dollars from {receiver}"
