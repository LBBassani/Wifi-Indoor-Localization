/* Código de servidor Wi-Fi ESP32 para mapear a intensidade das redes Wi-Fi disponíveis
 * @author: Lorena Bassani
 * @date: October 2021
 * @version: 1.0
 * @descrição:  Baseado nos tutoriais 
 *                  - "ESP32 WIFI: COMUNICAÇÃO COM A INTERNET" por Gustavo Teixeira. Acesso https://www.usinainfo.com.br/blog/esp32-wifi-comunicacao-com-a-internet/ em 29/07/2021.
 *                  - "ESP32 Useful Wi-Fi Library Functions (Arduino IDE)" in randomnerdtutorials. Acesso https://randomnerdtutorials.com/esp32-useful-wi-fi-functions-arduino/ em 01/10/2021.
 *                
 *                Estudo de indoor localization (localização em ambientes internos) utilizando a tecnologia wi-fi. Este código realiza a leitura das redes disponíveis e mostra a intensidade do sinal
 *                em uma página web. Este código se conecta a uma rede.
 *              
 *                Versão mais recente disponível em https://github.com/LBBassani/Wifi-Indoor-Localization.
 */

#include <WiFi.h>

// Informações do servidor wi-fi
const char* ssid = "lorena-notebook";
const char* password = "ultrabots";
WiFiServer server(80);

// Variáveis de resposta do servidor
String texto = "HTTP/1.1 200 OK\nContent-type:text/html\n\n";
String responses;

void setup() {

  // Construção do texto base da página HTML renderizda pelo servidor
  texto += "Redes Wi-fi";
  texto += "<hr>Click <a href=\"/CLEAR\">here</a> to clear responses.<br><br>";
  
  // Iniciando comunicação serial
  Serial.begin(9600);

  // Inicializando WiFi da placa ESP32
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
   delay(500);
  }
  server.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  WiFiClient client = server.available();
  if (client) {

    String currentLine = "";
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println(texto);

            // WiFi.scanNetworks will return the number of networks found
            int n = WiFi.scanNetworks();

            if (n == 0) {
                responses += "no networks found<br>";
            } else {
                responses += String(n) + " networks found<br>";
              for (int i = 0; i < n; ++i) {
                // Print SSID and RSSI for each network found
                String ssid = WiFi.SSID(i);
                int rssi = WiFi.RSSI(i);
                responses += String(i + 1) + ": " + ssid + " (" + String(rssi) + ")<br>";
                delay(10);
              }
            }
              client.println(responses);
           
            
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
        if (currentLine.endsWith("GET /CLEAR")){
          responses = String();
        }
      }
    }
    client.stop();
  }
}
