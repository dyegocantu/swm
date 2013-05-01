/* 
* SWM - Sensor Web Monitor
*
* DHT lib by AdaFruit:
* https://github.com/adafruit/DHT-sensor-library
*/

#include "DHT.h" // import the sensor lib

#define DHTPIN 2 // define the sensor pin
#define DHTTYPE DHT11 // define the sensor type

#define ID '1' // identification of thing (arduino)

DHT dht(DHTPIN, DHTTYPE); // create a sensor object
float humidity; 
float temperature;

void setup() 
{
  Serial.begin(115200); // starts the serial communication
  dht.begin(); // starts the sensor
}

void loop() 
{  
  humidity = dht.readHumidity(); // reads the humidity
  temperature = dht.readTemperature(); // reads the temperature
  delay(1000); // delay for next read
}

void serialEvent() // routine of serial event
{
  char receive = (char)Serial.read(); // reads a serial character
  
  if(receive == ID) // was received the ID
  {
    if(isnan(temperature) || isnan(humidity)) // check error of read 
    {
      Serial.print("error"); // sends a error message
    }
    else // was not error
    {
      Serial.print("{");
      Serial.print("\"id\":");
      Serial.print(ID);
      Serial.print(",");
      Serial.print("\"humidity\":");
      Serial.print(humidity);
      Serial.print(","); 
      Serial.print("\"temperature\":");
      Serial.print(temperature);
      Serial.print("}");
      Serial.println(); // treat to receive string /r/n. 
                        // eg. in python: x = x.rstrip('\r\n')
    }
  }
}

