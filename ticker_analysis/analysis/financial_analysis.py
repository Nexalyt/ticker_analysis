import matplotlib.pyplot as plt


def plot_financial_ratios(ratios):
    labels = ratios.keys()
    values = ratios.values()
    plt.bar(labels, values)
    plt.title('Financial Ratios')
    plt.show()
