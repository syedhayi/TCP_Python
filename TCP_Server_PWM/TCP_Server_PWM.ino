const int ledPin = 2; 
#include <ESP8266WiFi.h>
int dutyCycle;
int port = 8888;
WiFiServer server(port);
const char *ssid = "your SSID"; 
const char *password = "your password";


void setup() 
{
  Serial.begin(115200);  
  Serial.println();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password); //Connect to wifi
 
  // Wait for connection  
  Serial.println("Connecting to Wifi");
  while (WiFi.status() != WL_CONNECTED) {   
    delay(500);
    Serial.print(".");
    delay(500);
  }

  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  
  server.begin();
  Serial.print("connect to IP:");
  Serial.print(WiFi.localIP());
  Serial.print(" on port ");
  Serial.println(port);
}


void loop() 
{
  WiFiClient client = server.available();
  
  if (client) {
    if(client.connected())
    {
      Serial.println("Client Connected");
    }
    
    while(client.connected()){      
      while(client.available()>0){
        // read data from the connected client
        //Serial.write(client.read()); 
        dutyCycle = client.parseInt();
        Serial.println(dutyCycle);
        analogWrite(ledPin, dutyCycle);
      }
      
    }
    client.stop();   
  }
}
