# Water Remover App 💧

A powerful web-based application for removing watermarks from images using advanced image processing techniques.

## Features

- 🎯 **Multiple Processing Methods**: Inpaint, Gaussian Blur, and Median Filter
- 🚀 **Fast Processing**: Quick image processing with instant downloads
- 🔒 **Privacy First**: Images are processed locally and automatically deleted
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎨 **Multiple Format Support**: PNG, JPG, JPEG, GIF, and BMP
- 💾 **Easy Download**: Get your processed images instantly

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Farman72642/newcodbot.git
cd newcodbot
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Quick Start (Alternative)

You can use the provided convenience scripts:

**On Linux/Mac:**
```bash
./run.sh
```

**On Windows:**
```batch
run.bat
```

These scripts will automatically create a virtual environment, install dependencies, and start the application.

## Usage

1. Start the application:
```bash
python app.py
```

Or use the convenience scripts mentioned above.

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload an image and select a processing method:
   - **Inpaint**: Intelligently fills watermark areas (recommended)
   - **Gaussian Blur**: Smooths the image to reduce visibility
   - **Median Filter**: Removes noise and light watermarks

4. Click "Remove Watermark" and download your processed image

## Technology Stack

- **Python 3.x**: Core programming language
- **Flask**: Web framework
- **OpenCV**: Image processing library
- **Pillow**: Python Imaging Library
- **NumPy**: Numerical computing library

## Project Structure

```
newcodbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   └── about.html       # About page
├── uploads/             # Temporary upload folder
└── README.md            # This file
```

## API Endpoints

- `GET /` - Home page with upload form
- `POST /upload` - Upload and process image
- `GET /about` - About page with information

## Requirements

- Python 3.7 or higher
- See `requirements.txt` for Python package dependencies

## Configuration

The application can be configured using environment variables:

- `SECRET_KEY`: Flask secret key for sessions (auto-generated if not set)
- `FLASK_DEBUG`: Enable debug mode (`true` or `false`, default: `false`)
- `FLASK_HOST`: Host to bind to (default: `127.0.0.1`)
- `FLASK_PORT`: Port to run on (default: `5000`)

Other settings in `app.py`:

- `UPLOAD_FOLDER`: Temporary upload directory
- `MAX_CONTENT_LENGTH`: Maximum file upload size (default: 16MB)
- `ALLOWED_EXTENSIONS`: Allowed file extensions

### Example with Environment Variables

```bash
export SECRET_KEY="your-secret-key-here"
export FLASK_DEBUG="false"
export FLASK_HOST="0.0.0.0"
export FLASK_PORT="8080"
python app.py
```

## Processing Methods

### Inpaint Method (Recommended)
Uses OpenCV's inpainting algorithm to intelligently fill watermark regions by analyzing surrounding pixels. Best for removing solid watermarks.

### Gaussian Blur
Applies Gaussian blur to smooth out watermarks. Good for subtle watermarks or when you want to preserve more of the original image structure.

### Median Filter
Removes noise and light watermarks by replacing each pixel with the median of neighboring pixels. Effective for scattered or noisy watermarks.

## Security Features

- File type validation
- Secure filename handling
- Automatic cleanup of uploaded files
- File size limits
- Input sanitization

## Disclaimer

This tool is intended for educational purposes and for removing watermarks from your own images or images where you have the legal right to do so. Please respect copyright laws and intellectual property rights.

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
