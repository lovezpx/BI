import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


def ptlot():
    try:
        x = np.arange(8)
        y = np.array([1, 5, 3, 6, 2, 4, 5, 7])

        df = pd.DataFrame({"x-axis": x, "y-axis": y})

        sns.barplot("x-axis", "y-axis", palette="RdBu_r", data=df)
        plt.xticks(rotation=90)
        plt.show()

        u = 0  # 均值μ
        u01 = -2
        sig = math.sqrt(0.2)  # 标准差δ

        x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
        y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
        print(x)
        print("=" * 20)
        print(y_sig)
        plt.plot(x, y_sig, "r-", linewidth=2)
        plt.grid(True)
        plt.show()

        df = pd.DataFrame(np.random.rand(15, 4), columns=['a', 'b', 'c', 'd'])
        df.plot.area()
        plt.xticks(rotation=90)
        plt.show()
    except KeyError as Argument:
        print("BaseException" + Argument)
    else:
        print("END")


if __name__ == '__main__':
    ptlot()