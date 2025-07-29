from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = 'recommender.db'

# Dictionary mapping mood to recommended food
recommendations = {
    "happy": {"name": "Chicken Tikka", "image": "chicken_tikka.jpg"},
    "sad": {"name": "Hot Chocolate", "image": "chocolate.jpg"},
    "excited": {"name": "Ice Cream Sundae", "image": "ice_cream.jpg"},
    "tired": {"name": "Masala Chai & Biscuit", "image": "chai.jpg"}
}

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Function to fetch recommendation based on mood
def get_recommendation_based_on_mood(mood):
    return recommendations.get(mood, {"name": "Surprise Dish", "image": "default.jpg"})

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood']
    
    conn = sqlite3.connect('recommender.db')
    c = conn.cursor()
    
    # Get all 14 food items for the selected mood
    c.execute("SELECT name, image FROM suggestions WHERE mood = ?", (mood,))
    foods = c.fetchall()
    conn.close()

    return render_template('result.html', mood=mood, foods=foods)

# Food detail page route (from database)

@app.route('/food/<food>')
def food_detail(food):
    conn = sqlite3.connect("recommender.db")
    cur = conn.cursor()

    # Make query case-insensitive
    cur.execute("SELECT * FROM suggestions WHERE LOWER(name) = LOWER(?)", (food.lower(),))
    result = cur.fetchone()
    conn.close()

    if result:
        return render_template("food_detail.html", food=result)
    else:
        return render_template("food_detail.html", food=None, error="Food not found.")



@app.route('/result')
def result():
    mood = request.args.get('mood')
    
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    
    cur.execute("SELECT name, image FROM suggestions WHERE mood = ?", (mood,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        return render_template('result.html', mood=mood, food_items=[], background_image="default.jpg")

    return render_template('result.html', mood=mood, food_items=rows, background_image="bg.jpg")


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
