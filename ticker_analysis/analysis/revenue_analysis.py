import matplotlib.pyplot as plt


def plot_revenue_data(revenue, quarterly_revenue):
    fig, ax = plt.subplots()
    ax.bar(revenue.index.year, revenue.values, label="Annual Revenue")
    ax.bar(quarterly_revenue.index, quarterly_revenue.values, label="Quarterly Revenue", alpha=0.7)
    ax.set_title("Revenue Growth")
    ax.set_ylabel("USD")
    ax.legend()
    plt.show()
