def detect_underfitting(train_losses, val_losses, threshold=0.7):
    """
    Detects possible underfitting by checking if both training and
    validation losses remain high across epochs.

    Returns:
        dict: information about underfitting detection
    """

    if len(train_losses) != len(val_losses):
        raise ValueError("Training and validation loss lists must be of equal length.")

    avg_train_loss = sum(train_losses) / len(train_losses)
    avg_val_loss = sum(val_losses) / len(val_losses)

    if avg_train_loss > threshold and avg_val_loss > threshold:
        result = {
            "underfitting": True,
            "avg_train_loss": round(avg_train_loss, 3),
            "avg_val_loss": round(avg_val_loss, 3)
        }
        print("⚠️ Possible underfitting detected: losses remain high.")
        return result

    result = {
        "underfitting": False,
        "avg_train_loss": round(avg_train_loss, 3),
        "avg_val_loss": round(avg_val_loss, 3)
    }
    print("✅ No significant underfitting detected.")
    return result
