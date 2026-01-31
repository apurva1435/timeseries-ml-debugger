from debugger.overfitting_detector import detect_overfitting

train_losses = [0.9, 0.7, 0.5, 0.3, 0.2]
val_losses = [0.95, 0.8, 0.75, 0.78, 0.82]

result = detect_overfitting(train_losses, val_losses)
print("Returned result:", result)
