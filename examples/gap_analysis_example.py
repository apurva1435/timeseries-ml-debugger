from debugger.gap_analyzer import analyze_train_val_gap

train_losses = [0.8, 0.6, 0.4, 0.3, 0.25]
val_losses = [0.85, 0.7, 0.65, 0.7, 0.75]

result = analyze_train_val_gap(train_losses, val_losses)

print("Returned result:", result)
print("⚠️ Severity:", result["severity"].upper())
