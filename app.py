from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------
# Sample Destination Database
# (In real project this comes from PostgreSQL / MongoDB)
# ------------------------------

destinations = {
    "goa": {
        "daily_budget": 3000,
        "highlights": ["Baga Beach", "Fort Aguada", "Calangute Beach"],
        "tips": "Best time to visit: November to February"
    },
    "manali": {
        "daily_budget": 2500,
        "highlights": ["Solang Valley", "Rohtang Pass", "Hadimba Temple"],
        "tips": "Carry warm clothes year-round"
    },
    "jaipur": {
        "daily_budget": 2000,
        "highlights": ["Hawa Mahal", "Amber Fort", "City Palace"],
        "tips": "Visit forts early morning to avoid heat"
    }
}

# ------------------------------
# Home Route
# ------------------------------

@app.route("/")
def home():
    return "🌍 AI Travel Recommendation System is Running!"

# ------------------------------
# Itinerary Generator
# ------------------------------

@app.route("/generate-itinerary", methods=["POST"])
def generate_itinerary():
    data = request.json
    
    destination = data.get("destination", "").lower()
    days = int(data.get("days", 1))
    budget = int(data.get("budget", 0))
    
    if destination not in destinations:
        return jsonify({"error": "Destination not found"}), 404
    
    place = destinations[destination]
    
    estimated_cost = place["daily_budget"] * days
    
    itinerary = {
        "destination": destination.title(),
        "days": days,
        "suggested_places": place["highlights"],
        "local_tips": place["tips"],
        "estimated_cost": estimated_cost,
        "budget_status": "Within Budget ✅" if estimated_cost <= budget else "Budget Exceeded ⚠️"
    }
    
    return jsonify(itinerary)

# ------------------------------
# Budget Calculator
# ------------------------------

@app.route("/calculate-budget", methods=["POST"])
def calculate_budget():
    data = request.json
    
    accommodation = int(data.get("accommodation", 0))
    food = int(data.get("food", 0))
    transport = int(data.get("transport", 0))
    activities = int(data.get("activities", 0))
    
    total = accommodation + food + transport + activities
    
    return jsonify({
        "total_trip_cost": total
    })

# ------------------------------
# Run Application
# ------------------------------

if __name__ == "__main__":
    app.run(debug=True)
