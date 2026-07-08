import os
import json

IMAGE_DIR = 'images2'
MANIFEST_FILE = 'gallery.json'

# Trova tutti i file ignorando cartelle e file nascosti
images = []
if os.path.exists(IMAGE_DIR):
    for f in sorted(os.listdir(IMAGE_DIR)):
        if os.path.isfile(os.path.join(IMAGE_DIR, f)) and not f.startswith('.'):
            images.append(f)

# Crea il file JSON
with open(MANIFEST_FILE, 'w') as f:
    json.dump(images, f, indent=4)

print(f"Manifest generato! {len(images)} immagini trovate.")
