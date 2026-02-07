def check_time_series_validation(train_indices, val_indices):
    """
    Checks for potential data leakage and validation issues
    in time-series train/validation splits.

    Args:
        train_indices (list): Indices or timestamps used for training
        val_indices (list): Indices or timestamps used for validation

    Returns:
        dict: Validation check results
    """

    train_set = set(train_indices)
    val_set = set(val_indices)

    # Check for overlap
    overlap = train_set.intersection(val_set)

    if overlap:
        status = "data_leakage_detected"
        severity = "high"
        message = "Training and validation data overlap detected."
        recommendation = (
            "Ensure strict temporal separation between training and validation sets."
        )

    # Check for temporal ordering
    elif max(train_indices) > min(val_indices):
        status = "temporal_order_violation"
        severity = "medium"
        message = "Validation data occurs before training data ends."
        recommendation = (
            "Use forward-chaining or time-aware splits for validation."
        )

    else:
        status = "valid_split"
        severity = "low"
        message = "No data leakage detected in train-validation split."
        recommendation = "Current validation strategy is appropriate."

    print(f"🧪 Validation check result: {status}")

    return {
        "status": status,
        "severity": severity,
        "message": message,
        "recommendation": recommendation
    }
