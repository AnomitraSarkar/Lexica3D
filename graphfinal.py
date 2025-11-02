
import matplotlib.pyplot as plt
import numpy as np

# === Data ===
models = ["Shap-E", "Hybrid Model"]
vertex_error = [5, 0.75]
inference_time_min = [2.8, 7.55]   # In minutes
watertightness = [34, 2]          # In percentage

# === Setup ===
x = np.arange(len(models))
bar_width = 0.25

fig, ax = plt.subplots(figsize=(8, 5))

# === Plot Bars ===
bars_vertex = ax.bar(x - bar_width, vertex_error, width=bar_width, label="Vertex Error", alpha=0.8)
bars_time = ax.bar(x, inference_time_min, width=bar_width, label="Inference Time (min)", alpha=0.8)
bars_water = ax.bar(x + bar_width, watertightness, width=bar_width, label="Watertightness (%)", alpha=0.8)

# === Add Labels on Bars ===
def add_labels(bars):
    """Attach a text label above each bar displaying its height."""
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval:.2f}",
                ha='center', va='bottom', fontsize=9)

for b in [bars_vertex, bars_time, bars_water]:
    add_labels(b)

# === Formatting ===
ax.set_xlabel("Model", fontsize=12)
ax.set_ylabel("Metric Values", fontsize=12)
ax.set_title("Performance Comparison: Shap-E vs Hybrid Model", fontsize=14, weight="bold")
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()
