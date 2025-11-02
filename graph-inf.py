import matplotlib.pyplot as plt
import numpy as np

# Models
models = [
    "DreamGaussian", "ProlificDreamer", "GET3D", "Shap-E",
    "Michelangelo", "ClipFace", "Latent-NeRF", "Fantasia3D",
    "Point-E", "VPP"
]

# Inference times (average, in seconds)
inference_times = np.array([
    (185+178+185)/3,     
    (585+682+610)/3,     
    (61+58+64)/3,        
    (43+46+41)/3,        
    (165+185+170)/3,     
    (78+90+82)/3,        
    (2240+1546+1805)/3,  
    (1126+1170+1073)/3,  
    (72+97+80)/3,        
    (9+12+7)/3           
])

# Plot
plt.figure(figsize=(12,6))
bars = plt.bar(models, inference_times, color="tab:blue")
plt.ylabel("Inference Time (s)")
plt.title("Inference Time Comparison of 3D Generative Models")
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

plt.savefig("graph-inf.png")
