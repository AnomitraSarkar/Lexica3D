import matplotlib.pyplot as plt
import numpy as np

# Models
models = [
    "DreamGaussian", "ProlificDreamer", "GET3D", "Shap-E",
    "Michelangelo", "ClipFace", "Latent-NeRF", "Fantasia3D",
    "Point-E", "VPP"
]

# Memory usage (average, in GB)
memory_usage = np.array([
    (6.5+6.4+6.7)/3,  
    (7.3+6.8+7.1)/3,  
    (4.3+4.2+4.0)/3,  
    (2.9+3.0+2.8)/3,  
    (4.1+4.0+4.2)/3,  
    (3.8+4.0+3.9)/3,  
    (5.1+5.7+5.5)/3,  
    (6.0+6.2+6.1)/3,  
    (3.5+3.6+3.4)/3,  
    (3.6+3.4+3.5)/3   
])

# Plot
plt.figure(figsize=(12,6))
bars = plt.bar(models, memory_usage, color="tab:orange")
plt.ylabel("Memory Usage (GB)")
plt.title("Memory Usage Comparison of 3D Generative Models")
plt.xticks(rotation=45, ha="right")

# Annotate values
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.1f}', 
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

plt.tight_layout()
plt.show()
plt.savefig("graph-mem.png")
