import cv2
import numpy as np
import os

frames_dir = 'assets/frames'
differences = []

# We'll check the last 40 frames to find where the animation stabilizes and where the glitch happens
for i in range(150, 191):
    f1_path = os.path.join(frames_dir, f'frame_{i:04d}.jpg')
    f2_path = os.path.join(frames_dir, f'frame_{i+1:04d}.jpg')
    
    if not os.path.exists(f1_path) or not os.path.exists(f2_path):
        continue
        
    img1 = cv2.imread(f1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(f2_path, cv2.IMREAD_GRAYSCALE)
    
    # Calculate Mean Squared Error between the two frames
    err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
    err /= float(img1.shape[0] * img1.shape[1])
    
    print(f"Diff between {i} and {i+1}: {err}")
    
