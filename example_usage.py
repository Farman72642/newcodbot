"""
Example script showing how to use the Water Remover App programmatically
"""

import requests
import os

def remove_watermark_from_file(image_path, method='inpaint', server_url='http://localhost:5000'):
    """
    Remove watermark from an image file using the Water Remover App API
    
    Args:
        image_path: Path to the input image
        method: Processing method ('inpaint', 'blur', or 'median')
        server_url: URL of the Water Remover App server
    
    Returns:
        bytes: Processed image data
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Prepare the request
    with open(image_path, 'rb') as f:
        files = {'file': f}
        data = {'method': method}
        
        # Send POST request to the upload endpoint
        response = requests.post(
            f'{server_url}/upload',
            files=files,
            data=data
        )
    
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Error processing image: {response.status_code}")


def save_processed_image(image_data, output_path):
    """
    Save processed image data to a file
    
    Args:
        image_data: Image data as bytes
        output_path: Path where to save the processed image
    """
    with open(output_path, 'wb') as f:
        f.write(image_data)
    print(f"Processed image saved to: {output_path}")


# Example usage
if __name__ == '__main__':
    # Example: Remove watermark from an image
    try:
        # Make sure the server is running on localhost:5000
        input_image = 'input.jpg'  # Replace with your image path
        output_image = 'output.png'
        
        print("Processing image...")
        processed_data = remove_watermark_from_file(
            image_path=input_image,
            method='inpaint',
            server_url='http://localhost:5000'
        )
        
        save_processed_image(processed_data, output_image)
        print("Done!")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nTo use this script:")
        print("1. Start the Water Remover App: python app.py")
        print("2. Place an image file named 'input.jpg' in this directory")
        print("3. Run this script: python example_usage.py")
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure the Water Remover App is running:")
        print("python app.py")
