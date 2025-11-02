
import matplotlib.pyplot as plt
import numpy as np

# Models
models = [
    "DreamGaussian", "ProlificDreamer", "GET3D",
    "Shap-E", "Michelangelo", "ClipFace",
    "Latent-NeRF", "Fantasia3D", "Point-E", "VPP"
]

# Quantitative aspect: Vertex Error (%) - lower is better
vertex_error = [
    17, 20, 25,   # DreamGaussian, ProlificDreamer, GET3D
    5, 18, 15,    # Shap-E, Michelangelo, ClipFace
    22, 19, 21, 3 # Latent-NeRF, Fantasia3D, Point-E, VPP
]

# Qualitative descriptions
qualitative_aspect = [
    "Extremely high-fidelity; NOT optimization-ready due to heavy mesh flow",
    "High-fidelity geometry; minor over-smoothing; NOT optimization-ready",
    "Good geometric detail; minor blurring; NOT optimization-ready",
    "Good mesh structure; smooth textures; moderate detail; stable optimization pipeline",
    "Good semantic shape adherence; moderate geometric detail; NOT optimization-ready",
    "High semantic fidelity for facial shape; limited fine-detail; NOT optimization-ready since heavy mesh flow",
    "Moderate view consistency; edges are blurred; neRF data conversion costly on hardware but stable",
    "Excellent multi-view consistency; crisp mesh geometry; NOT optimization-ready kernel crashed",
    "Accurate coarse geometry; visible sparsity; low resolution; stable optimization achieved",
    "Good coarse geometry; smooth point distribution; minor voxelization artifacts; multi-context resilient; stable optimization pipeline"
]

# Create bar graph for quantitative aspect
x = np.arange(len(models))
plt.figure(figsize=(14,6))
plt.bar(x, vertex_error, color='skyblue')
plt.xticks(x, models, rotation=45, ha='right')
plt.ylabel('Vertex Error (%)')
plt.title('Vertex Error (%) of 3D Generative Models')

# Add value labels on bars
for i, v in enumerate(vertex_error):
    plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()
plt.savefig("graph-err.png")

# Print qualitative table
import pandas as pd

df = pd.DataFrame({
    "Model": models,
    "Qualitative Assessment": qualitative_aspect
})

print(df.to_string(index=False))
