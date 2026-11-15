
import os
import numpy as np
import pandas as pd

from evidently import Report
from evidently.presets import DataDriftPreset

os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

reference_path = "data/reference.csv"
current_path = "data/current.csv"

# Generate reference data if it does not exist
if not os.path.exists(reference_path):

    rng = np.random.default_rng(42)

    reference = pd.DataFrame({
        "num": rng.normal(50, 15, 200),
        "denominator": rng.normal(10, 3, 200)
    })

    reference["num"] = reference["num"].clip(lower=1)
    reference["denominator"] = reference["denominator"].clip(lower=1)

    reference.to_csv(reference_path, index=False)

# Generate demonstration current data if it does not exist
if not os.path.exists(current_path):

    rng = np.random.default_rng(100)

    current = pd.DataFrame({
        "num": rng.normal(70, 15, 200),
        "denominator": rng.normal(16, 3, 200)
    })

    current["num"] = current["num"].clip(lower=1)
    current["denominator"] = current["denominator"].clip(lower=1)

    current.to_csv(current_path, index=False)

reference_data = pd.read_csv(reference_path)
current_data = pd.read_csv(current_path)

# Generate data drift report
report = Report([
    DataDriftPreset()
])

snapshot = report.run(
    current_data=current_data,
    reference_data=reference_data
)

snapshot.save_html("reports/data_drift_report.html")

print("Evidently monitoring completed!")
print("Reference records:", len(reference_data))
print("Current records:", len(current_data))
print("Report saved in reports/data_drift_report.html")
