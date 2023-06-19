#include <Arduino.h>
#include <WiFi.h>

const char* ssid = "Joao";
const char* password = "123456789";

WiFiServer server(80);
String header;
String output26State = "off";
String output27State = "off";
const int output26 = 26;
const int output27 = 27;
const int pinoLDR = 33;
unsigned long currentTime = millis();
unsigned long previousTime = 0;
const long timeoutTime = 2000;
int valorLDR = 0;

void handleLDRRequest(WiFiClient client);

void setup() {
  Serial.begin(115200);

  pinMode(output26, OUTPUT);
  pinMode(output27, OUTPUT);
  pinMode(pinoLDR, INPUT);
  digitalWrite(output26, LOW);
  digitalWrite(output27, LOW);

  WiFi.begin(ssid, password);
  Serial.print("Connecting to ");
  Serial.println(ssid);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    currentTime = millis();
    previousTime = currentTime;
    Serial.println("New Client.");
    String currentLine = "";

    while (client.connected() && currentTime - previousTime <= timeoutTime) {
      currentTime = millis();

      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        header += c;

        if (c == '\n') {

          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();

            if (header.indexOf("GET /26/on") >= 0) {
              Serial.println("GPIO 26 on");
              output26State = "on";
              digitalWrite(output26, HIGH);
            } else if (header.indexOf("GET /26/off") >= 0) {
              Serial.println("GPIO 26 off");
              output26State = "off";
              digitalWrite(output26, LOW);
            } else if (header.indexOf("GET /27/on") >= 0) {
              Serial.println("GPIO 27 on");
              output27State = "on";
              digitalWrite(output27, HIGH);
            } else if (header.indexOf("GET /27/off") >= 0) {
              Serial.println("GPIO 27 off");
              output27State = "off";
              digitalWrite(output27, LOW);
            } else if (header.indexOf("GET /ldr") >= 0) {
              handleLDRRequest(client);
            }

            client.println("<!DOCTYPE html><html>");
            client.println("<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">");
            client.println("<style>");
            client.println("body { background-color: #f2f2f2; font-family: Arial, Helvetica, sans-serif; text-align: center; }");
            client.println("h1 { color: #0066cc; }");
            client.println("h2 { color: #0099ff; }");
            client.println(".container { max-width: 400px; margin: 0 auto; padding: 20px; background-color: #ffffff; border-radius: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); }");
            client.println(".button { display: inline-block; background-color: #4CAF50; color: #ffffff; padding: 10px 20px; text-decoration: none; border-radius: 4px; font-size: 16px; margin: 10px; cursor: pointer; }");
            client.println(".button-red { background-color: #ff3300; }");
            client.println(".button-blue { background-color: #2196F3; }");
            client.println(".ldr-value { font-size: 24px; margin-bottom: 20px; }");
            client.println(".footer { font-size: 12px; color: #888888; margin-top: 20px; }");
            client.println("</style>");
            client.println("</head>");
            client.println("<body>");
            client.println("<div class=\"container\">");
            client.println("<h1>Trabalho Sistemas Digitais - IOT</h1>");

            client.println("<h2>GPIO 26</h2>");
            client.println("<p>State: " + output26State + "</p>");
            if (output26State == "off") {
              client.println("<a href=\"/26/on\"><button class=\"button\">Turn On</button></a>");
            } else {
              client.println("<a href=\"/26/off\"><button class=\"button button-red\">Turn Off</button></a>");
            }

            client.println("<h2>GPIO 27</h2>");
            client.println("<p>State: " + output27State + "</p>");
            if (output27State == "off") {
              client.println("<a href=\"/27/on\"><button class=\"button\">Turn On</button></a>");
            } else {
              client.println("<a href=\"/27/off\"><button class=\"button button-red\">Turn Off</button></a>");
            }

            client.println("<h2>Sensor de Luminosidade: LDR</h2>");
            client.println("<p class=\"ldr-value\">Valor LDR: " + String(valorLDR) + "</p>");
            client.println("<a href=\"/ldr\"><button class=\"button button-blue\">Atualizar Valor do LDR</button></a>");

            

            client.println("</div>");
            client.println("</body></html>");
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }

    header = "";
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }
}

void handleLDRRequest(WiFiClient client) {
  valorLDR = analogRead(pinoLDR);
  client.print(String(valorLDR));
}

