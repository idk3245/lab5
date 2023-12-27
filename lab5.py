import numpy as np
import matplotlib.pyplot as plt

class Calculator:
    def add(self, a, b):
        return np.add(a, b)

    def subtract(self, a, b):
        return np.subtract(a, b)

    def multiply(self, a, b):
        return np.multiply(a, b)

    def divide(self, a, b):
        if 0 in b:
            raise ValueError("Division by zero is not allowed.")
        return np.divide(a, b)

def run_tests():
    calculator = Calculator()

    assert calculator.add([1, 2, 3], [4, 5, 6]).tolist() == [5, 7, 9]

    assert calculator.subtract([1, 2, 3], [4, 5, 6]).tolist() == [-3, -3, -3]

    assert calculator.multiply([1, 2, 3], [4, 5, 6]).tolist() == [4, 10, 18]

    assert calculator.divide([1, 2, 3], [2, 1, 3]).tolist() == [0.5, 2.0, 1.0]

if __name__ == "__main__":
    run_tests()

    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, 'Calculator', size=12, ha='center', va='center')
    ax.axis('off')

    plt.show()