import urllib.request, re, os, json

all_pids = [
    "photo-1444653614773-995cb1ef9028",
    "photo-1450133064473-71024230f91b",
    "photo-1451187580459-43490279c0fa",
    "photo-1454165804606-c3d57bc86b40",
    "photo-1455390582262-044cdead277a",
    "photo-1460925895917-afdab827c52f",
    "photo-1464938050520-ef2270bb8ce8",
    "photo-1466611653911-95081537e5b7",
    "photo-1477959858617-67f30bc75b82",
    "photo-1486406146926-c627a92ad1ab",
    "photo-1497215728101-856f4ea42174",
    "photo-1497215842964-222b430dc094",
    "photo-1497366216548-37526070297c",
    "photo-1497366754035-f200968a6e72",
    "photo-1498084393753-b411b2d26b34",
    "photo-1501167786227-4cba60f6d58f",
    "photo-1504384308090-c894fdcc538d",
    "photo-1504868584819-f8e8b4b6d7e3",
    "photo-1506973035872-a4ec16b8e8d9",
    "photo-1507679799987-c73779587ccf",
    "photo-1509198397868-475647b2a1e5",
    "photo-1509390288171-ce2088f7d08e",
    "photo-1510511459019-5dee997ddfef",
    "photo-1513694203232-719a280e022f",
    "photo-1514565131-fce0801e5785",
    "photo-1517502884422-41eaead166d4",
    "photo-1517976487507-5b3a4a080c5e",
    "photo-1519501025264-65ba15a82390",
    "photo-1526374965328-7f61d4dc18c5",
    "photo-1531403009284-440f080d1e12",
    "photo-1532187863486-abf9dbad1b69",
    "photo-1540959733332-eab4deabeeaf",
    "photo-1541872703-74c5e44368f9",
    "photo-1541888946425-d0fbb18086f6",
    "photo-1542744173-8e7e53415bb0",
    "photo-1543096222-72de739f7917",
    "photo-1551288049-bebda4e38f71",
    "photo-1554224155-6726b3ff858f",
    "photo-1554224155-8d04cb21cd6c",
    "photo-1556761175-5973dc0f32e7",
    "photo-1558494949-ef010cbdcc31",
    "photo-1559526324-4b87b5e36e44",
    "photo-1576671081837-49000212a370",
    "photo-1577495508048-b635879837f1",
    "photo-1578575340632-6a4a40669d5f",
    "photo-1578575437130-527eed3abbec",
    "photo-1582719366768-de4481b828ce",
    "photo-1582719471384-894fbb16e074",
    "photo-1586281380349-632531db7ed4",
    "photo-1586528116311-ad8dd3c8310d",
    "photo-1594321120041-00d204971461",
    "photo-1610375461246-83df859d849d",
    "photo-1611974789855-9c2a0a7236a3",
    "photo-1621416894569-0f39ed31d247",
    "photo-1621504450181-5d356f61d307",
    "photo-1625029010191-66ba0c5f2cbb",
    "photo-1633829131104-e2134f75c6e5",
    "photo-1639762681485-074b7f938ba0",
    "photo-1642285709726-f9eb035b034b",
    "photo-1642543492481-44e81e3914a7",
    "photo-1642790106117-e829e14a795f",
    "photo-1644568954144-899f51175074",
    "photo-1663931932716-3086b87f2ed1",
    "photo-1675883161988-0fea4d198709",
    "photo-1681400592810-f5e452af17c5",
    "photo-1681400678259-255b10890b08",
    "photo-1683141154082-324d296f3c66",
    "photo-1695653422715-991ec3a0db7a"
]

results = []
for pid in all_pids[:30]:
    url = f"https://unsplash.com/photos/{pid}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=5).read().decode('utf-8', errors='ignore')
        m = re.search(r'<title>(.*?)</title>', html)
        t = m.group(1).replace(' | Download Free Images on Unsplash', '').replace(' | Unsplash', '') if m else ''
        print(f"{pid}: {t}")
        results.append((pid, t))
    except Exception as e:
        pass

print("\nDone inspecting batch 1")
