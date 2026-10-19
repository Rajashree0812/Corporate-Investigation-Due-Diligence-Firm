import os
from PIL import Image
import numpy as np

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
workspace = r"c:\Users\thand\Desktop\Website"

# Check if service-corporate-investigations.jpg is the same as corporate_investigations_1791883501360.jpg
f1 = os.path.join(brain_dir, "corporate_investigations_1791883501360.jpg")
f2 = os.path.join(workspace, "assets", "images", "services", "service-corporate-investigations.jpg")

im1 = Image.open(f1).resize((100, 100))
im2 = Image.open(f2).resize((100, 100))
diff = np.mean(np.abs(np.array(im1) - np.array(im2)))
print(f"Difference between corporate_investigations artifact and service-corporate-investigations.jpg: {diff}")
