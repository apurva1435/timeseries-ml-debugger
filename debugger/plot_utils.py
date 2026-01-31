import matplotlib.pyplot as plt


def plot_loss_curves(train_losses, val_losses, save_path="loss_plot.png"):
    """
    Plots training and validation loss curves and saves the figure.
    """

    epochs = range(1, len(train_losses) + 1)

    plt.figure()
    plt.plot(epochs, train_losses, label="Training Loss")
    plt.plot(epochs, val_losses, label="Validation Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training vs Validation Loss")
    plt.legend()
    plt.grid(True)

    plt.savefig(save_path)
    plt.close()

    print(f"📊 Loss curve saved to {save_path}")
