# timeseries-ml-debugger

A lightweight, beginner-friendly toolkit to analyze and debug common failure modes
in machine learning models trained on time-series data.

This project focuses on **why models fail**, not just how to train them.

---

## 🔍 Problem Overview

Machine learning models trained on time-series data often fail silently due to issues such as:
- overfitting to training data
- underfitting due to overly simple models
- misleading or unstable training behavior

These problems are difficult to diagnose, especially for beginners and early-stage researchers.

This toolkit provides **simple, reusable diagnostics and visualizations** to identify
such issues early in the model development process.

---

## ✅ Current Features

- **Overfitting Detection**
  - Detects divergence between training and validation loss

- **Underfitting Detection**
  - Identifies when both losses remain consistently high

- **Unified Training Analyzer**
  - Runs multiple diagnostics together and returns a structured summary

- **Train–Validation Gap Analysis**
  - Detects persistent gaps and sudden divergence
  - Assigns severity levels (low / medium / high)
  - Provides actionable recommendations for corrective steps

- **Loss Curve Visualization**
  - Plots and saves training vs validation loss curves

- **Beginner-Friendly Examples**
  - Minimal runnable examples for each feature

---

## ▶️ How to Run

Clone the repository and run examples from the project root.

```bash
git clone https://github.com/apurva1435/timeseries-ml-debugger.git
cd timeseries-ml-debugger
