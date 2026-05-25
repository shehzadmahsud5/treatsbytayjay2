import cv2
import os
import glob

frames_dir = 'assets/frames'
jpg_files = glob.glob(os.path.join(frames_dir, '*.jpg'))

for file in jpg_files:
    img = cv2.imread(file)
    if img is not None:
        # Resize to 960x540 to save space while retaining enough quality for canvas
        resized = cv2.resize(img, (960, 540), interpolation=cv2.INTER_AREA)
        webp_path = file.replace('.jpg', '.webp')
        # Encode as WebP with 80% quality
        cv2.imwrite(webp_path, resized, [cv2.IMWRITE_WEBP_QUALITY, 80])
        # Remove original jpg
        os.remove(file)
        
print("Successfully converted all frames to WebP.")
