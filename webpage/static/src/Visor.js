import React, { useRef } from 'react'

import './Viso.css';

function Visor({ image }) {
    
    const canvasRef = useRef(null);
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    
    context.drawImage(image,0,0);

    return(
        <canvas ref={canvasRef}/>
    )
}

export { Visor };