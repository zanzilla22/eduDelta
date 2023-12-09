import React, { useEffect, useRef } from 'react';

const Live2DAvatar = ({ modelPath }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    // Ensure the Live2D SDK is loaded
    if (window.Live2D) {
      try {
        // Initialize the Live2D model here using the SDK
        // You will need to refer to the SDK documentation for specific initialization code
        // This typically involves creating a new Live2D model instance
        // and loading the model data and textures.
        
        const live2DModel = new window.Live2DModel(canvasRef.current, modelPath);
        // Start rendering the model
        live2DModel.start();
      } catch (e) {
        console.error('Error initializing Live2D model:', e);
      }
    }
  }, [modelPath]);

  return (
    <canvas ref={canvasRef} width="300" height="500">
      {/* Canvas where the Live2D model will render */}
    </canvas>
  );
};

export default Live2DAvatar;
