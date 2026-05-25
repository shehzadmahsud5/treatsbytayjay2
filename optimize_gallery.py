import cv2
import os
import glob

gallery_dir = 'assets/gallery'
png_files = glob.glob(os.path.join(gallery_dir, '*.png'))

for file in png_files:
    img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    if img is not None:
        webp_path = file.replace('.png', '.webp')
        # Encode as WebP with 80% quality
        cv2.imwrite(webp_path, img, [cv2.IMWRITE_WEBP_QUALITY, 80])
        # Remove original png
        os.remove(file)
        
print("Successfully converted all gallery images to WebP.")
