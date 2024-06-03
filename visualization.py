import matplotlib.pyplot as plt
import seaborn as sns

def plot_conservation_heatmap(sequences):
    conservation_scores = [len(seq) - seq.count('-') for seq in sequences]
    # Create the heatmap using seaborn and matplotlib
    # Example:
    plt.figure(figsize=(10, 6))
    sns.heatmap([conservation_scores], annot=True, cmap="YlGnBu")
    plt.xlabel("Sequence Position")
    plt.ylabel("Sequence Index")
    plt.title("Sequence Conservation Heatmap")
    plt.show()
