from PIL import Image, ImageDraw

def boundary_fill(img, x, y, fill, boundary):
    if (0 <= x < img.width) and (0 <= y < img.height):
        current = img.getpixel((x, y))
        if current != boundary and current != fill:
            img.putpixel((x, y), fill)
            boundary_fill(img, x+1, y, fill, boundary)
            boundary_fill(img, x-1, y, fill, boundary)
            boundary_fill(img, x, y+1, fill, boundary)
            boundary_fill(img, x, y-1, fill, boundary)

# Create image and rectangle boundary
img = Image.new("RGB", (100, 100), "white")
draw = ImageDraw.Draw(img)
draw.rectangle([30, 30, 70, 70], outline="black")

# Apply boundary fill
boundary_fill(img, 50, 50, (255, 0, 0), (0, 0, 0))

img.show()
