import random

# CHC-275 Semester Project: Tropical Island Weather App
# Author: [Your Name]
# Description: This program tells the weather on a tropical island based on the condition of a rock.
# Beginner-friendly version using Python basics.

# -----------------------------
# Step 1: Import necessary modules
# -----------------------------
import time
import random

# -----------------------------
# Step 2: Define weather and rock conditions
# -----------------------------
weather_conditions = [
    "sunny", "rain", "snow", "hurricane", "cloudy", "stormy",
    "foggy", "eclipse", "tsunami"
]

rock_conditions = [
    "wet", "dry", "white", "gone", "green",
    "darker than usual", "blurry", "black", "underwater"
]

# -----------------------------
# Step 3: Session weather history
# -----------------------------
weather_history = []

# -----------------------------
# Step 4: Define function to read rock condition from file
# -----------------------------
def read_rock_condition(filename):
    try:
        with open(filename, "r") as file:
            rocks = file.readlines()
            rocks = [rock.strip() for rock in rocks if rock.strip() != ""]
            if len(rocks) == 0:
                print("File is empty. Using random rock.")
                return [random.choice(rock_conditions)]
            return rocks
    except FileNotFoundError:
        print("Rock condition file not found. Using random rock condition.")
        return [random.choice(rock_conditions)]

# -----------------------------
# Step 5: Determine weather from the rock
# -----------------------------
def determine_weather(rock):
    if rock == "wet":
        return "It is raining on the island."
    elif rock == "dry":
        return "The sun is shining brightly."
    elif rock == "white":
        return "It is snowing on the island! Surprising for a tropical island!"
    elif rock == "gone":
        return "A hurricane is approaching! Take cover!"
    elif rock == "green":
        return "The weather is calm and cloudy."
    elif rock == "darker than usual":
        return "It is cloudy; the sky is darker than usual."
    elif rock == "blurry":
        return "It is foggy outside; visibility is low."
    elif rock == "black":
        return "An eclipse is happening! Look carefully."
    elif rock == "underwater":
        return "A tsunami is approaching! Stay safe!"
    else:
        return "The rock is mysterious... Weather cannot be determined."

# -----------------------------
# Step 6: Display menu
# -----------------------------
def display_menu():
    print("\nWelcome to the Tropical Island Weather App!")
    print("1. Check weather using rock condition file")
    print("2. Check weather manually")
    print("3. View weather history")
    print("4. Exit app")

# -----------------------------
# Step 7: Function to get manual rock input
# -----------------------------
def manual_rock_input():
    print("\nChoose the rock condition from the list:")
    for i, condition in enumerate(rock_conditions):
        print(f"{i + 1}. {condition}")
    choice = input("Enter the number of the rock condition: ")
    
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(rock_conditions):
            return rock_conditions[index]
        else:
            print("Invalid number. Choosing random rock condition.")
            return random.choice(rock_conditions)
    else:
        print("Invalid input. Choosing random rock condition.")
        return random.choice(rock_conditions)

# -----------------------------
# Step 8: emojis for weather
# -----------------------------
def weather_ascii(weather):
    if "rain" in weather:
        print("☔☔☔ It's raining! ☔☔☔")
    elif "sun" in weather:
        print("☀️☀️☀️ Sunny day! ☀️☀️☀️")
    elif "snow" in weather:
        print("❄️❄️❄️ Snowing! ❄️❄️❄️")
    elif "hurricane" in weather:
        print("🌪️🌪️🌪️ Hurricane alert! 🌪️🌪️🌪️")
    elif "cloudy" in weather:
        print("☁️☁️☁️ Cloudy skies ☁️☁️☁️")
    elif "storm" in weather:
        print("⚡⚡⚡ Stormy weather! ⚡⚡⚡")
    elif "foggy" in weather:
        print("🌫️🌫️🌫️ Foggy conditions! 🌫️🌫️🌫️")
    elif "eclipse" in weather:
        print("🌑🌑🌑 Eclipse happening! 🌑🌑🌑")
    elif "tsunami" in weather:
        print("🌊🌊🌊 Tsunami alert! 🌊🌊🌊")
    else:
        print("The weather is unusual today.")

# -----------------------------
# Step 9: Random events
# -----------------------------
def random_event():
    events = [
        "A seagull lands on the rock!",
        "A sudden gust of wind blows by!",
        "You hear waves crashing nearby.",
        "A palm tree shakes in the breeze.",
        "A coconut falls near your feet!"
    ]
    print(random.choice(events))

# -----------------------------
# Step 10: Main program loop
# -----------------------------
def main():
    while True:
        display_menu()
        option = input("\nEnter your choice: ")

        if option == "1":
            filename = input("Enter the rock condition filename (e.g., rock.txt): ")
            rocks = read_rock_condition(filename)
            for rock in rocks:
                print(f"\nRock condition: {rock}")
                weather = determine_weather(rock)
                print(weather)
                weather_ascii(weather)
                weather_history.append(f"Rock: {rock} -> {weather}")
                random_event()
                time.sleep(2)
        elif option == "2":
            rock = manual_rock_input()
            print(f"\nRock condition: {rock}")
            weather = determine_weather(rock)
            print(weather)
            weather_ascii(weather)
            weather_history.append(f"Rock: {rock} -> {weather}")
            random_event()
            time.sleep(2)
        elif option == "3":
            print("\n--- Weather History ---")
            if len(weather_history) == 0:
                print("No weather data yet.")
            else:
                for record in weather_history:
                    print(record)
        elif option == "4":
            print("\nThank you for using the Tropical Island Weather App!")
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            time.sleep(1)

# -----------------------------
# Step 11: Run the app
# -----------------------------
if __name__ == "__main__":
    print("Loading Tropical Island Weather App...")
    time.sleep(1)
    main()
