# Task 1: Designing the Book Module

# Create a module for managing book-related 
# functionalities. This includes classes and functions for 
# book attributes, book availability, and any other book-specific operations.

# Problem Statement:

# The bookstore system requires a dedicated module for handling 
# various aspects related to books, such as title, author, price, and stock status.

from book import Book

library = []
addAnother = 1

while addAnother == 1:
    title = input("ENTER TITLE: ")
    author = input("ENTER AUTHOR: ")
    price = float(input("ENTER PRICE: "))
    volume = input("ENTER VOLUME: ")
    stock = int(input("ENTER STOCK: "))

    newBook = Book(title, author, price, volume, stock)
    print("\nBOOK INFORMATION ADDED: \n")
    newBook.displayInfo(title, author, price, volume, stock)
    library.append(newBook)

    addAnother = int(input("\nUPDATE BOOK INFO, PRESS 1. To quit, press -99: "))
print()   
print("*********AVAILABLE BOOKS*********\n")
for book in library:
    newBook.displayInfo(title, author, price, volume, stock) 
    print()

bookTitle = input("ENTER TITLE OF BOOK TO UPDATE STOCK: ")
for book in library:
    if book.title.lower() == bookTitle.lower():
        updateStock = int(input("ENTER STOCK NUMBER: "))
        book.updateStock(updateStock)
        break
else:
    print("BOOK NOT FOUND!")

# Task 1: Identifying and Creating Classes

# Analyze the provided script and identify distinct functionalities
# that can be encapsulated into classes. Create classes that represent 
# different aspects of the weather forecast application, such as 
# fetching data, parsing data, and user interaction.

# Problem Statement:

# The existing script for the weather forecast application 
# is written in a procedural style and lacks organization.

class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"city": "New York", "temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"city": "London", "temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"city": "Tokyo", "temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city.title(), {})

class WeatherDataParser:
    @staticmethod
    def parse_weather_data(data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:
    def get_user_input(self):
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        return city.lower()

    def get_detailed_forecast_preference(self):
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        return detailed == 'yes'

def main():
    ui = UserInterface()
    weather_fetcher = WeatherDataFetcher()
    
    while True:
        city = ui.get_user_input()
        if city == 'exit':
            break
        detailed = ui.get_detailed_forecast_preference()
        data = weather_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            if detailed:
                forecast = WeatherDataParser.parse_weather_data(data)
            else:
                forecast = f"Weather in {city}: {data['temperature']} degrees, {data['condition']}"
            print(forecast)

if __name__ == "__main__":
    main()

