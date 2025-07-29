import sqlite3

# Connect to the correct database file
conn = sqlite3.connect('recommender.db')
c = conn.cursor()

# 🔧 Step 1: Create table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    benefits TEXT,
    ingredients TEXT,
    calories TEXT,
    process TEXT,
    youtube_link TEXT,
    image TEXT,
    mood TEXT NOT NULL
)
''')

# 🔧 Step 2: (Optional) Clear old data if you want fresh data every time
c.execute('DELETE FROM suggestions')

# Insert sample data for different moods with embedded YouTube links

data = [
    # HAPPY
    (
    'Pizza Margherita',
    'Classic cheese pizza to lift your spirits.',
    'Dough, Cheese, Tomato Sauce, Basil',
    '400 kcal per slice',
    'Bake dough with sauce and toppings in oven.',
    'https://www.youtube.com/embed/3hzvziYzzZA',
    'https://images.getrecipekit.com/20220211142645-margherita-9920.jpg?aspect_ratio=1:1&quality=90&',
    'happy'
),
(
    'Strawberry Milkshake',
    'Sweet and refreshing drink for joyful vibes.',
    'Strawberries, Milk, Sugar, Ice Cream',
    '250 kcal per glass',
    'Blend all ingredients until smooth and creamy.',
    'https://youtu.be/vwO7nPaAWvs?si=U26zSf6EBNG91b_T',
    'https://therecipecritic.com/wp-content/uploads/2022/05/strawberrymilkshake.jpg',
    'happy'
),
(
    'Chocolate Brownie',
    'Rich and gooey dessert that brings instant joy.',
    'Flour, Cocoa, Sugar, Butter, Eggs',
    '320 kcal per piece',
    'Mix and bake all ingredients until fudgy.',
    'https://youtu.be/rRtngF-Liu4?si=9kmzBcIiXzwYR1w3',
    'https://images.alphacoders.com/838/thumb-1920-838946.jpg',
    'happy'
),
(
    'French Fries',
    'Crispy and salty comfort food loved by all.',
    'Potatoes, Salt, Oil',
    '365 kcal per serving',
    'Slice, fry and season the potatoes.',
    'https://youtu.be/lB8dMNj7JMA?si=G5qrKZNEO2QqcEa8',
    'https://c4.wallpaperflare.com/wallpaper/666/302/422/food-potato-french-fries-hd-wallpaper-preview.jpg',
    'happy'
),
(
    'Paneer Tikka',
    'Indian grilled delight full of flavors.',
    'Paneer, Yogurt, Spices, Capsicum',
    '270 kcal per skewer',
    'Marinate paneer and grill on skewers.',
    'https://youtu.be/BwIJHI4KdIE?si=37tSjb47eOxmnEdQ',
    'https://images.pexels.com/photos/3928854/pexels-photo-3928854.png',
    'happy'
),
(
    'Cheeseburger',
    'Juicy and satisfying treat for good times.',
    'Buns, Cheese, Patty, Lettuce, Sauce',
    '450 kcal per burger',
    'Grill patty, assemble burger with toppings.',
    'https://youtu.be/_q5GKCNZcHI?si=LtnYHX-OB1qsw5g7',
    'https://static.vecteezy.com/system/resources/previews/030/683/548/large_2x/burgers-high-quality-4k-hdr-free-photo.jpg',
    'happy'
),
(
    'Gulab Jamun',
    'Indian sweet that melts in your mouth.',
    'Milk solids, Sugar syrup, Cardamom',
    '180 kcal per piece',
    'Fry balls and soak in sugar syrup.',
    'https://youtu.be/QFvd7u_YjVk?si=wHMaq0feZFaJHlzD',
    'https://namastevictoria.ca/wp-content/uploads/2024/01/gulab-jamun.png',
    'happy'
),
(
    'Fruit Salad',
    'Colorful, healthy, and sweet delight.',
    'Mixed fruits, Honey, Lemon juice, Mint',
    '150 kcal per bowl',
    'Chop and mix all ingredients fresh.',
    'https://youtu.be/tBN_qdB1h7Q?si=_tWgVHLFh9HjUJeK',
    'https://www.thedeliciouscrescent.com/wp-content/uploads/2020/12/Fruit-Salad-7.jpg',
    'happy'
),
(
    'Donuts',
    'Fun and sweet treat for celebrations.',
    'Flour, Sugar, Yeast, Milk, Oil',
    '280 kcal per donut',
    'Fry dough rings and glaze with sugar.',
    'https://youtu.be/w6TxH8ha8XU?si=CL2qgMBDFb3hsNcJ',
    'https://images.pexels.com/photos/3026801/pexels-photo-3026801.jpeg',
    'happy'
),
(
    'Cupcakes',
    'Mini cakes with colorful frosting — perfect for parties!',
    'Flour, Butter, Eggs, Sugar, Frosting',
    '200 kcal per cupcake',
    'Bake batter and decorate with frosting.',
    'https://youtu.be/oD1anfQsgbE?si=jgv6uWlIU8P2zofB',
    'https://images5.alphacoders.com/304/thumb-1920-304630.jpg',
    'happy'
),

# SAD
(
    'Hot Chocolate',
    'Warm and comforting drink, boosts mood.',
    'Milk, Cocoa Powder, Sugar, Chocolate',
    '180 kcal per cup',
    'Heat milk, mix cocoa and sugar, stir until smooth.',
    'https://youtu.be/6nXv-Np-Bc4?si=YcAIzLU6yoau6tIf',
    'https://images2.alphacoders.com/877/877309.jpg',
    'sad'
),
(
    'Mac & Cheese',
    'Creamy comfort food for gloomy days.',
    'Pasta, Cheese, Milk, Butter',
    '410 kcal per bowl',
    'Boil pasta, mix with cheese sauce.',
    'https://youtu.be/YxVZuuxxXxk?si=lbBiMXJfJCEKww3o',
    'https://images3.alphacoders.com/132/thumbbig-1322102.webp',
    'sad'
),
(
    'Momos',
    'Soft and spicy dumplings that feel like a warm hug.',
    'Flour, Veggies/Meat, Spices',
    '200 kcal per plate',
    'Steam filled dumplings and serve hot.',
    'https://youtu.be/4vB5RPMo7HA?si=Edt7t1fffybnM4es',
    'https://e1.pxfuel.com/desktop-wallpaper/56/428/desktop-wallpaper-chef-s-recipe-chicken-momos-by-mad-about-china-the-forum-fiza-mall-mangalore-momo-food.jpg',
    'sad'
),
(
    'Tomato Soup',
    'Soothing and warm, perfect for low moods.',
    'Tomatoes, Herbs, Cream',
    '120 kcal per bowl',
    'Cook tomatoes and blend with seasoning.',
    'https://youtu.be/H7FclpQ--y8?si=Odqz6x1Any-2PIqE',
    'https://www.indianhealthyrecipes.com/wp-content/uploads/2022/11/tomato-soup-recipe.jpg',
    'sad'
),
(
    'Grilled Cheese Sandwich',
    'Golden crunchy comfort between bread slices.',
    'Bread, Cheese, Butter',
    '330 kcal per sandwich',
    'Grill buttered bread with cheese in between.',
    'https://youtu.be/YrdDj36j0Tw?si=cCy3d-5eh_fj-zJA',
    'https://wallpapers.com/images/hd/grilled-cheese-sandwich-dcjm9b7pi8kwzsgg.jpg',
    'sad'
),
(
    'Rice Kheer',
    'Sweet and milky – tastes like childhood comfort.',
    'Rice, Milk, Sugar, Cardamom',
    '240 kcal per bowl',
    'Boil rice with milk and sugar until thick.',
    'https://youtu.be/YwViAlvV4Mo?si=nya34YCmvXjZB4pM',
    'https://as1.ftcdn.net/v2/jpg/05/80/99/02/1000_F_580990235_8Gh3BydggtpyRw62RALPqi145eQYf5fZ.jpg',
    'sad'
),
(
    'Veg Pulao',
    'Warm rice dish to soothe your soul.',
    'Rice, Veggies, Spices, Ghee',
    '290 kcal per bowl',
    'Cook rice with veggies and spices.',
    'https://youtu.be/W1wnXzcxGEU?si=FPcKN2gkr-dCqRqk',
    'https://img.freepik.com/premium-photo/indian-veg-biryani-veg-pulav-4k-hd-photo-indian-vegetable-pulao_1193781-13341.jpg?w=900',
    'sad'
),
(
    'Rajma Chawal',
    'Comfort food classic for Indian hearts.',
    'Kidney Beans, Rice, Spices',
    '360 kcal per serving',
    'Cook beans in masala, serve with rice.',
    'https://youtu.be/M_ncAJhIaIU?si=NZYUgNLDq4yYnG32',
    'https://www.indianveggiedelight.com/wp-content/uploads/2020/02/instant-pot-rajma-masala-featured.jpg',
    'sad'
),
(
    'Banana Smoothie',
    'Natural sweetness to beat the blues.',
    'Banana, Milk, Honey',
    '180 kcal per glass',
    'Blend everything until smooth.',
    'https://youtu.be/wBI-PfvA2T8?si=qTGjI53WS-R9vM43',
    'https://fitelo.co/wp-content/uploads/2020/05/banana-smoothie-recipes--2048x1363.jpg',
    'sad'
),
(
    'Stuffed Paratha',
    'Hearty stuffed flatbread that feels like home.',
    'Wheat, Potatoes, Spices, Butter',
    '320 kcal per paratha',
    'Roll, stuff and cook with butter.',
    'https://youtu.be/pa5X-04HW1M?si=bkTD40nhXAURqmY_',
    'https://image.freepik.com/free-photo/aloo-paratha-indian-potato-stuffed-flatbread-with-butter-top-served-with-fresh-sweet-lassi-chutney-pickle-selective-focus_466689-49095.jpg',
    'sad'
),
(
    'Paneer Bhurji',
    'Soft scrambled paneer with spices.',
    'Paneer, Onion, Tomato, Spices',
    '250 kcal per serving',
    'Cook crumbled paneer with onion and tomato.',
    'https://youtu.be/TP9FheJgclQ?si=LaxHAD3NmkqEIPf1',
    'https://www.cookwithmanali.com/wp-content/uploads/2019/06/Paneer-Bhurji-Recipe-Vegetarian-Indian-Cottage-Cheese-Scramble.jpg',
    'sad'
),
(
    'Sweet Corn Chaat',
    'Warm and sweet-savory snack.',
    'Corn, Butter, Chilli, Lemon',
    '180 kcal per bowl',
    'Boil corn and mix with spices and butter.',
    'https://youtu.be/sF3droMGLlQ?si=48YA1p7LShw2U3GI',
    'https://png.pngtree.com/thumb_back/fw800/background/20240801/pngtree-indian-sweet-corn-chat-or-is-an-easy-to-make-snack-image_16122299.jpg',
    'sad'
),
(
    'Upma',
    'South Indian breakfast that gives warmth.',
    'Rava, Mustard, Curry leaves, Veggies',
    '220 kcal per bowl',
    'Cook rava with veggies and tempering.',
    'https://youtu.be/Fz20kYmUcuY?si=Ddq9pFgrVPSEGbA-',
    'https://tableandflavor.com/wp-content/uploads/2022/01/9795-upma-recipe-rava-upma-sooji-upma-recipe-by-tiffin-box-veg-upma-easy-healthy-breakfast-recipe.jpg',
    'sad'
),
(
    'Lemon Rice',
    'Tangy and light, good for emotional reset.',
    'Rice, Lemon, Spices, Mustard',
    '230 kcal per bowl',
    'Mix cooked rice with lemon and tempering.',
    'https://youtu.be/UgGinthI9NU?si=4AnB_IIiir7GGgpY',
    'https://www.cookwithmanali.com/wp-content/uploads/2016/01/South-Indian-Lemon-Rice-Recipe-500x500.jpg',
    'sad'
),
# Excited

    (
    'Ice Cream Sundae',
    'Sweet treat to uplift your spirit.',
    'Ice cream, chocolate syrup, nuts, cherry',
    '300 kcal per serving',
    'Scoop ice cream, top with syrup, nuts and cherry.',
    'https://www.youtube.com/embed/0zxvxrd1PDA',
    'https://media.istockphoto.com/id/471859630/photo/fancy-ice-cream-sundae-with-hot-fudge-sprinkles-cherries.jpg?s=612x612&w=0&k=20&c=MEaH7-Andg3bnzDVUCiCU5V5CUz6qjfu0xvR1vEepTE=',
    'excited'
),
(
    'Loaded Nachos',
    'Crispy, cheesy, spicy – a party in your mouth!',
    'Nachos, Cheese, Beans, Salsa',
    '450 kcal per plate',
    'Layer nachos, cheese, toppings and bake.',
    'https://youtu.be/ZKVYlS4QnEY?si=aI9jggoBh6WwLbHt',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGidHJmorXUrc4H_5NNZKcYbNoW05IPR53jA&s',
    'excited'
),
(
    'Chocolate Lava Cake',
    'Molten chocolate delight to celebrate anything.',
    'Chocolate, Butter, Eggs, Flour',
    '350 kcal per cake',
    'Bake cake with molten chocolate core.',
    'https://www.youtube.com/embed/1AP0HqG8JjU',
    'https://images.pexels.com/photos/5163948/pexels-photo-5163948.jpeg',
    'excited'
),
(
    'Tacos',
    'Flavor burst that matches your mood!',
    'Tortilla, Veggies/Meat, Cheese, Salsa',
    '300 kcal per serving',
    'Fill tortillas with toppings and serve warm.',
    'https://youtu.be/pvSL_VsLb4w?si=uus0boZdTRTWi4g9',
    'https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg',
    'excited'
),
(
    'Sizzling Brownie',
    'Chocolate fun with sizzling hot twist!',
    'Brownie, Ice Cream, Chocolate Sauce',
    '420 kcal per serving',
    'Heat brownie on sizzler plate, top with ice cream and sauce.',
    'https://youtu.be/ngDqanR_1iU?si=8qvPolDSyTdVE6_X',
    'https://images.pexels.com/photos/5386671/pexels-photo-5386671.jpeg',
    'excited'
),
(
    'Cheesy Quesadilla',
    'Exciting flavors and gooey cheese.',
    'Tortilla, Cheese, Peppers, Chicken/Paneer',
    '340 kcal per piece',
    'Grill tortilla with cheese and filling inside.',
    'https://youtu.be/AhoZ2TbLxzU?si=k0xOoPzUO4wlWxwH',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUTkX42CO0PXrVpxYThw9EFp7L7xlZ8AERu_Iy8g6BAlKubhITC5A5y5dJkyKiVed0HIE&usqp=CAU',
    'excited'
),
(
    'Spring Rolls',
    'Crispy bites perfect for celebration!',
    'Flour wrappers, Veggies, Soy sauce',
    '200 kcal per roll',
    'Wrap and deep-fry the fillings.',
    'https://www.youtube.com/embed/J9ytYe6EhvE',
    'https://c1.wallpaperflare.com/preview/564/844/49/nem-chinese-vegetables-chinese-cabbage.jpg',
    'excited'
),
(
    'Corn Cheese Balls',
    'Crispy outside, cheesy inside – pure joy!',
    'Corn, Cheese, Bread crumbs, Spices',
    '270 kcal per 4 balls',
    'Mix, roll and fry the cheese balls.',
    'https://youtu.be/4eoqzyeRvcw?si=Xj5XcmTJRS9s4V-q',
    'https://media.istockphoto.com/id/609932320/photo/fried-mac-and-cheese-balls-selective-focus.jpg?s=612x612&w=0&k=20&c=kuYowih6LnbXiIEgWQoXNU2ZcJrZEQP7w4Ck4WhwsK0=',
    'excited'
),
(
    'Strawberry Milkshake',
    'Sweet and refreshing drink for celebration.',
    'Strawberries, Milk, Sugar, Ice cream',
    '200 kcal per glass',
    'Blend all ingredients till smooth.',
    'https://youtu.be/JU-LFi7tD88?si=RXZ5ejjICXaHhLLM',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3hS2o-RKmvJnuo4o9PrED_agl21tt9_dylw&s',
    'excited'
),
(
    'Mini Pancakes',
    'Fun and cute food for high energy!',
    'Flour, Eggs, Milk, Maple Syrup',
    '180 kcal per 5 pancakes',
    'Cook small pancakes on griddle and serve with syrup.',
    'https://youtu.be/2TTy-Y3hudo?si=pjvFTMcSZ3iv6diA',
    'https://t4.ftcdn.net/jpg/14/56/29/97/360_F_1456299743_d69FzMZqgyQLO8Q62gOf9sQRdDP47SsZ.jpg',
    'excited'
),
(
    'Churros',
    'Crunchy, sweet, and playful snack!',
    'Flour, Cinnamon, Sugar, Butter',
    '300 kcal per 3 pieces',
    'Pipe and fry the dough, roll in cinnamon sugar.',
    'https://youtu.be/VYqoOiQsV0A?si=jpKRCWxtIdjcWmkP',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSF5uuOc2PEsUpoW621yrsduj2Ty4t6aMOvQ&s',
    'excited'
),
(
    'Fruit Trifle',
    'Colorful layers to match your happy vibe!',
    'Fruits, Custard, Cake, Cream',
    '250 kcal per bowl',
    'Layer all ingredients in a glass.',
    'https://youtu.be/9HQnA0j440o?si=a-2mdeda22_Sh8ex',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFm7q-rgAemws8Im0LLd2YUQxHtSEMkuHh74AlhuU4SAJdyaajxaY8183mJcPB_KaU5N8&usqp=CAU',
    'excited'
),
(
    'BBQ Wings',
    'Spicy and sticky – full of energy!',
    'Chicken Wings, BBQ Sauce, Garlic',
    '400 kcal per 6 wings',
    'Marinate and grill with BBQ sauce.',
    'https://youtu.be/9gwf7AWKpfM?si=qb-BPCILfe9JL-46',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfxsz93XWNdP0N_GiaQTfV8YvLECfLfma_eA&s',
    'excited'
),
(
    'Cold Coffee with Ice Cream',
    'A chilling twist to cool your excitement!',
    'Coffee, Milk, Sugar, Ice Cream',
    '190 kcal per glass',
    'Blend coffee with milk and top with ice cream.',
    'https://youtube.com/shorts/kX3XggZOfoI?si=Re6HJ_ztJetB4Upg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGKTCGZtG5JzzOJ6mpp67CLgyK8tvgX40zyQ&s',
    'excited'
),

    # TIRED
    # TIRED
(
    'Masala Chai & Biscuit',
    'Helps you relax and recharge your energy.',
    'Tea, Milk, Spices, Sugar, Biscuit',
    '120 kcal per cup',
    'Boil tea leaves with spices, strain, serve with biscuits.',
    'https://www.youtube.com/embed/2KI-PGM7PYQ',
    'https://images.pexels.com/photos/16942969/pexels-photo-16942969.jpeg?auto=compress&cs=tinysrgb&h=627&fit=crop&w=1200',
    'tired'
),
(
    'Khichdi',
    'Light and easy on the tummy, perfect after a long day.',
    'Rice, Lentils, Ghee, Spices',
    '250 kcal per bowl',
    'Cook rice and lentils together, temper with ghee.',
    'https://www.youtube.com/embed/N0vIGZWTnyg',
    'https://i.ytimg.com/vi/3v8bqzaMMZM/maxresdefault.jpg',
    'tired'
),
(
    'Vegetable Soup',
    'Nutritious and warm, relaxes your body.',
    'Mixed Veggies, Water, Spices',
    '150 kcal per bowl',
    'Boil veggies in seasoned broth.',
    'https://youtu.be/Q4kXLqUiSWI?si=pnqDzl1uxqiY4kWu',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVHqLsXM42ksRDrsgdvTfdQxvUJWFgDT4053CTU9-5xAhfYQJ-2opVIU9mQrVHzRjqUsM&usqp=CAU',
    'tired'
),
(
    'Banana Smoothie',
    'Boosts energy with natural sugars and potassium.',
    'Banana, Milk, Honey, Ice',
    '180 kcal per glass',
    'Blend all ingredients until smooth and creamy.',
    'https://youtu.be/7r6wdJI78OY?si=lhGGbuJuajkHIUUK',
    'https://media.istockphoto.com/id/522334972/photo/peanut-butter-banana-oat-smoothie-on-rustic-wood-with-scattered-ingredients.jpg?s=612x612&w=0&k=20&c=F_0O7J_x36jHY7-eVMYoOdjEMlnahMTH7_kDCXO6XUA=',
    'tired'
),
(
    'Avocado Toast',
    'Full of healthy fats to nourish a tired body.',
    'Bread, Avocado, Lemon, Salt',
    '250 kcal per slice',
    'Toast bread, mash avocado, season and serve.',
    'https://youtu.be/hIOadxvW0ys?si=wN2tBNCA3oucjCig',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiQASUS7-0oLSxUvHVay5hV2nc8COvcvQ5eeYSnu3wkmtCLbVF0HGASrQOQmQ_819XEAc&usqp=CAU',
    'tired'
),
(
    'Boiled Eggs',
    'Quick protein snack to fuel recovery.',
    'Eggs, Salt, Pepper',
    '78 kcal per egg',
    'Boil eggs, peel and season to taste.',
    'https://youtu.be/ORHEXhD84x0?si=cNAYu4V9qWwnGVaF',
    'https://media.istockphoto.com/id/520889612/photo/boiled-eggs-in-bowl.jpg?s=612x612&w=0&k=20&c=wwes11nnPnZu7IFz6SSSjhsfoBK-ZcTFsqH9Em72ClA=',
    'tired'
),
(
    'Oats Porridge',
    'Comforting and fibrous for a light recharge.',
    'Oats, Milk, Sugar/Honey',
    '200 kcal per bowl',
    'Cook oats in milk and sweeten to taste.',
    'https://youtu.be/GHVW9VzFz3w?si=UmzbMHrp55rlOKLI',
    'https://c4.wallpaperflare.com/wallpaper/677/138/554/honey-bananas-nuts-porridge-wallpaper-preview.jpg',
    'tired'
),
(
    'Upma',
    'Warm and filling, made with semolina and veggies.',
    'Rava (semolina), Veggies, Spices',
    '300 kcal per bowl',
    'Roast rava, cook with sautéed veggies and water.',
    'https://youtu.be/nb91xp4V4GQ?si=-kDuicj1alXLCfly',
    'https://t3.ftcdn.net/jpg/02/45/09/36/360_F_245093618_UBTNjpxMdMHR7Aup9SflZMxRikpxOpki.jpg',
    'tired'
),
(
    'Fruit Salad',
    'Refreshing and hydrating for a tired body.',
    'Mixed Fruits, Lemon Juice, Honey',
    '120 kcal per bowl',
    'Chop fruits, drizzle lemon juice and honey.',
    'https://youtu.be/3VbebGrgRWw?si=FCSqSpbl_WU21Seg',
    'https://t4.ftcdn.net/jpg/13/32/83/71/360_F_1332837182_WoUTxsopcxcEmEFINk1oIGMLXIy1bPP8.jpg',
    'tired'
),
(
    'Paneer Roll',
    'Protein-rich wrap to fuel you gently.',
    'Paneer, Roti, Veggies, Spices',
    '320 kcal per roll',
    'Cook paneer with spices, roll in roti with veggies.',
    'https://youtu.be/7_2BRFIms04?si=QRvqmQt-8W0dz782',
    'https://img.freepik.com/premium-photo/cottage-cheese-paneer-kathi-roll-wrap-also-known-as-kolkata-style-spring-rolls-vegetarians-indian-food_466689-52294.jpg',
    'tired'
)
]

c.executemany('''
    INSERT INTO suggestions (
        name, benefits, ingredients, calories, process, youtube_link, image, mood
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', data)

conn.commit()
conn.close()
print("✅ Food suggestions inserted into recommender.db.")
