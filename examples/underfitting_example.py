from debugger.underfitting_detector import detect_underfitting

# Example where model fails to learn properly
train_losses = [0.9, 0.88, 0.85, 0.87]
val_losses = [0.92, 0.9, 0.89, 0.91]

result = detect_underfitting(train_losses, val_losses)
print("Returned result:", result)
