def celsius_to_fahrenheit(celsius=25):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
if __name__ == "__main__":
    celsius_value = 25   # default temperature
    result = celsius_to_fahrenheit(celsius_value)
    print("Temperature in Celsius:", celsius_value)
    print("Temperature in Fahrenheit:", result)

