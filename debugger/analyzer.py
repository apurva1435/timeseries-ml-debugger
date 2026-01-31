from debugger.overfitting_detector import detect_overfitting
from debugger.underfitting_detector import detect_underfitting


def analyze_training(train_losses, val_losses):
    """
    Runs multiple diagnostics to analyze model training behavior.
    """

    print("\n🔍 Running training analysis...\n")

    overfit_result = detect_overfitting(train_losses, val_losses)
    underfit_result = detect_underfitting(train_losses, val_losses)

    summary = {
        "overfitting": overfit_result,
        "underfitting": underfit_result
    }

  
    return summary
