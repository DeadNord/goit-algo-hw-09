import time
from tabulate import tabulate
import matplotlib.pyplot as plt


class GreedyChangeMaker:
    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)

    def find_coins(self, amount):
        result = {}
        for coin in self.denominations:
            if amount >= coin:
                num_coins = amount // coin
                amount -= num_coins * coin
                result[coin] = num_coins
        return result


class DynamicChangeMaker:
    def __init__(self, denominations):
        self.denominations = sorted(denominations)

    def find_coins(self, amount):
        # Table to store the minimum number of coins for each amount from 0 to amount
        min_coins = [float("inf")] * (amount + 1)
        min_coins[0] = 0

        # Table to store the last used coin to form the amount
        last_coin = [0] * (amount + 1)

        for coin in self.denominations:
            for i in range(coin, amount + 1):
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    last_coin[i] = coin

        # Reconstruct the result from the tables
        result = {}
        while amount > 0:
            coin = last_coin[amount]
            result[coin] = result.get(coin, 0) + 1
            amount -= coin

        return result


# Функція для вимірювання часу виконання функції
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time


def main(denominations, test_amounts):
    greedy_maker = GreedyChangeMaker(denominations)
    dynamic_maker = DynamicChangeMaker(denominations)

    greedy_times = []
    dynamic_times = []

    results = []

    for amount in test_amounts:
        greedy_result, greedy_time = measure_time(greedy_maker.find_coins, amount)
        dynamic_result, dynamic_time = measure_time(dynamic_maker.find_coins, amount)

        greedy_times.append(greedy_time)
        dynamic_times.append(dynamic_time)

        results.append([amount, greedy_time, dynamic_time])

        print(
            f"Amount: {amount}, Greedy Result: {greedy_result}, Dynamic Result: {dynamic_result}"
        )

    # Виведення результатів у таблиці за допомогою tabulate
    headers = ["Amount", "Greedy Algorithm Time (s)", "Dynamic Algorithm Time (s)"]
    table = tabulate(results, headers=headers, tablefmt="pipe")
    print(table)

    # Побудова графіків за допомогою matplotlib
    plt.plot(test_amounts, greedy_times, label="Greedy Algorithm", marker="o")
    plt.plot(test_amounts, dynamic_times, label="Dynamic Algorithm", marker="o")
    plt.xlabel("Amount")
    plt.ylabel("Time (s)")
    plt.title("Algorithm Performance Comparison")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    denominations = [50, 25, 10, 5, 2, 1]
    test_amounts = [113]
    main(denominations, test_amounts)

    denominations = [50, 25, 10, 5, 2, 1]
    test_amounts = [87, 143, 289, 498, 1023, 3764]
    main(denominations, test_amounts)
