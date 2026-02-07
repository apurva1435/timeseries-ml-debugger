from debugger.overfitting_detector import detect_overfitting
from debugger.underfitting_detector import detect_underfitting
from debugger.gap_analyzer import analyze_train_val_gap


def analyze_training(train_losses, val_losses):
    """
    Run multiple diagnostics to analyze model training behavior.

    Returns:
        dict: Combined analysis results
    """

    print("\n🔍 Running unified training analysis...\n")

    overfit_result = detect_overfitting(train_losses, val_losses)
    underfit_result = detect_underfitting(train_losses, val_losses)
    gap_result = analyze_train_val_gap(train_losses, val_losses)

    return {
        "overfitting": overfit_result,
        "underfitting": underfit_result,
        "gap_analysis": gap_result
    }
