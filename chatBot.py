import requests
import random
import tkinter as tk
import random

name = "Osos"
age = 21
religion = "Muslim"
interests = "geography"

def get_country_info(country):
    url = f"https://restcountries.com/v3/name/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        info = {
            "capital": data.get("capital", ""),
            "lat": data.get("latlng", [])[0],
            "lng": data.get("latlng", [])[1],
            "region": data.get("region", ""),
            "population": data.get("population", ""),
            "area": data.get("area", ""),
            "timezones": ", ".join(data.get("timezones", [])),
            "borders": ", ".join(data.get("borders", []))
        }
        return info
    else:
        return None

# Define some personality for the chatbot
greetings = ["Hi there!", "Hello!", "Hey!", "Greetings!", "Nice to meet you!"]
unknown_responses = ["I'm sorry, I don't understand the question.", "Could you rephrase that?", "I'm not sure what you're asking."]
positive_responses = ["Great question!", "Interesting!", "I love talking about this stuff!", "Fascinating!", "Wow, I'm learning so much!"]
personality_responses = [f"My name is {name}. I'm {age} years old and {religion}. I love talking about {interests}.",
                         f"I'm {name}. I'm {age} years old and {religion}. Geography is one of my favorite topics.",
                         f"{name} here! I'm {age} years old and {religion}. Ask me anything about geography!"]

def generate_response(question):
    if any(word in question for word in ["hi", "hello", "hey"]):
        return random.choice(greetings) + " How can I help you today?"
    elif "what is your name?" in question:
        return "My name is Osos. Nice to meet you!"
    elif "how old are you?" in question:
        return "I am 21 years old."
    elif any(word in question for word in ["what's your religion?", "what do you believe in?"]):
        return "I am Muslim and I believe in God."
    elif "what do you like?" in question:
        return "I like geography and learning about different countries."
    elif"how can you help me?"in question:
        return"I can help you to know the capitals of countries and their coordinates and some other geographical information"
    elif "?" in question:
        if "capital" in question:
          last_word = question.split()[-1]
          country = last_word[:-1]
          country_info = get_country_info(country)
          if country_info:
            return f"{country_info['capital'][0]}. " + random.choice(positive_responses)

          else:
                return random.choice(unknown_responses)
        elif "coordinates" in question:
            last_word = question.split()[-1]
            country = last_word[:-1]
            country_info = get_country_info(country)
            if country_info:
                return f"The coordinates of {country} are ({country_info['lat']}, {country_info['lng']}). " + random.choice(positive_responses)
            else:
                return random.choice(unknown_responses)
        elif "region" in question:
            last_word = question.split()[-1]
            country = last_word[:-1]
            country_info = get_country_info(country)
            if country_info:
                return f"{country} is located in the {country_info['region']} region. " + random.choice(positive_responses)
            else:
                return random.choice(unknown_responses)
        elif "population" in question:
            last_word = question.split()[-1]
            country = last_word[:-1]
            country_info = get_country_info(country)
            if country_info:
                return f"The population of {country} is {country_info['population']}. " + random.choice(positive_responses)
            else:
                return random.choice(unknown_responses)
        elif "area" in question:
            last_word = question.split()[-1]
            country = last_word[:-1]
            country_info = get_country_info(country)
            if country_info:
                return f"{country} has an area of {country_info['area']} sq. km. " + random.choice(positive_responses)
            else:
                return random.choice(unknown_responses)
        elif "time zone" in question:
            last_word = question.split()[-1]
            country = last_word[:-1]
            country_info = get_country_info(country)
            if country_info:
                return f"{country} time zone is {country_info['timezones']}. " + random.choice(positive_responses)
            else:
                return random.choice(unknown_responses)
        elif"border"in question:
            last_word = question.split()[-1]
            country = last_word[:-1]
            country_info = get_country_info(country)
            if country_info and country_info['borders']:
                return f"{country} borders {country_info['borders']}."
            else:
                return f"{country} does not share a border with any other country."+random.choice(unknown_responses)
            
        elif "information" in question:
            last_word = question.split()[-1]
            country = last_word[:-1]
            country_info = get_country_info(country)
            if country_info:
                
                info_str = f"{country_info['capital'][0]} is the capital.\n"
                info_str += f"Population: {country_info['population']}\n"
                info_str += (f"{country} borders {country_info['borders']}.\n" if country_info and country_info['borders'] else f"{country} does not share a border with any other country.")
                info_str += f"Area: {country_info['area']}\n"
             
                # add more info as needed
                return info_str             
            else:
                print(f"Sorry, I don't have information about {country}.")    
        else:
            return random.choice(unknown_responses)
        
    else:
        return random.choice(unknown_responses)


BACKGROUND_COLOR = "#f2f2f2"
TEXTBOX_COLOR = "#ffffff"
BUTTON_COLOR = "#4caf50"
BUTTON_HOVER_COLOR = "#388e3c"

def handle_input():
    user_input = entry_field.get()
    conversation_history.insert(tk.END, "You: " + user_input + "\n")
    bot_response = generate_response(user_input)
    conversation_history.insert(tk.END, "Bot: " + bot_response + "\n\n")
    conversation_history.see(tk.END)
    entry_field.delete(0, tk.END)

window = tk.Tk()
window.title("Chatbot")
window.configure(bg=BACKGROUND_COLOR)

conversation_history = tk.Text(window, height=20, width=50, font=("Arial", 12), bg=TEXTBOX_COLOR)
conversation_history.pack(side=tk.BOTTOM, fill=tk.X)

scrollbar = tk.Scrollbar(window, command=conversation_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
conversation_history.config(yscrollcommand=scrollbar.set)

entry_field = tk.Entry(window, font=("Arial", 12), bg=TEXTBOX_COLOR)
entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button = tk.Button(window, text="Send", font=("Arial", 16), bg=BUTTON_COLOR, activebackground=BUTTON_HOVER_COLOR, command=handle_input)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

window.mainloop()
