# Growfinix Internship – Task 5
## External API Consumer – Weather Application

### Project Overview

This project is developed as part of the Python Development Internship at Growfinix Technology.

The Weather Application is a Python-based program that connects to external weather APIs to retrieve and display current weather information for a user-entered city.

### Objectives

- Connect Python applications with external APIs.
- Retrieve weather information using HTTP requests.
- Process JSON responses.
- Display weather information in a structured format.
- Handle API and network errors.

### Technologies Used

- Python
- Requests Library
- JSON
- Open-Meteo API
- Visual Studio Code

### Features

1. City Search – Search weather information using a city name.
2. Temperature – Display current temperature in Celsius.
3. Humidity – Display relative humidity percentage.
4. Wind Speed – Display current wind speed.
5. Weather Description – Display weather conditions.
6. Error Handling – Handle network errors and invalid city names.

### APIs Used

- Open-Meteo Geocoding API
- Open-Meteo Forecast API

### Installation

Install the required Python library:

```bash
python -m pip install requests
```

### How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Execute:

```bash
python main.py
```

4. Enter a city name when prompted.

### Sample Output

```text
GROWFINIX WEATHER APPLICATION

Enter city name: Trichy

City          : Trichy
Country       : India
Temperature   : 25.6 °C
Humidity      : 82 %
Wind Speed    : 10.7 km/h
Weather       : Partly cloudy

WEATHER FETCH SUCCESSFUL
```

*Note: Sample values are illustrative. Actual results depend on the API response.*

### Learning Outcomes

- Understanding external APIs.
- Making HTTP requests using Python.
- Working with JSON data.
- Using Python functions.
- Handling exceptions.
- Extracting information from API responses.

### Internship Information

**Organization:** Growfinix Technology

**Domain:** Python Development

**Task:** Task 5 – External API Consumer

### Conclusion

This project demonstrates how Python can communicate with external APIs and retrieve useful real-world information through HTTP requests and JSON processing.

Developed as part of the Growfinix Python Development Internship.
