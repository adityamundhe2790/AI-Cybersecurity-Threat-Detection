import matplotlib.pyplot as plt

def plot_results(preds):
    plt.hist(preds)
    plt.title("Anomaly Detection Results")
    plt.savefig("outputs/result.png")
    plt.show()