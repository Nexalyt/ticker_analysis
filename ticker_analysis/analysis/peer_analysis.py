import matplotlib.pyplot as plt


def plot_peer_comparison(peer_data):
    plt.bar(peer_data.keys(), peer_data.values())
    plt.title("Peer Comparison (P/E Ratios)")
    plt.ylabel("P/E Ratio")
    plt.show()
