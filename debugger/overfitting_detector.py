def detect_overfitting(train_losses, val_losses, threshold=0.2):
    """
    Detects possible overfitting by comparing training and validation losses.

    Returns:
        dict: information about overfitting detection
    """

    if len(train_losses) != len(val_losses):
        raise ValueError("Training and validation loss lists must be of equal length.")

    for epoch in range(len(train_losses)):
        loss_gap = val_losses[epoch] - train_losses[epoch]
        if loss_gap > threshold:
            result = {
                "overfitting": True,
                "epoch": epoch + 1,
                "gap": round(loss_gap, 3)
            }
            print(f"⚠️ Possible overfitting detected at epoch {epoch + 1}.")
            return result

    result = {
        "overfitting": False,
        "epoch": None,
        "gap": None
    }
    print("✅ No significant overfitting detected.")
    return result
