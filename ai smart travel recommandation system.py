print("="*60)
print("      🌍 AI SMART TRAVEL RECOMMENDATION SYSTEM 🌍")
print("="*60)

# -------------------------------
# Travel Database
# -------------------------------

destinations = [
    {
        "name": "Goa",
        "budget": "Low",
        "climate": "Warm",
        "purpose": "Relaxation",
        "days": "3-5",
        "activities": ["Beach", "Nightlife", "Water Sports"]
    },
    {
        "name": "Manali",
        "budget": "Medium",
        "climate": "Cold",
        "purpose": "Adventure",
        "days": "5-7",
        "activities": ["Snow", "Trekking", "Camping"]
    },
    {
        "name": "Jaipur",
        "budget": "Medium",
        "climate": "Warm",
        "purpose": "Historical",
        "days": "2-4",
        "activities": ["Forts", "Palaces", "Shopping"]
    },
    {
        "name": "Kerala",
        "budget": "High",
        "climate": "Warm",
        "purpose": "Relaxation",
        "days": "5-7",
        "activities": ["Backwaters", "Nature", "Houseboat"]
    },
    {
        "name": "Ladakh",
        "budget": "High",
        "climate": "Cold",
        "purpose": "Adventure",
        "days": "7+",
        "activities": ["Mountains", "Bike Ride", "Camping"]
    },
    {
        "name": "Varanasi",
        "budget": "Low",
        "climate": "Warm",
        "purpose": "Spiritual",
        "days": "2-3",
        "activities": ["Temples", "Ganga Aarti", "Culture"]
    },
    {
        "name": "Andaman",
        "budget": "High",
        "climate": "Warm",
        "purpose": "Relaxation",
        "days": "5-7",
        "activities": ["Beach", "Scuba Diving", "Snorkeling"]
    },
    {
        "name": "Mysore",
        "budget": "Medium",
        "climate": "Pleasant",
        "purpose": "Historical",
        "days": "2-4",
        "activities": ["Palace", "Zoo", "Gardens"]
    }
]

# -------------------------------
# User Inputs
# -------------------------------

print("\nAnswer the following questions.\n")

budget = input("Budget (Low(below 30k)/Medium(above 30k)/High(above 50k)): ").title()

climate = input("Preferred Climate (Warm/Cold/Pleasant): ").title()

purpose = input("Purpose (Adventure/Relaxation/Historical/Spiritual): ").title()

days = input("Trip Duration (2-3 / 2-4 / 3-5 / 5-7 / 7+): ")

activity = input("Favorite Activity: ").title()

print("\nFinding the best destination...\n")

# -------------------------------
# Recommendation Logic
# -------------------------------

results = []

budget_order = {
    "Low":1,
    "Medium":2,
    "High":3
}

for place in destinations:

    score = 0

    # Budget Matching
    if budget == place["budget"]:
        score += 3
    else:
        if abs(budget_order[budget]-budget_order[place["budget"]]) == 1:
            score += 2
        else:
            score += 1

    # Climate
    if climate == place["climate"]:
        score += 3

    # Purpose
    if purpose == place["purpose"]:
        score += 4

    # Days
    if days == place["days"]:
        score += 2

    # Activity
    if activity in place["activities"]:
        score += 5

    results.append((score, place))

# -------------------------------
# Sort Results
# -------------------------------

results.sort(reverse=True, key=lambda x:x[0])

print("="*60)
print("✨ TOP TRAVEL RECOMMENDATIONS ✨")
print("="*60)

for score, place in results[:3]:

    print("\nDestination :", place["name"])
    print("Match Score :", score,"/17")
    print("Budget      :", place["budget"])
    print("Climate     :", place["climate"])
    print("Purpose     :", place["purpose"])
    print("Trip Days   :", place["days"])
    print("Activities  :", ", ".join(place["activities"]))

print("\nThank you for using the AI Smart Travel Recommendation System!")