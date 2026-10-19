import os
from PIL import Image, ImageEnhance

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
workspace = r"c:\Users\thand\Desktop\Website"
template_dir = os.path.join(workspace, "veritas-intelligence-template")

mapping = [
    {
        "src": os.path.join(brain_dir, "corporate_investigations_1791883501360.jpg"),
        "dest_name": "home-service-investigations.jpg"
    },
    {
        "src": os.path.join(brain_dir, "executive_screening_1791883533720.jpg"),
        "dest_name": "home-service-screening.jpg"
    },
    {
        "src": os.path.join(brain_dir, "ma_due_diligence_1791883574148.jpg"),
        "dest_name": "home-service-ma.jpg"
    },
    {
        "src": os.path.join(brain_dir, "financial_fraud_1791883611509.jpg"),
        "dest_name": "home-service-fraud.jpg"
    }
]

for item in mapping:
    src_path = item["src"]
    dest_name = item["dest_name"]
    print(f"Processing {os.path.basename(src_path)} -> {dest_name}...")
    
    im = Image.open(src_path).convert("RGB")
    # Resize to exact 4K: 3840 x 2160 (16:9)
    im_4k = im.resize((3840, 2160), Image.Resampling.LANCZOS)
    
    # Subtle sharpness enhancement for crisp 4k display
    enhancer = ImageEnhance.Sharpness(im_4k)
    im_4k = enhancer.enhance(1.15)
    
    # Save to root workspace
    dest_path1 = os.path.join(workspace, "assets", "images", "services", dest_name)
    im_4k.save(dest_path1, "JPEG", quality=95, optimize=True)
    
    # Save to template directory
    dest_path2 = os.path.join(template_dir, "assets", "images", "services", dest_name)
    im_4k.save(dest_path2, "JPEG", quality=95, optimize=True)
    
    print(f"  Successfully written {dest_name} in 3840x2160 to both root and template.")

print("All 4 service card images processed to 4K successfully!")
