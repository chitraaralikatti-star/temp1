import sys

def celsius_to_fahrenheit(celsius=25):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    if len(sys.argv) == 2:
        celsius = float(sys.argv[1])
    else:
        celsius = 25
        print("Arguments not provided - using default values")

    print("Celsius:", celsius)
    print("Fahrenheit:", celsius_to_fahrenheit(celsius))

