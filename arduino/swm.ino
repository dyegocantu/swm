/* SWM - Sensor Web Monitor */

#include "DHT.h" // importa lib do sensor dht

#define DHTPIN 2 // pino do sensor
#define DHTTYPE DHT11 //  tipo de sensor

const int ID = 1; // identificador do dispositivo

DHT dht(DHTPIN, DHTTYPE); // objeto sensor dht
float humidity; // umidade
float temperature; // temperatura

void setup() 
{
  Serial.begin(115200); // inicia comunicacao serial
  dht.begin(); // inicia comunicacao com o sensor
}

void loop() 
{  
  humidity = dht.readHumidity(); // faz leitura de umidade
  temperature = dht.readTemperature(); // fz leitura de temperatura
  delay(1000); // pausa (tempo minimo nova leitura)
}

void serialEvent() // simula evento serial
{
  char cmd = (char)Serial.read(); // le caracter recebido pela serial
  
  if(cmd == '1') // se for um comando valido executa rotina
  {
      if(isnan(t) || isnan(h)) // verifica se houve erro na leitura
    {
      Serial.print("error");
    }
    else // se nao houve erro entao imprime os valores lidos
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
      Serial.println(); // tratar /r/n ao receber: ex. x = x.rstrip('\r\n')
    }
  }
}

