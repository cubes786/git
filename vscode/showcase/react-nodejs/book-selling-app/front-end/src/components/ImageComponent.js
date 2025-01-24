// frontend/src/components/ImageComponent.js
import React, { useState } from 'react';

const ImageComponent = ({ src, alt, style, fallbackSrc }) => {
    const [imageSrc, setImageSrc] = useState(src);

    const handleImageError = () => {
        if(fallbackSrc){
             setImageSrc(fallbackSrc);
        }
       else{
            setImageSrc('/book-placeholder.jpg') // default placeholder image
        }
    };

    return (
        <img src={imageSrc} alt={alt} style={style} onError={handleImageError} />
    );
};

export default ImageComponent;