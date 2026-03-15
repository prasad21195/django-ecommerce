"""
Script to load data with local product images
Run this script to populate your database with products
Usage: python load_data.py
"""

import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from shop.models import Category, Product
from decimal import Decimal
from pathlib import Path

# ============ CATEGORIES DATA ============

CATEGORIES = [
    {"name": "Electronics", "description": "Electronic devices and gadgets"},
    {"name": "Clothing", "description": "Clothes and fashion items"},
    {"name": "Home & Garden", "description": "Home and garden products"},
    {"name": "Sports", "description": "Sports equipment and accessories"},
    {"name": "Books", "description": "Books and literature"},
    {"name": "Beauty", "description": "Beauty and personal care"},
    {"name": "Toys", "description": "Toys and games for all ages"},
]

# ============ PRODUCTS DATA WITH LOCAL IMAGES ============

PRODUCTS = [
    # ===== ELECTRONICS =====
    {
        "name": "Wireless Headphones Pro",
        "description": "Premium wireless headphones with active noise cancellation",
        "detailed_description": "Experience crystal clear audio with our premium wireless headphones",
        "price": Decimal("99.99"),
        "discount_price": Decimal("79.99"),
        "category": "Electronics",
        "stock": 50,
        "is_featured": True,
        "sku": "WH-001",
        "image_file": "headphones.jpg",
    },
    {
        "name": "USB-C Fast Charging Cable",
        "description": "Durable USB-C cable with fast charging support",
        "detailed_description": "High-quality USB-C cable for fast charging",
        "price": Decimal("19.99"),
        "category": "Electronics",
        "stock": 100,
        "sku": "USB-001",
        "image_file": "phone.jpg",
    },
    {
        "name": "Adjustable Phone Stand",
        "description": "Universal adjustable phone stand",
        "detailed_description": "Adjustable phone stand made from premium aluminum",
        "price": Decimal("14.99"),
        "discount_price": Decimal("9.99"),
        "category": "Electronics",
        "stock": 75,
        "is_featured": True,
        "sku": "PS-001",
        "image_file": "phone.jpg",
    },
    {
        "name": "Ergonomic Wireless Mouse",
        "description": "Ergonomic wireless mouse with precision tracking",
        "detailed_description": "Comfortable ergonomic wireless mouse",
        "price": Decimal("29.99"),
        "category": "Electronics",
        "stock": 60,
        "sku": "WM-001",
        "image_file": "laptop.jpg",
    },
    {
        "name": "4-Port USB 3.0 Hub",
        "description": "Fast 4-port USB 3.0 hub",
        "detailed_description": "Expand your USB connectivity",
        "price": Decimal("34.99"),
        "discount_price": Decimal("24.99"),
        "category": "Electronics",
        "stock": 45,
        "sku": "UH-001",
        "image_file": "laptop.jpg",
    },
    {
        "name": "Protective Phone Case",
        "description": "Durable protective phone case",
        "detailed_description": "Heavy-duty phone case with protection",
        "price": Decimal("12.99"),
        "category": "Electronics",
        "stock": 200,
        "sku": "PC-001",
        "image_file": "phone.jpg",
    },
    {
        "name": "Tempered Glass Screen Protector",
        "description": "Premium tempered glass screen protector",
        "detailed_description": "9H hardness tempered glass",
        "price": Decimal("9.99"),
        "category": "Electronics",
        "stock": 150,
        "sku": "SP-001",
        "image_file": "phone.jpg",
    },
    {
        "name": "Aluminum Laptop Stand",
        "description": "Premium aluminum laptop stand",
        "detailed_description": "Portable aluminum laptop stand",
        "price": Decimal("49.99"),
        "discount_price": Decimal("39.99"),
        "category": "Electronics",
        "stock": 40,
        "is_featured": True,
        "sku": "LS-001",
        "image_file": "laptop.jpg",
    },
    {
        "name": "RGB Mechanical Keyboard",
        "description": "Professional RGB mechanical keyboard",
        "detailed_description": "Gaming-grade mechanical keyboard",
        "price": Decimal("89.99"),
        "discount_price": Decimal("69.99"),
        "category": "Electronics",
        "stock": 35,
        "sku": "KB-001",
        "image_file": "laptop.jpg",
    },
    {
        "name": "27-inch 4K Monitor",
        "description": "27-inch 4K IPS display monitor",
        "detailed_description": "High-resolution 4K IPS monitor",
        "price": Decimal("299.99"),
        "discount_price": Decimal("249.99"),
        "category": "Electronics",
        "stock": 20,
        "is_featured": True,
        "sku": "MN-001",
        "image_file": "laptop.jpg",
    },

    # ===== CLOTHING =====
    {
        "name": "Premium Cotton T-Shirt",
        "description": "100% cotton comfortable t-shirt",
        "detailed_description": "High-quality t-shirt made from organic cotton",
        "price": Decimal("29.99"),
        "category": "Clothing",
        "stock": 100,
        "is_featured": True,
        "sku": "TS-001",
        "image_file": "tshirt.jpg",
    },
    {
        "name": "Classic Blue Denim Jeans",
        "description": "Classic blue denim jeans",
        "detailed_description": "Timeless blue denim jeans",
        "price": Decimal("59.99"),
        "discount_price": Decimal("49.99"),
        "category": "Clothing",
        "stock": 75,
        "sku": "JN-001",
        "image_file": "jeans.jpg",
    },
    {
        "name": "Elegant White Polo Shirt",
        "description": "Elegant white polo shirt",
        "detailed_description": "Smart casual polo shirt",
        "price": Decimal("34.99"),
        "category": "Clothing",
        "stock": 60,
        "sku": "PO-001",
        "image_file": "tshirt.jpg",
    },
    {
        "name": "Warm Black Hoodie",
        "description": "Warm black hoodie for winter",
        "detailed_description": "Cozy black hoodie",
        "price": Decimal("49.99"),
        "discount_price": Decimal("39.99"),
        "category": "Clothing",
        "stock": 45,
        "is_featured": True,
        "sku": "HD-001",
        "image_file": "tshirt.jpg",
    },
    {
        "name": "Casual Shorts",
        "description": "Comfortable casual shorts",
        "detailed_description": "Lightweight shorts for warm weather",
        "price": Decimal("24.99"),
        "category": "Clothing",
        "stock": 50,
        "sku": "SH-001",
        "image_file": "jeans.jpg",
    },
    {
        "name": "Light Summer Dress",
        "description": "Flowing light summer dress",
        "detailed_description": "Elegant summer dress",
        "price": Decimal("39.99"),
        "discount_price": Decimal("29.99"),
        "category": "Clothing",
        "stock": 40,
        "sku": "DR-001",
        "image_file": "tshirt.jpg",
    },
    {
        "name": "Heavy Winter Jacket",
        "description": "Warm winter jacket",
        "detailed_description": "Premium winter jacket",
        "price": Decimal("79.99"),
        "discount_price": Decimal("59.99"),
        "category": "Clothing",
        "stock": 35,
        "sku": "JK-001",
        "image_file": "tshirt.jpg",
    },
    {
        "name": "Running Sneakers",
        "description": "Comfortable running sneakers",
        "detailed_description": "Professional running shoes",
        "price": Decimal("69.99"),
        "category": "Clothing",
        "stock": 55,
        "sku": "SN-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Socks Pack (5 Pairs)",
        "description": "Pack of 5 comfortable socks",
        "detailed_description": "Set of 5 pairs of comfortable socks",
        "price": Decimal("14.99"),
        "category": "Clothing",
        "stock": 200,
        "sku": "SK-001",
        "image_file": "tshirt.jpg",
    },
    {
        "name": "Leather Belt",
        "description": "Classic leather belt",
        "detailed_description": "Genuine leather belt",
        "price": Decimal("24.99"),
        "category": "Clothing",
        "stock": 80,
        "sku": "BT-001",
        "image_file": "jeans.jpg",
    },

    # ===== HOME & GARDEN =====
    {
        "name": "Modern LED Table Lamp",
        "description": "Modern LED table lamp",
        "detailed_description": "Elegant LED table lamp",
        "price": Decimal("39.99"),
        "category": "Home & Garden",
        "stock": 30,
        "is_featured": True,
        "sku": "LP-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Wooden Desk Organizer",
        "description": "Wooden desk organizer",
        "detailed_description": "Compact wooden desk organizer",
        "price": Decimal("24.99"),
        "category": "Home & Garden",
        "stock": 50,
        "sku": "DO-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Ceramic Plant Pot",
        "description": "Beautiful ceramic plant pot",
        "detailed_description": "Elegant ceramic pot",
        "price": Decimal("14.99"),
        "category": "Home & Garden",
        "stock": 100,
        "sku": "PT-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Modern Wall Clock",
        "description": "Contemporary wall clock",
        "detailed_description": "Stylish wall clock",
        "price": Decimal("29.99"),
        "discount_price": Decimal("19.99"),
        "category": "Home & Garden",
        "stock": 40,
        "sku": "CK-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Cotton Bed Sheet Set",
        "description": "Soft cotton bed sheet set",
        "detailed_description": "Premium cotton bed sheet set",
        "price": Decimal("44.99"),
        "category": "Home & Garden",
        "stock": 35,
        "sku": "BS-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Memory Foam Pillow",
        "description": "Memory foam pillow",
        "detailed_description": "Orthopedic memory foam pillow",
        "price": Decimal("34.99"),
        "discount_price": Decimal("27.99"),
        "category": "Home & Garden",
        "stock": 45,
        "sku": "PL-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Blackout Curtains",
        "description": "Blackout curtains",
        "detailed_description": "Heavy-duty blackout curtains",
        "price": Decimal("49.99"),
        "category": "Home & Garden",
        "stock": 25,
        "sku": "CR-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Persian Style Rug",
        "description": "Beautiful Persian style rug",
        "detailed_description": "Traditional Persian design rug",
        "price": Decimal("79.99"),
        "category": "Home & Garden",
        "stock": 15,
        "sku": "RG-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Automatic Coffee Maker",
        "description": "Automatic coffee maker",
        "detailed_description": "Programmable coffee maker",
        "price": Decimal("59.99"),
        "discount_price": Decimal("49.99"),
        "category": "Home & Garden",
        "stock": 20,
        "sku": "CF-001",
        "image_file": "lamp.jpg",
    },
    {
        "name": "Ergonomic Office Chair",
        "description": "Ergonomic office chair",
        "detailed_description": "Premium office chair",
        "price": Decimal("129.99"),
        "discount_price": Decimal("99.99"),
        "category": "Home & Garden",
        "stock": 10,
        "sku": "CH-001",
        "image_file": "lamp.jpg",
    },

    # ===== SPORTS =====
    {
        "name": "Non-Slip Yoga Mat",
        "description": "Non-slip yoga mat",
        "detailed_description": "Premium quality yoga mat",
        "price": Decimal("34.99"),
        "category": "Sports",
        "stock": 45,
        "sku": "YM-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Stainless Steel Water Bottle",
        "description": "Insulated stainless steel water bottle",
        "detailed_description": "Double-walled insulated water bottle",
        "price": Decimal("24.99"),
        "discount_price": Decimal("19.99"),
        "category": "Sports",
        "stock": 80,
        "is_featured": True,
        "sku": "WB-001",
        "image_file": "phone.jpg",
    },
    {
        "name": "Adjustable Dumbbells Set",
        "description": "Adjustable dumbbells set",
        "detailed_description": "Adjustable dumbbells",
        "price": Decimal("79.99"),
        "category": "Sports",
        "stock": 25,
        "sku": "DB-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Professional Running Shoes",
        "description": "Professional running shoes",
        "detailed_description": "High-performance running shoes",
        "price": Decimal("89.99"),
        "discount_price": Decimal("69.99"),
        "category": "Sports",
        "stock": 30,
        "sku": "RN-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Professional Tennis Racket",
        "description": "Professional tennis racket",
        "detailed_description": "High-quality tennis racket",
        "price": Decimal("99.99"),
        "category": "Sports",
        "stock": 15,
        "sku": "TR-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Official Basketball",
        "description": "Official basketball",
        "detailed_description": "Professional-grade basketball",
        "price": Decimal("29.99"),
        "category": "Sports",
        "stock": 40,
        "sku": "BB-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Yoga Blocks Set (2)",
        "description": "Set of 2 foam yoga blocks",
        "detailed_description": "Non-slip foam yoga blocks",
        "price": Decimal("19.99"),
        "category": "Sports",
        "stock": 60,
        "sku": "YB-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Resistance Bands Set (5)",
        "description": "Set of 5 resistance bands",
        "detailed_description": "Complete set of resistance bands",
        "price": Decimal("24.99"),
        "category": "Sports",
        "stock": 70,
        "sku": "RB-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Speed Jump Rope",
        "description": "Professional speed jump rope",
        "detailed_description": "High-speed jump rope",
        "price": Decimal("14.99"),
        "category": "Sports",
        "stock": 100,
        "sku": "JR-001",
        "image_file": "shoes.jpg",
    },
    {
        "name": "Large Gym Bag",
        "description": "Large gym bag",
        "detailed_description": "Spacious gym bag",
        "price": Decimal("44.99"),
        "category": "Sports",
        "stock": 35,
        "sku": "GB-001",
        "image_file": "shoes.jpg",
    },

    # ===== BOOKS =====
    {
        "name": "Python Programming Guide",
        "description": "Comprehensive guide to Python",
        "detailed_description": "Learn Python programming",
        "price": Decimal("39.99"),
        "category": "Books",
        "stock": 50,
        "sku": "BK-001",
        "image_file": "book.jpg",
    },
    {
        "name": "Complete Web Development Guide",
        "description": "Complete web development guide",
        "detailed_description": "Learn web development",
        "price": Decimal("44.99"),
        "discount_price": Decimal("34.99"),
        "category": "Books",
        "stock": 40,
        "sku": "BK-002",
        "image_file": "book.jpg",
    },
    {
        "name": "Modern Business Strategy",
        "description": "Modern business strategies",
        "detailed_description": "Learn business strategies",
        "price": Decimal("34.99"),
        "category": "Books",
        "stock": 30,
        "sku": "BK-003",
        "image_file": "book.jpg",
    },
    {
        "name": "Data Science Fundamentals",
        "description": "Data science fundamentals",
        "detailed_description": "Introduction to data science",
        "price": Decimal("49.99"),
        "category": "Books",
        "stock": 25,
        "sku": "BK-004",
        "image_file": "book.jpg",
    },
    {
        "name": "Machine Learning Algorithms",
        "description": "Machine learning algorithms",
        "detailed_description": "Learn ML algorithms",
        "price": Decimal("54.99"),
        "discount_price": Decimal("44.99"),
        "category": "Books",
        "stock": 20,
        "sku": "BK-005",
        "image_file": "book.jpg",
    },
    {
        "name": "Complete JavaScript Guide",
        "description": "Complete JavaScript guide",
        "detailed_description": "Master JavaScript",
        "price": Decimal("39.99"),
        "category": "Books",
        "stock": 35,
        "sku": "BK-006",
        "image_file": "book.jpg",
    },
    {
        "name": "Django Web Development",
        "description": "Build with Django",
        "detailed_description": "Learn Django framework",
        "price": Decimal("44.99"),
        "category": "Books",
        "stock": 30,
        "sku": "BK-007",
        "image_file": "book.jpg",
    },
    {
        "name": "React Handbook",
        "description": "Master React framework",
        "detailed_description": "Complete React guide",
        "price": Decimal("49.99"),
        "category": "Books",
        "stock": 25,
        "sku": "BK-008",
        "image_file": "book.jpg",
    },
    {
        "name": "SQL Database Design",
        "description": "SQL and database design",
        "detailed_description": "Learn SQL",
        "price": Decimal("34.99"),
        "category": "Books",
        "stock": 40,
        "sku": "BK-009",
        "image_file": "book.jpg",
    },
    {
        "name": "DevOps Practices Guide",
        "description": "DevOps practices",
        "detailed_description": "Learn DevOps",
        "price": Decimal("44.99"),
        "category": "Books",
        "stock": 20,
        "sku": "BK-010",
        "image_file": "book.jpg",
    },

    # ===== BEAUTY =====
    {
        "name": "Gentle Face Wash",
        "description": "Gentle facial cleanser",
        "detailed_description": "Mild formula facial cleanser",
        "price": Decimal("14.99"),
        "category": "Beauty",
        "stock": 100,
        "sku": "BC-001",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Hydrating Moisturizer Cream",
        "description": "Hydrating moisturizer cream",
        "detailed_description": "Rich moisturizer",
        "price": Decimal("24.99"),
        "category": "Beauty",
        "stock": 75,
        "is_featured": True,
        "sku": "BC-002",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Moisturizing Lip Balm",
        "description": "Moisturizing lip balm",
        "detailed_description": "Nourishing lip balm",
        "price": Decimal("9.99"),
        "category": "Beauty",
        "stock": 150,
        "sku": "BC-003",
        "image_file": "beauty.jpg",
    },
    {
        "name": "SPF 50 Sunscreen",
        "description": "SPF 50 sunscreen",
        "detailed_description": "Broad-spectrum sunscreen",
        "price": Decimal("19.99"),
        "category": "Beauty",
        "stock": 80,
        "sku": "BC-004",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Sheet Face Mask",
        "description": "Sheet face mask",
        "detailed_description": "Hydrating sheet mask",
        "price": Decimal("12.99"),
        "category": "Beauty",
        "stock": 120,
        "sku": "BC-005",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Anti-Aging Eye Cream",
        "description": "Anti-aging eye cream",
        "detailed_description": "Eye cream for fine lines",
        "price": Decimal("29.99"),
        "category": "Beauty",
        "stock": 45,
        "sku": "BC-006",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Organic Shampoo",
        "description": "Organic shampoo",
        "detailed_description": "Sulfate-free shampoo",
        "price": Decimal("16.99"),
        "category": "Beauty",
        "stock": 90,
        "sku": "BC-007",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Hair Conditioner",
        "description": "Hair conditioner",
        "detailed_description": "Nourishing conditioner",
        "price": Decimal("16.99"),
        "category": "Beauty",
        "stock": 85,
        "sku": "BC-008",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Moisturizing Body Lotion",
        "description": "Body lotion",
        "detailed_description": "Moisturizing lotion",
        "price": Decimal("19.99"),
        "category": "Beauty",
        "stock": 70,
        "sku": "BC-009",
        "image_file": "beauty.jpg",
    },
    {
        "name": "Professional Makeup Brush Set",
        "description": "Makeup brush set",
        "detailed_description": "Professional brushes",
        "price": Decimal("34.99"),
        "category": "Beauty",
        "stock": 35,
        "sku": "BC-010",
        "image_file": "beauty.jpg",
    },

    # ===== TOYS =====
    {
        "name": "Educational Building Blocks",
        "description": "Building blocks set",
        "detailed_description": "Educational blocks",
        "price": Decimal("29.99"),
        "category": "Toys",
        "stock": 45,
        "sku": "TY-001",
        "image_file": "toy.jpg",
    },
    {
        "name": "High-Speed RC Car",
        "description": "Remote control car",
        "detailed_description": "High-speed RC car",
        "price": Decimal("49.99"),
        "discount_price": Decimal("39.99"),
        "category": "Toys",
        "stock": 30,
        "sku": "TY-002",
        "image_file": "toy.jpg",
    },
    {
        "name": "1000 Piece Puzzle Game",
        "description": "Jigsaw puzzle",
        "detailed_description": "1000-piece puzzle",
        "price": Decimal("19.99"),
        "category": "Toys",
        "stock": 60,
        "sku": "TY-003",
        "image_file": "toy.jpg",
    },
    {
        "name": "Marvel Action Figure",
        "description": "Action figure",
        "detailed_description": "Marvel superhero",
        "price": Decimal("24.99"),
        "category": "Toys",
        "stock": 50,
        "sku": "TY-004",
        "image_file": "toy.jpg",
    },
    {
        "name": "Family Board Game",
        "description": "Board game",
        "detailed_description": "Family game",
        "price": Decimal("34.99"),
        "category": "Toys",
        "stock": 25,
        "sku": "TY-005",
        "image_file": "toy.jpg",
    },
    {
        "name": "RPG Dice Set",
        "description": "Dice set",
        "detailed_description": "RPG dice",
        "price": Decimal("14.99"),
        "category": "Toys",
        "stock": 100,
        "sku": "TY-006",
        "image_file": "toy.jpg",
    },
    {
        "name": "Colorful Play Dough",
        "description": "Play dough",
        "detailed_description": "Non-toxic play dough",
        "price": Decimal("9.99"),
        "category": "Toys",
        "stock": 150,
        "sku": "TY-007",
        "image_file": "toy.jpg",
    },
    {
        "name": "Flying Kite",
        "description": "Kite",
        "detailed_description": "Colorful kite",
        "price": Decimal("12.99"),
        "category": "Toys",
        "stock": 70,
        "sku": "TY-008",
        "image_file": "toy.jpg",
    },
    {
        "name": "Professional Yo-Yo",
        "description": "Yo-yo",
        "detailed_description": "Professional yo-yo",
        "price": Decimal("14.99"),
        "category": "Toys",
        "stock": 80,
        "sku": "TY-009",
        "image_file": "toy.jpg",
    },
    {
        "name": "3x3 Rubik's Cube",
        "description": "Rubik's cube",
        "detailed_description": "Classic puzzle",
        "price": Decimal("9.99"),
        "category": "Toys",
        "stock": 120,
        "sku": "TY-010",
        "image_file": "toy.jpg",
    },
]

