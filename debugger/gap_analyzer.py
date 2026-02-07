def analyze_train_val_gap(train_losses, val_losses, gap_threshold=0.3):
    """
    Analyze the gap between training and validation losses to detect
    overfitting or unstable training behavior.

    Args:
    
        train_losses (list): Training loss values per epoch
        val_losses (list): Validation loss values per epoch
        gap_threshold (float): Threshold to flag divergence

    Returns:
        dict: Analysis summary including status and severity
    """

    if len(train_losses) != len(val_losses):
        raise ValueError("Training and validation loss lists must be the same length.")

    # Compute gaps
    gaps = [v - t for t, v in zip(train_losses, val_losses)]
    final_gap = round(gaps[-1], 3)

    # Detect patterns
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

    # Determine severity
    if final_gap < 0.2:
        severity = "low"
    elif final_gap < 0.4:
        severity = "medium"
    else:
        severity = "high"

    print(f"🔎 Gap analysis result: {status}")

    # Actionable suggestion based on severity
    if severity == "high":
        recommendation = "Consider early stopping, stronger regularization, or reducing model complexity."
    elif severity == "medium":
        recommendation = "Monitor training closely and consider tuning hyperparameters."
    else:
        recommendation = "No immediate action required."


   return {
    "status": status,
    "severity": severity,
    "message": message,
    "final_gap": final_gap,
    "recommendation": recommendation
}
