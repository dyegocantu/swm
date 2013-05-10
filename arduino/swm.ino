/* 
* SWM - Sensor Web Monitor
*
* DHT lib by AdaFruit:
* https://github.com/adafruit/DHT-sensor-library
*/

#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11

#define DELAY 1 // time to wait for next read
#define ID '1' // identification

DHT dht(DHTPIN, DHTTYPE); // create a sensor object
float humidity; 
float temperature;

void setup() 
{
  Serial.begin(115200);
  dht.begin(); // start the sensor
}

void loop() 
{  
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();
  // delay(DELAY); // not used
}

void serialEvent() // routine of serial event
{
  char receive = Serial.read();
  
  if(receive == ID) // was received the ID
  {
    if(isnan(temperature) || isnan(humidity)) // check error of read 
    {
      Serial.println("{\"error\": \"Failed to read from DHT\"}");
    }
    else
    {
      Serial.print("{");
      // Serial.print("\"id\": "); // not used
      // Serial.print(ID);
      // Serial.print(", ");
      Serial.print("\"humidity\": ");
      Serial.print(humidity);
      Serial.print(", "); 
      Serial.print("\"temperature\": ");
      Serial.print(temperature);
      Serial.print("}");
      Serial.println(); // treat to receive string /r/n. 
                        // eg. in python: x = x.rstrip('\r\n')
    }
  }
}