# ============ LOAD DATA FUNCTIONS ============

def get_image_path(image_filename):
    """Get full path to image file"""
    image_dir = Path(__file__).parent / "shop" / "static" / "images" / "products"
    image_path = image_dir / image_filename
    return image_path


def load_categories():
    """Load all categories"""
    print("=" * 60)
    print("LOADING CATEGORIES")
    print("=" * 60)
    
    created_count = 0
    for cat_data in CATEGORIES:
        category, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults=cat_data
        )
        if created:
            print(f"✓ Created: {category.name}")
            created_count += 1
        else:
            print(f"- Already exists: {category.name}")
    
    print(f"\nTotal categories: {Category.objects.count()}\n")


def load_products():
    """Load all products with LOCAL images"""
    print("=" * 60)
    print("LOADING PRODUCTS WITH LOCAL IMAGES")
    print("=" * 60)
    
    created_count = 0
    
    for prod_data in PRODUCTS:
        category_name = prod_data.pop("category")
        image_filename = prod_data.pop("image_file", None)
        
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            print(f"✗ Category '{category_name}' not found")
            continue
        
        product, created = Product.objects.get_or_create(
            name=prod_data["name"],
            defaults={**prod_data, "category": category}
        )
        
        if created:
            print(f"✓ Created: {product.name}")
            
            # Add image if file exists
            if image_filename:
                image_path = get_image_path(image_filename)
                
                if image_path.exists():
                    try:
                        with open(image_path, 'rb') as img_file:
                            product.image.save(
                                image_filename,
                                File(img_file),
                                save=True
                            )
                        print(f"  ✓ Image added: {image_filename}")
                    except Exception as e:
                        print(f"  ✗ Error adding image: {e}")
                else:
                    print(f"  ✗ Image file not found: {image_filename}")
            
            created_count += 1
        else:
            print(f"- Already exists: {product.name}")
    
    print(f"\nTotal products: {Product.objects.count()}")
    print(f"Newly created: {created_count}\n")


# ============ MAIN ============

if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + "LOADING DATA WITH LOCAL IMAGES".center(58) + "║")
    print("╚" + "=" * 58 + "╝\n")
    
    try:
        load_categories()
        load_products()
        
        print("=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"Categories: {Category.objects.count()}")
        print(f"Products: {Product.objects.count()}")
        print("\n")
        print("╔" + "=" * 58 + "╗")
        print("║" + "✓ DATA LOADING COMPLETE!".center(58) + "║")
        print("╚" + "=" * 58 + "╝\n")
        
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}\n")