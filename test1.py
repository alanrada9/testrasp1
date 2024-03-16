import Adafruit_DHT
import Adafruit_CharLCD as LCD
import time

# Initialize DHT sensor (DHT22) and LCD display (16x2)
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

LCD_RS = 21
LCD_EN = 20
LCD_D4 = 16
LCD_D5 = 12
LCD_D6 = 7
LCD_D7 = 8
LCD_COLS = 16
LCD_ROWS = 2

lcd = LCD.Adafruit_CharLCD(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7, LCD_COLS, LCD_ROWS)

def read_dht_sensor()
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

def read_light_status()
    # Placeholder function to simulate reading LDR
    # Replace this with your actual LDR reading code
    return Light Detected if True else No Light

try
    while True
        humidity, temperature = read_dht_sensor()
        light_status = read_light_status()

        # Display results on the console
        print(fTemperature {temperature.2f}°C, Humidity {humidity.2f}%)
        print(fLight Status {light_status})

        # Display results on the LCD
        lcd.clear()
        lcd.message(fTemp {temperature.1f}CnHumidity {humidity.1f}%n{light_status})
        
        time.sleep(2)  # Wait for 2 seconds before updating readings

except KeyboardInterrupt
    print(Exiting...)

finally
    lcd.clear()
    lcd.message(Goodbye!)
    time.sleep(2)
    lcd.clear()
