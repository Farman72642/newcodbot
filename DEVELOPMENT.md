# Water Remover App - Development Guide

## Overview
This document provides additional information for developers working on the Water Remover App.

## Architecture

### Application Flow
1. User uploads an image via the web interface
2. Flask receives the file and validates it
3. Image is temporarily saved to the `uploads/` directory
4. Selected processing method is applied to the image
5. Processed image is returned to the user as a download
6. Temporary file is immediately deleted

### Processing Methods

#### 1. Inpaint Method (Recommended)
- **Algorithm**: OpenCV INPAINT_TELEA
- **How it works**: 
  - Converts image to grayscale
  - Detects bright regions (threshold: 240)
  - Creates a mask of watermark areas
  - Uses inpainting to fill masked regions based on surrounding pixels
- **Best for**: Solid, bright watermarks

#### 2. Gaussian Blur
- **Algorithm**: Gaussian convolution with 5x5 kernel
- **How it works**: Applies Gaussian blur to smooth the entire image
- **Best for**: Subtle watermarks where preservation of structure is important

#### 3. Median Filter
- **Algorithm**: Median filter with 5x5 kernel
- **How it works**: Replaces each pixel with median of neighbors
- **Best for**: Scattered or noisy watermarks

## Security Features

### File Handling
- File type validation using `allowed_file()` function
- Secure filename sanitization with `secure_filename()`
- Maximum file size limit (16MB)
- Automatic cleanup of uploaded files

### Application Security
- Secret key auto-generation if not provided
- Debug mode disabled by default in production
- Host binding to localhost by default (not 0.0.0.0)
- Environment variable configuration support

### Dependencies
All dependencies are regularly updated to patch security vulnerabilities:
- Pillow >= 10.2.0 (patched CVE)
- Werkzeug >= 3.0.3 (patched debugger vulnerability)

## Testing

### Running Tests
```bash
python test_app.py
```

### Test Coverage
- File structure validation
- Application structure validation
- Template structure validation
- README content validation

## Development Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Local Development
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
export FLASK_DEBUG="true"
export FLASK_HOST="127.0.0.1"
python app.py
```

## Production Deployment

### Environment Variables
Set these for production:
```bash
export SECRET_KEY="generate-a-strong-random-key-here"
export FLASK_DEBUG="false"
export FLASK_HOST="0.0.0.0"  # Or specific IP
export FLASK_PORT="5000"
```

### Using a Production Server
For production, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Future Enhancements

Possible improvements for future versions:
- [ ] Batch processing of multiple images
- [ ] Advanced watermark detection using ML
- [ ] Support for video watermark removal
- [ ] User accounts and processing history
- [ ] API endpoint for programmatic access
- [ ] Docker containerization
- [ ] Additional image enhancement options
- [ ] Preview before download

## Contributing

When contributing to this project:
1. Follow PEP 8 style guidelines for Python code
2. Add tests for new features
3. Update documentation
4. Ensure security best practices
5. Test with various image formats and sizes

## License

This project is open source and available for educational purposes.
