# === Исходный код (project.py) ===
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount

    def check_balance(self):
        return self.balance


# === Тесты (tests/test_project.py) ===
import pytest

def test_initial_balance():
    """Проверка начального баланса."""
    account = BankAccount()
    assert account.check_balance() == 0


def test_deposit_positive_amount():
    """Проверка зачисления положительной суммы."""
    account = BankAccount()
    account.deposit(100)
    assert account.check_balance() == 100


def test_withdraw_positive_amount():
    """Проверка снятия положительной суммы."""
    account = BankAccount(balance=100)
    account.withdraw(50)
    assert account.check_balance() == 50


def test_withdraw_insufficient_funds():
    """Проверка снятия суммы, превышающей баланс."""
    account = BankAccount(balance=50)
    with pytest.raises(ValueError, match="Недостаточно средств на счете."):
        account.withdraw(100)


def test_deposit_negative_amount():
    """Проверка попытки зачисления отрицательной суммы."""
    account = BankAccount()
    with pytest.raises(ValueError, match="Сумма должна быть положительной."):
        account.deposit(-50)


def test_withdraw_negative_amount():
    """Проверка попытки снятия отрицательной суммы."""
    account = BankAccount(balance=100)
    with pytest.raises(ValueError, match="Сумма должна быть положительной."):
        account.withdraw(-50)


def test_deposit_correctly_increases_balance():
    """Проверка, что депозит корректно увеличивает баланс."""
    account = BankAccount(balance=50)
    account.deposit(50)
    assert account.check_balance() == 100


def test_withdraw_correctly_decreases_balance():
    """Проверка, что снятие корректно уменьшает баланс."""
    account = BankAccount(balance=100)
    account.withdraw(50)
    assert account.check_balance() == 50


# === Инструкции для мутационного тестирования ===
if __name__ == "__main__":
    print(
        """
        === Инструкции для выполнения мутационного тестирования ===
        1. Убедитесь, что установлен mutmut: pip install mutmut
        2. Сохраните этот файл как `project_with_tests.py`.
        3. Выполните команду для запуска мутационного тестирования:
           mutmut run --paths-to-mutate=project_with_tests.py --tests-dir=project_with_tests.py
        4. Если есть выжившие мутанты, используйте команду:
           mutmut show all
        5. Добавьте или измените тесты, чтобы убить всех мутантов.
        """
    )