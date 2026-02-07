# timeseries-ml-debugger

A lightweight, beginner-friendly toolkit to analyze and debug common failure modes
in machine learning models trained on time-series data.

This project focuses on **why models fail**, not just how to train them.

---

🔍Problem Overview

Machine learning models trained on time-series data often fail silently due to issues such as:
- overfitting to training data
- underfitting due to overly simple models
- misleading or unstable training behavior

These problems are difficult to diagnose, especially for beginners and early-stage researchers.

This toolkit provides **simple, reusable diagnostics and visualizations** to identify
such issues early in the model development process.

---

✅ Current Features

- **Overfitting Detection**
  - Detects divergence between training and validation loss
- **Underfitting Detection**
  - Identifies when both losses remain consistently high
- **Unified Training Analyzer**
  - Runs multiple diagnostics together and returns a structured summary
- **Loss Curve Visualization**
  - Plots and saves training vs validation loss curves
- **Beginner-Friendly Examples**
  - Minimal runnable examples for each feature

---

▶️ How to Run

Clone the repository and run examples from the project root.

```bash
git clone https://github.com/apurva1435/timeseries-ml-debugger.git

## 📉 Train–Validation Gap Analysis

The toolkit now includes gap-based diagnostics to analyze the relationship
between training and validation loss across epochs.

Features:
- detection of persistent gap and sudden divergence
- severity classification (low / medium / high)
- actionable recommendations for corrective steps

Example:
```bash
python -m examples.gap_analysis_example

cd timeseries-ml-debugger
