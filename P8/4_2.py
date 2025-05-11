import deal
import pytest

# Класс BankAccount с инвариантами
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    @deal.inv(lambda self: isinstance(self.balance, (int, float)))  # Баланс должен быть числом
    @deal.inv(lambda self: self.balance >= 0)  # Баланс не может быть отрицательным
    class _Invariant:
        pass

    @deal.pre(lambda self, amount: amount > 0)  # Сумма должна быть положительной
    @deal.post(lambda result: "успешно зачислены" in result)  # Проверка результата
    def deposit(self, amount):
        """Зачисление средств на счёт."""
        self.balance += amount
        return f"{amount:.2f} средств успешно зачислены на счёт."

    @deal.pre(lambda self, amount: amount > 0)  # Сумма должна быть положительной
    @deal.pre(lambda self, amount: self.balance >= amount)  # Достаточно средств для снятия
    @deal.post(lambda result: "успешно сняты" in result)  # Проверка результата
    def withdraw(self, amount):
        """Снятие средств со счёта."""
        self.balance -= amount
        return f"{amount:.2f} средств успешно сняты с счёта."

    @deal.ensure(lambda self, result: result == f"Баланс счёта: {self.balance:.2f}")  # Проверка результата
    def check_balance(self):
        """Проверка баланса."""
        return f"Баланс счёта: {self.balance:.2f}"


# Тесты для класса BankAccount
def test_initial_balance():
    """Проверка начального баланса."""
    account = BankAccount()
    assert account.check_balance() == "Баланс счёта: 0.00"


def test_deposit_positive_amount():
    """Проверка зачисления положительной суммы."""
    account = BankAccount()
    result = account.deposit(100)
    assert "успешно зачислены" in result
    assert account.check_balance() == "Баланс счёта: 100.00"


def test_withdraw_positive_amount():
    """Проверка снятия положительной суммы."""
    account = BankAccount(balance=100)
    result = account.withdraw(50)
    assert "успешно сняты" in result
    assert account.check_balance() == "Баланс счёта: 50.00"


def test_withdraw_insufficient_funds():
    """Проверка снятия суммы, превышающей баланс."""
    account = BankAccount(balance=50)
    with pytest.raises(deal.PreContractError):
        account.withdraw(100)


def test_deposit_negative_amount():
    """Проверка попытки зачисления отрицательной суммы."""
    account = BankAccount()
    with pytest.raises(deal.PreContractError):
        account.deposit(-50)


def test_withdraw_negative_amount():
    """Проверка попытки снятия отрицательной суммы."""
    account = BankAccount(balance=100)
    with pytest.raises(deal.PreContractError):
        account.withdraw(-50)


def test_balance_after_deposit_and_withdraw():
    """Проверка баланса после зачисления и снятия средств."""
    account = BankAccount()
    account.deposit(0.3)
    account.withdraw(0.1)
    assert account.check_balance() == "Баланс счёта: 0.20"


# Запуск тестов
if __name__ == "__main__":
    pytest.main()