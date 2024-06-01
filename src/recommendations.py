import glob
import streamlit as st
from PIL import Image

predicted_label_list = predicted_label_list = ['Shirts', 'Jeans', 'Watches', 'Track Pants', 'Tshirts', 'Socks',
       'Casual Shoes', 'Belts', 'Flip Flops', 'Handbags', 'Tops', 'Bra',
       'Sandals', 'Shoe Accessories', 'Sweatshirts', 'Deodorant',
       'Formal Shoes', 'Bracelet', 'Lipstick', 'Flats', 'Kurtas',
       'Waistcoat', 'Sports Shoes', 'Shorts', 'Briefs', 'Sarees',
       'Perfume and Body Mist', 'Heels', 'Sunglasses', 'Innerwear Vests',
       'Pendant', 'Nail Polish', 'Laptop Bag', 'Scarves', 'Rain Jacket',
       'Dresses', 'Night suits', 'Skirts', 'Wallets', 'Blazers', 'Ring',
       'Kurta Sets', 'Clutches', 'Shrug', 'Backpacks', 'Caps', 'Trousers',
       'Earrings', 'Camisoles', 'Boxers', 'Jewellery Set', 'Dupatta',
       'Capris', 'Lip Gloss', 'Bath Robe', 'Mufflers', 'Tunics',
       'Jackets', 'Trunk', 'Lounge Pants', 'Face Wash and Cleanser',
       'Necklace and Chains', 'Duffel Bag', 'Sports Sandals',
       'Foundation and Primer', 'Sweaters', 'Free Gifts', 'Trolley Bag',
       'Tracksuits', 'Swimwear', 'Shoe Laces', 'Fragrance Gift Set',
       'Bangle', 'Nightdress', 'Ties', 'Baby Dolls', 'Leggings',
       'Highlighter and Blush', 'Travel Accessory', 'Kurtis',
       'Mobile Pouch', 'Messenger Bag', 'Lip Care', 'Face Moisturisers',
       'Compact', 'Eye Cream', 'Accessory Gift Set', 'Beauty Accessory',
       'Jumpsuit', 'Kajal and Eyeliner', 'Water Bottle', 'Suspenders',
       'Lip Liner', 'Robe', 'Salwar and Dupatta', 'Patiala', 'Stockings',
       'Eyeshadow', 'Headband', 'Tights', 'Nail Essentials', 'Churidar',
       'Lounge Tshirts', 'Face Scrub and Exfoliator', 'Lounge Shorts',
       'Gloves', 'Mask and Peel', 'Wristbands', 'Tablet Sleeve',
       'Ties and Cufflinks', 'Footballs', 'Stoles', 'Shapewear',
       'Nehru Jackets', 'Salwar', 'Cufflinks', 'Jeggings', 'Hair Colour',
       'Concealer', 'Rompers', 'Body Lotion', 'Sunscreen', 'Booties',
       'Waist Pouch', 'Hair Accessory', 'Rucksacks', 'Basketballs',
       'Lehenga Choli', 'Clothing Set', 'Mascara', 'Toner',
       'Cushion Covers', 'Key chain', 'Makeup Remover', 'Lip Plumper',
       'Umbrellas', 'Face Serum and Gel', 'Hat', 'Mens Grooming Kit',
       'Rain Trousers', 'Body Wash and Scrub', 'Suits', 'Ipad']

def get_recommendations(predicted_label):
    
    #Button to call the model
    recommendations_button =st.button("Get Recommendations")
    if recommendations_button:


        st.header(f"Item predicted as {predicted_label}. Here are similar items:")
        
        #Display recommendations
        image_paths = glob.glob(f"data/{predicted_label}/*")
        count=0
        for image_path in image_paths:
            image = Image.open(image_path)
            st.image(image, use_column_width=True)
            st.text("Item: Item Name")
            st.text("Description: Item Description")
            st.text("Price: $99.99")
            st.button("Buy Now",key = count)
            count += 1


