import random
import json

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

palette = [random_color() for _ in range(5)]

with open("palettes/sample_palette.json", "w") as f:
    json.dump(palette, f, indent=2)

print("Generated palette:", palette)
