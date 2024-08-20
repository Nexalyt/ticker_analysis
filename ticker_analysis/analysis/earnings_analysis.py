import matplotlib.pyplot as plt


def plot_earnings_data(net_income, quarterly_net_income):
    fig, ax = plt.subplots()
    ax.bar(net_income.index.year, net_income.values, label="Annual Net Income")
    ax.bar(quarterly_net_income.index, quarterly_net_income.values, label="Quarterly Net Income", alpha=0.7)
    ax.set_title("Net Income Growth")
    ax.set_ylabel("USD")
    ax.legend()
    plt.show()
