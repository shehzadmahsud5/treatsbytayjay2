import cv2
import os

video_path = 'logo-animation.mp4'
output_dir = 'assets/frames'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video stream or file")
    exit(1)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    # Optional: resize if the video is extremely large to save load time
    # frame = cv2.resize(frame, (1280, 720))
    
    # Save frame as JPEG with 80% quality to balance size and quality
    output_path = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(output_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames successfully.")
