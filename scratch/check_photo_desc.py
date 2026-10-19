import urllib.request, re

pids = [
    ('1513635269975-59663e0ac1ad', 'blog_city_towers'),
    ('1589829545856-d10d557cf95f', 'blog_legal_documents'),
    ('1497366811353-6870744d04b2', 'blog_hearing_suite'),
    ('1550751827-4bd374c3f58b', 'blog_cyber_intel')
]

for pid, name in pids:
    url = f'https://unsplash.com/photos/{pid}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        m = re.search(r'<title>(.*?)</title>', html)
        desc = re.search(r'<meta name="description" content="(.*?)"', html)
        print(f'=== {name} ({pid}) ===')
        if m: print('Title:', m.group(1))
        if desc: print('Desc:', desc.group(1))
    except Exception as e:
        print(f'{name} error: {e}')
