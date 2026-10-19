import difflib

f1 = open(r"c:\Users\thand\Desktop\Website\index.html", encoding="utf-8").readlines()
f2 = open(r"c:\Users\thand\Desktop\Website\veritas-intelligence-template\index.html", encoding="utf-8").readlines()

diff = list(difflib.unified_diff(f1, f2, fromfile="root", tofile="template"))
if not diff:
    print("Files are 100% IDENTICAL!")
else:
    print(f"Found {len(diff)} diff lines:")
    for l in diff[:20]:
        print(l.rstrip())
