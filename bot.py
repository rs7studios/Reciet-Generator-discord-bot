import discord
from discord import app_commands
from PIL import Image, ImageDraw, ImageFont
import io
import os
import random
import string
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path=r'C:\Users\maksb\OneDrive\Desktop\Receit generator\.env')
TOKEN = os.getenv('TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

STORES = [
    ("Best Buy", "8923 Bay Pkwy", "Brooklyn"),
    ("Walmart", "2975 Richmond Ave", "Staten Island"),
    ("Target", "139 Flatbush Ave", "Brooklyn"),
    ("Home Depot", "550 Hamilton Ave", "Brooklyn"),
    ("CVS Pharmacy", "1201 Atlantic Ave", "Brooklyn"),
    ("Costco", "976 Third Ave", "Brooklyn"),
    ("Walgreens", "4301 Queens Blvd", "Queens"),
    ("Rite Aid", "882 Flatbush Ave", "Brooklyn"),
]

ITEMS_POOL = {
    "Best Buy": [("TV 55in Samsung", 499.99), ("HDMI Cable", 19.99), ("USB Hub", 29.99), ("Laptop Stand", 39.99), ("Wireless Mouse", 24.99), ("Keyboard", 59.99), ("Monitor", 299.99), ("Headphones", 79.99)],
    "Walmart": [("Tide Pods 42ct", 12.97), ("Bread", 2.98), ("Milk 1gal", 3.48), ("Eggs 12ct", 4.97), ("Chicken Breast", 8.97), ("Rice 5lb", 4.97), ("Orange Juice", 3.97), ("Dish Soap", 2.97)],
    "Target": [("Paper Towels 6pk", 9.99), ("Shampoo", 6.99), ("Body Wash", 5.99), ("Toothpaste", 3.99), ("Deodorant", 4.99), ("Face Wash", 7.99), ("Laundry Detergent", 11.99), ("Trash Bags", 8.99)],
    "Home Depot": [("Light Bulbs 4pk", 8.97), ("Extension Cord", 14.97), ("Paint Brush Set", 12.97), ("Duct Tape", 6.97), ("Screwdriver Set", 19.97), ("WD-40", 7.97), ("Batteries AA 8pk", 9.97), ("Zip Ties", 4.97)],
    "CVS Pharmacy": [("Advil 50ct", 9.99), ("Band-Aids 30ct", 5.99), ("Vitamin C", 8.99), ("Cough Syrup", 7.99), ("Hand Sanitizer", 3.99), ("Chapstick", 2.99), ("Sunscreen SPF50", 10.99), ("Eye Drops", 6.99)],
    "Costco": [("Paper Towels 12pk", 19.99), ("Chicken Breast 6lb", 14.99), ("Mixed Nuts 2lb", 17.99), ("Olive Oil 2L", 12.99), ("Tide Pods 96ct", 24.99), ("Water 40pk", 9.99), ("Salmon 3lb", 22.99), ("Cheese 2lb", 11.99)],
    "Walgreens": [("Tylenol 100ct", 11.99), ("Allergy Pills 30ct", 9.99), ("Moisturizer", 8.99), ("Nail Polish", 4.99), ("Cotton Balls", 2.99), ("Pregnancy Test", 12.99), ("Vitamins D3", 7.99), ("Melatonin 60ct", 8.99)],
    "Rite Aid": [("Ibuprofen 50ct", 7.99), ("Cough Drops", 3.99), ("Antacid 48ct", 6.99), ("Sleep Aid 16ct", 8.99), ("First Aid Kit", 14.99), ("Thermometer", 11.99), ("Rubbing Alcohol", 2.99), ("Gauze Pads", 4.99)],
}

PAYMENTS = [("VISA", "4"), ("MASTERCARD", "5"), ("AMEX", "3"), ("DISCOVER", "6")]

def generate_trans_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_mcc():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_receipt():
    store_name, address, city = random.choice(STORES)
    items_pool = ITEMS_POOL[store_name]
    num_items = random.randint(2, 5)
    selected_items = random.sample(items_pool, num_items)
    payment, card_start = random.choice(PAYMENTS)
    card_last4 = card_start + ''.join(random.choices(string.digits, k=3))
    tax_rate = random.choice([0.0, 8.0, 8.875])

    width = 400
    padding = 30
    line_h = 22
    font_size = 15

    try:
        font = ImageFont.truetype("cour.ttf", font_size)
        font_bold = ImageFont.truetype("courbd.ttf", font_size)
    except:
        font = ImageFont.load_default()
        font_bold = font

    subtotal = sum(p for _, p in selected_items)
    tax = subtotal * (tax_rate / 100)
    total = subtotal + tax
    now = datetime.now().strftime("%m/%d/%Y      %I:%M %p")
    trans = generate_trans_id()
    mcc = generate_mcc()
    dash = '-' * 42

    height = padding * 2 + line_h * (14 + len(selected_items))
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    y = padding

    def write(text, bold=False, center=False):
        nonlocal y
        f = font_bold if bold else font
        x = width // 2 if center else padding
        anchor = 'mt' if center else 'lt'
        draw.text((x, y), text, fill='black', font=f, anchor=anchor)
        y += line_h

    def write_row(left, right):
        nonlocal y
        draw.text((padding, y), left, fill='black', font=font, anchor='lt')
        draw.text((width - padding, y), right, fill='black', font=font, anchor='rt')
        y += line_h

    write(store_name, bold=True, center=True)
    write(address, center=True)
    write(city, center=True)
    y += 5
    write(dash)
    write(now)
    write(dash)
    y += 5
    write(f"  TRANS - {trans}")
    write(f"  MCC - {mcc}")
    write(f"  PAYMENT - {payment} {card_last4}")
    y += 5
    write(dash)
    y += 5

    for name, price in selected_items:
        write_row(f"  {name}", f"${price:.2f}")

    y += 5
    write(dash)
    y += 5
    write_row("SUBTOTAL:", f"${subtotal:.2f}")
    write_row("TAX:", f"${tax:.2f}")
    write_row("TOTAL:", f"${total:.2f}")
    y += 10
    write("")
    write("PLEASE COME AGAIN", center=True)
    write("THANK YOU", center=True)

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

@tree.command(name="receipt", description="Generate a random receipt")
async def receipt(interaction: discord.Interaction):
    await interaction.response.defer()
    buf = generate_receipt()
    file = discord.File(buf, filename="receipt.png")
    await interaction.followup.send(file=file)

@client.event
async def on_ready():
    await tree.sync()
    print(f'Bot is online as {client.user}')

try:
    client.run(TOKEN)
except Exception as e:
    print(f"Error: {e}")
    input("Press Enter to exit...")