document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('hero-animation');
    const context = canvas.getContext('2d');
    
    // Set internal resolution for high quality
    canvas.width = 1280;
    canvas.height = 720;
    
    const frameCount = 185; // Stop exactly at frame 184 to avoid glitch
    const currentFrame = index => (
      `assets/frames/frame_${index.toString().padStart(4, '0')}.webp`
    );
    
    const images = [];
    const scrollContainer = document.querySelector('.hero-scroll-container');
    
    // Preload all frames to ensure 60fps zero-lag scrolling
    for (let i = 0; i < frameCount; i++) {
      const img = new Image();
      img.src = currentFrame(i);
      images.push(img);
      
      // Draw the first frame immediately once it loads so the screen isn't blank
      if (i === 0) {
        img.onload = () => {
            drawImageCentered(img);
        };
      }
    }
    
    function drawImageCentered(img) {
      if (!img || !img.complete || img.naturalWidth === 0) return;
      
      const canvasRatio = canvas.width / canvas.height;
      const imgRatio = img.width / img.height;
      
      let drawWidth, drawHeight, offsetX, offsetY;
      
      // Implement object-fit: contain logic for the canvas drawing
      // This ensures the logo is never cropped on narrow mobile screens
      if (canvasRatio > imgRatio) {
          drawHeight = canvas.height;
          drawWidth = img.width * (canvas.height / img.height);
          offsetX = (canvas.width - drawWidth) / 2;
          offsetY = 0;
      } else {
          drawWidth = canvas.width;
          drawHeight = img.height * (canvas.width / img.width);
          offsetX = 0;
          offsetY = (canvas.height - drawHeight) / 2;
      }
      
      // Clear the canvas and draw
      context.clearRect(0, 0, canvas.width, canvas.height);
      context.drawImage(img, offsetX, offsetY, drawWidth, drawHeight);
    }
    
    let animationFrameId;
    
    const updateImage = () => {
        const containerRect = scrollContainer.getBoundingClientRect();
        
        // Calculate how far down the scroll container we are
        let scrollFraction = -containerRect.top / (containerRect.height - window.innerHeight);
        
        // Clamp values between 0 and 1
        scrollFraction = Math.max(0, Math.min(1, scrollFraction));
        
        // Find the exact frame to display
        const frameIndex = Math.min(
            frameCount - 1,
            Math.floor(scrollFraction * frameCount)
        );
        
        requestAnimationFrame(() => {
            drawImageCentered(images[frameIndex]);
        });
    };
    
    window.addEventListener('scroll', () => {
        // Throttle updates using requestAnimationFrame for butter smooth performance
        if (!animationFrameId) {
            animationFrameId = requestAnimationFrame(() => {
                updateImage();
                animationFrameId = null;
            });
        }
    });
    
    // Redraw on window resize to ensure correct proportions
    window.addEventListener('resize', () => {
        updateImage();
    });
});
