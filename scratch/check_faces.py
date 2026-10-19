import cv2, os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
upperbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

scratch = r'C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\scratch'
test_imgs = [
    os.path.join(scratch, 'blog_city_towers.jpg'),
    os.path.join(scratch, 'blog_legal_documents.jpg'),
    os.path.join(scratch, 'blog_hearing_suite.jpg'),
    os.path.join(scratch, 'blog_cyber_intel.jpg'),
    'assets/images/banners/banner-cta.jpg'
]

for p in test_imgs:
    if not os.path.exists(p):
        print('NOT FOUND:', p)
        continue
    img = cv2.imread(p)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    bodies = upperbody_cascade.detectMultiScale(gray, 1.1, 4)
    print(f'{os.path.basename(p)} -> Faces: {len(faces)}, Upper bodies: {len(bodies)}')
