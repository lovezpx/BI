import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


# 制图工具类
class PlotUtil:
    # 条形图
    def barplot(self, data):
        sns.barplot("x-axis", "y-axis", palette="RdBu_r", data=data)
        plt.xticks(rotation=90)
        plt.show()


if __name__ == "__main__":
    plotUtil = PlotUtil();

    x = np.arange(8)
    y = np.array([1, 5, 3, 6, 2, 4, 5, 7])
    df = pd.DataFrame({"x-axis": x, "y-axis": y})

    # plotUtil.barplot(df)

    df2 = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [2, 3, 4, 5]], index=list('1234'),
                       columns=list('ABCD'))
    df3 = pd.DataFrame([[35], [26], [95], [122]], index=list('1234'), columns=list('E'))

    df4 = df2.join(df3)
    print(df4.describe())
