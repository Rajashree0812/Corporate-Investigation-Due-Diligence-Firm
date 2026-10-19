import os
from PIL import Image, ImageEnhance

brain_dir = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e"
workspace = r"c:\Users\thand\Desktop\Website"

src = os.path.join(brain_dir, "blog_mandate_cta_1791957823858.jpg")
target1 = os.path.join(workspace, "assets", "images", "banners", "banner-ma-due-diligence.jpg")
target2 = os.path.join(workspace, "veritas-intelligence-template", "assets", "images", "banners", "banner-ma-due-diligence.jpg")

im = Image.open(src)
# 4:3 4K resolution: 3840 x 2867
im_4k = im.resize((3840, 2867), Image.Resampling.LANCZOS)
enhancer = ImageEnhance.Sharpness(im_4k)
im_4k = enhancer.enhance(1.15)

im_4k.save(target1, "JPEG", quality=95, optimize=True)
im_4k.save(target2, "JPEG", quality=95, optimize=True)
print(f"Saved banner-ma-due-diligence.jpg: {im_4k.size} to both locations.")
