def analyze_train_val_gap(train_losses, val_losses, gap_threshold=0.3):
    """
    Analyze the gap between training and validation losses to detect
    overfitting or unstable training behavior.

    Returns:
        dict: analysis summary
    """

    if len(train_losses) != len(val_losses):
        raise ValueError("Training and validation loss lists must be the same length.")

    gaps = [v - t for t, v in zip(train_losses, val_losses)]

    persistent_gap = all(gap > gap_threshold for gap in gaps[-3:])
    sudden_divergence = any(gap > gap_threshold for gap in gaps)

    if persistent_gap:
        status = "persistent_gap_detected"
        message = "Validation loss consistently higher than training loss."
    elif sudden_divergence:
        status = "sudden_divergence_detected"
        message = "Sudden spike detected between training and validation loss."
    else:
        status = "normal_training"
        message = "No significant train-validation gap detected."

    result = {
        "status": status,
        "message": message,
        "final_gap": round(gaps[-1], 3)
    }

    print(f"🔎 Gap analysis result: {status}")
    return result
