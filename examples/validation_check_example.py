from debugger.validation_checker import check_time_series_validation

# Example with leakage risk
train_indices = [0, 1, 2, 3, 4]
val_indices = [3, 4, 5, 6]

result = check_time_series_validation(train_indices, val_indices)

print("Returned result:", result)
print("⚠️ Severity:", result["severity"].upper())
print("💡 Recommendation:", result["recommendation"])
