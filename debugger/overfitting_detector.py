# Simple utility to detect overfitting based on loss trends

def detect_overfitting(train_losses, val_losses, threshold=0.2):
    """
    Detects possible overfitting by comparing training and validation losses.

    Parameters:
    train_losses (list): List of training loss values per epoch
    val_losses (list): List of validation loss values per epoch
    threshold (float): Difference threshold to flag overfitting
    """

    if len(train_losses) != len(val_losses):
        raise ValueError("Training and validation loss lists must be of equal length.")

    for epoch in range(len(train_losses)):
        loss_gap = val_losses[epoch] - train_losses[epoch]
        if loss_gap > threshold:
            print(f"Possible overfitting detected at epoch {epoch + 1}.")
            return

    print("No significant overfitting detected.")
