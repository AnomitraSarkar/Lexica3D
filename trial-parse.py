import json

output_file = "output.obj"
data=[]
with open('trial-dataset.jsonl', 'r') as f:
  data = json.load(f)
  
  print(data)

faces = data.get('faces',[])
vertices = data.get('vertices', [])
with open(output_file, "w") as f:
    for i in vertices:
        f.write(f"{i}\n")
    for i in faces:
        f.write(f"{i}\n")
print(f"Written file: {output_file}")
