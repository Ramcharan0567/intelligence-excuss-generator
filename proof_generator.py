def generate_proof(excuse_text):
    from PIL import Image, ImageDraw
    import os

    # Create a blank image
    img = Image.new('RGB', (600, 200), color='white')
    draw = ImageDraw.Draw(img)

    # Draw the excuse text
    draw.text((10, 80), excuse_text, fill='black')

    # Save to static folder
    os.makedirs('static', exist_ok=True)
    path = 'static/proof.png'
    img.save(path)

    return '/' + path
