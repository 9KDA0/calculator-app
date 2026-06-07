#!/usr/bin/env python3
"""
Простой калькулятор с текстовым интерфейсом.
Поддерживает: +, -, ×, ÷, ^, √
"""

import math
import sys


# ── Математические функции ──────────────────────────────────────────

def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание второго числа из первого."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Деление первого числа на второе."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b


def power(a: float, b: float) -> float:
    """Возведение числа a в степень b."""
    return a ** b


def sqrt(a: float) -> float:
    """Квадратный корень числа."""
    if a < 0:
        raise ValueError("Нельзя извлечь квадратный корень из отрицательного числа!")
    return math.sqrt(a)


# ── Вспомогательные функции ─────────────────────────────────────────

def get_number(prompt: str) -> float:
    """Безопасный ввод числа с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ❌ Ошибка: введите корректное число!")
        except (EOFError, KeyboardInterrupt):
            print("\n  👋 Выход...")
            sys.exit(0)


def print_header():
    """Красивый заголовок."""
    print()
    print("╔" + "═" * 48 + "╗")
    print("║" + "       🧮  К А Л Ь К У Л Я Т О Р  🧮       ".center(56) + "║")
    print("╚" + "═" * 48 + "╝")


def print_menu():
    """Меню выбора операции."""
    print()
    print("  ┌──────────────────────────────────────┐")
    print("  │  Выберите операцию:                  │")
    print("  │                                      │")
    print("  │   1. ➕   Сложение                   │")
    print("  │   2. ➖   Вычитание                  │")
    print("  │   3. ✖️   Умножение                  │")
    print("  │   4. ➗   Деление                    │")
    print("  │   5. 🔼   Возведение в степень      │")
    print("  │   6. √    Квадратный корень          │")
    print("  │                                      │")
    print("  │   0. 🚪   Выход                      │")
    print("  └──────────────────────────────────────┘")


def print_result(expression: str, result: float):
    """Красивый вывод результата."""
    # Форматируем: если целое — без .0
    if result == int(result) and abs(result) < 1e15:
        result_str = str(int(result))
    else:
        result_str = f"{result:.6g}"
    print()
    print("  ╔" + "═" * 46 + "╗")
    print(f"  ║  ✅  {expression} = {result_str}".ljust(49) + "║")
    print("  ╚" + "═" * 46 + "╝")


def print_error(message: str):
    """Вывод ошибки."""
    print()
    print(f"  ╔{'═' * 46}╗")
    print(f"  ║  ❌  {message}".ljust(49) + "║")
    print(f"  ╚{'═' * 46}╝")


# ── Главный цикл ────────────────────────────────────────────────────

def main():
    print_header()

    while True:
        print_menu()

        try:
            choice = input("\n  Ваш выбор (0-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n  👋 До свидания!")
            break

        # Выход
        if choice == "0":
            print("\n  👋 До свидания!")
            break

        # Проверка корректности выбора
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print_error("Неверный выбор. Введите число от 0 до 6.")
            continue

        try:
            # Квадратный корень — одно число
            if choice == "6":
                a = get_number("  Введите число: ")
                result = sqrt(a)
                print_result(f"√{a}", result)

            # Бинарные операции — два числа
            else:
                a = get_number("  Введите первое число: ")
                b = get_number("  Введите второе число: ")

                if choice == "1":
                    result = add(a, b)
                    print_result(f"{a} + {b}", result)
                elif choice == "2":
                    result = subtract(a, b)
                    print_result(f"{a} - {b}", result)
                elif choice == "3":
                    result = multiply(a, b)
                    print_result(f"{a} × {b}", result)
                elif choice == "4":
                    result = divide(a, b)
                    print_result(f"{a} ÷ {b}", result)
                elif choice == "5":
                    result = power(a, b)
                    print_result(f"{a} ^ {b}", result)

        except ValueError as e:
            print_error(str(e))
        except Exception as e:
            print_error(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  👋 До свидания!")
        sys.exit(0)
