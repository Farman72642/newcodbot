"""
Water Remover App - A Flask web application for removing watermarks from images
"""

import os
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24).hex())
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def remove_watermark(image_path, method='inpaint'):
    """
    Remove watermark from image using various methods
    
    Args:
        image_path: Path to the input image
        method: Method to use for watermark removal ('inpaint', 'blur', 'median')
    
    Returns:
        Processed image as numpy array
    """
    # Read the image
    img = cv2.imread(image_path)
    
    if img is None:
        raise ValueError("Could not read image")
    
    if method == 'inpaint':
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply threshold to detect bright watermark areas
        # Threshold of 240 detects very bright regions typically used for watermarks
        _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
        
        # Dilate the mask to cover watermark completely
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=2)
        
        # Inpaint the watermark region
        result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
        
    elif method == 'blur':
        # Apply Gaussian blur to smooth out watermarks
        result = cv2.GaussianBlur(img, (5, 5), 0)
        
    elif method == 'median':
        # Apply median filter to remove noise and light watermarks
        result = cv2.medianBlur(img, 5)
        
    else:
        result = img
    
    return result


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and processing"""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Get selected method
        method = request.form.get('method', 'inpaint')
        
        try:
            # Process the image
            processed_img = remove_watermark(filepath, method)
            
            # Convert BGR to RGB for PIL
            processed_img_rgb = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
            
            # Convert to PIL Image
            pil_img = Image.fromarray(processed_img_rgb)
            
            # Save to bytes buffer
            img_buffer = io.BytesIO()
            pil_img.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            
            # Clean up uploaded file
            os.remove(filepath)
            
            return send_file(
                img_buffer,
                mimetype='image/png',
                as_attachment=True,
                download_name=f'processed_{filename}'
            )
            
        except Exception as e:
            flash(f'Error processing image: {str(e)}')
            if os.path.exists(filepath):
                os.remove(filepath)
            return redirect(url_for('index'))
    
    flash('Invalid file type. Allowed types: png, jpg, jpeg, gif, bmp')
    return redirect(url_for('index'))


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


if __name__ == '__main__':
    # Get debug and host settings from environment variables
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', '5000'))
    
    app.run(debug=debug_mode, host=host, port=port)
