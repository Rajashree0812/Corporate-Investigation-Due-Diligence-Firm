import os, glob, re

workspace = r"c:\Users\thand\Desktop\Website"
html_files = glob.glob(os.path.join(workspace, "*.html"))
template_files = glob.glob(os.path.join(workspace, "veritas-intelligence-template", "*.html"))

def analyze_files(files, label):
    used_images = {}
    for hf in files:
        base_h = os.path.basename(hf)
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            # find all src="assets/images/..." or url(...)
            matches = re.findall(r'assets/images/[a-zA-Z0-9_\-\./]+\.(?:jpg|png|webp|svg|jpeg)', text)
            for m in matches:
                img_name = os.path.basename(m)
                if img_name not in used_images:
                    used_images[img_name] = []
                used_images[img_name].append(base_h)
    
    print(f"=== {label}: {len(used_images)} unique images referenced ===")
    return used_images

root_used = analyze_files(html_files, "Root HTML Files")
tmpl_used = analyze_files(template_files, "Template HTML Files")

# Check specifically for blog details pages
blog_pages = ["blog-details.html", "blog-details-ma-diligence.html", "blog-details-whistleblower.html"]
print("\n--- Images used in Blog Details Pages ---")
for bp in blog_pages:
    print(f"\nPage: {bp}")
    path = os.path.join(workspace, bp)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            matches = re.findall(r'assets/images/[a-zA-Z0-9_\-\./]+\.(?:jpg|png|webp|svg|jpeg)', f.read())
            for m in sorted(set(matches)):
                base = os.path.basename(m)
                other_pages = [p for p in root_used.get(base, []) if p != bp]
                print(f"  {m} (used in other pages: {other_pages})")
