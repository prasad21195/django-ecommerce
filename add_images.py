"""
Script to add images to existing products
Run this script to add images to already created products
Usage: python add_images.py
"""

import os
import django
from django.core.files import File
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from shop.models import Product

# ============ PRODUCT IMAGE MAPPING ============
# Map product names to image filenames

PRODUCT_IMAGES = {
    # Electronics
    "Wireless Headphones Pro": "headphones.jpg",
    "USB-C Fast Charging Cable": "phone.jpg",
    "Adjustable Phone Stand": "phone.jpg",
    "Ergonomic Wireless Mouse": "laptop.jpg",
    "4-Port USB 3.0 Hub": "laptop.jpg",
    "Protective Phone Case": "phone.jpg",
    "Tempered Glass Screen Protector": "phone.jpg",
    "Aluminum Laptop Stand": "laptop.jpg",
    "RGB Mechanical Keyboard": "laptop.jpg",
    "27-inch 4K Monitor": "laptop.jpg",
    
    # Clothing
    "Premium Cotton T-Shirt": "tshirt.jpg",
    "Classic Blue Denim Jeans": "jeans.jpg",
    "Elegant White Polo Shirt": "tshirt.jpg",
    "Warm Black Hoodie": "tshirt.jpg",
    "Casual Shorts": "jeans.jpg",
    "Light Summer Dress": "tshirt.jpg",
    "Heavy Winter Jacket": "tshirt.jpg",
    "Running Sneakers": "shoes.jpg",
    "Socks Pack (5 Pairs)": "tshirt.jpg",
    "Leather Belt": "jeans.jpg",
    
    # Home & Garden
    "Modern LED Table Lamp": "lamp.jpg",
    "Wooden Desk Organizer": "lamp.jpg",
    "Ceramic Plant Pot": "lamp.jpg",
    "Modern Wall Clock": "lamp.jpg",
    "Cotton Bed Sheet Set": "lamp.jpg",
    "Memory Foam Pillow": "lamp.jpg",
    "Blackout Curtains": "lamp.jpg",
    "Persian Style Rug": "lamp.jpg",
    "Automatic Coffee Maker": "lamp.jpg",
    "Ergonomic Office Chair": "lamp.jpg",
    
    # Sports
    "Non-Slip Yoga Mat": "shoes.jpg",
    "Stainless Steel Water Bottle": "phone.jpg",
    "Adjustable Dumbbells Set": "shoes.jpg",
    "Professional Running Shoes": "shoes.jpg",
    "Professional Tennis Racket": "shoes.jpg",
    "Official Basketball": "shoes.jpg",
    "Yoga Blocks Set (2)": "shoes.jpg",
    "Resistance Bands Set (5)": "shoes.jpg",
    "Speed Jump Rope": "shoes.jpg",
    "Large Gym Bag": "shoes.jpg",
    
    # Books
    "Python Programming Guide": "book.jpg",
    "Complete Web Development Guide": "book.jpg",
    "Modern Business Strategy": "book.jpg",
    "Data Science Fundamentals": "book.jpg",
    "Machine Learning Algorithms": "book.jpg",
    "Complete JavaScript Guide": "book.jpg",
    "Django Web Development": "book.jpg",
    "React Handbook": "book.jpg",
    "SQL Database Design": "book.jpg",
    "DevOps Practices Guide": "book.jpg",
    
    # Beauty
    "Gentle Face Wash": "beauty.jpg",
    "Hydrating Moisturizer Cream": "beauty.jpg",
    "Moisturizing Lip Balm": "beauty.jpg",
    "SPF 50 Sunscreen": "beauty.jpg",
    "Sheet Face Mask": "beauty.jpg",
    "Anti-Aging Eye Cream": "beauty.jpg",
    "Organic Shampoo": "beauty.jpg",
    "Hair Conditioner": "beauty.jpg",
    "Moisturizing Body Lotion": "beauty.jpg",
    "Professional Makeup Brush Set": "beauty.jpg",
    
    # Toys
    "Educational Building Blocks": "toy.jpg",
    "High-Speed RC Car": "toy.jpg",
    "1000 Piece Puzzle Game": "toy.jpg",
    "Marvel Action Figure": "toy.jpg",
    "Family Board Game": "toy.jpg",
    "RPG Dice Set": "toy.jpg",
    "Colorful Play Dough": "toy.jpg",
    "Flying Kite": "toy.jpg",
    "Professional Yo-Yo": "toy.jpg",
    "3x3 Rubik's Cube": "toy.jpg",
}

# ============ GET IMAGE PATH ============

def get_image_path(image_filename):
    """Get full path to image file"""
    image_dir = Path(__file__).parent / "shop" / "static" / "images" / "products"
    image_path = image_dir / image_filename
    return image_path


# ============ ADD IMAGES TO PRODUCTS ============

def add_images_to_products():
    """Add images to existing products"""
    print("=" * 60)
    print("ADDING IMAGES TO EXISTING PRODUCTS")
    print("=" * 60 + "\n")
    
    total = 0
    added = 0
    failed = 0
    
    for product_name, image_filename in PRODUCT_IMAGES.items():
        total += 1
        
        try:
            # Find product
            product = Product.objects.get(name=product_name)
            print(f"Found: {product_name}")
            
            # Get image path
            image_path = get_image_path(image_filename)
            
            # Check if image file exists
            if not image_path.exists():
                print(f"  ✗ Image file not found: {image_filename}")
                print(f"    Expected at: {image_path}")
                failed += 1
                continue
            
            # Add image
            with open(image_path, 'rb') as img_file:
                product.image.save(
                    image_filename,
                    File(img_file),
                    save=True
                )
            
            print(f"  ✓ Image added: {image_filename}\n")
            added += 1
            
        except Product.DoesNotExist:
            print(f"✗ Product not found: {product_name}\n")
            failed += 1
        except Exception as e:
            print(f"✗ Error: {e}\n")
            failed += 1
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total products: {total}")
    print(f"Images added: {added}")
    print(f"Failed: {failed}")
    print("=" * 60 + "\n")
    
    if added > 0:
        print("✓ Images added successfully!")
    else:
        print("✗ No images were added. Check image file paths.")


# ============ MAIN ============

if __name__ == "__main__":
    print("\n")
    add_images_to_products()
    print("\n")