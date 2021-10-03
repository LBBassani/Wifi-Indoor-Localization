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
String response_header = "HTTP/1.1 200 OK\nContent-type:application/json\n\n";
String response;
String self_ip;

void setup() {
  
  // Iniciando comunicação serial
  Serial.begin(9600);

  // Inicializando WiFi da placa ESP32
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
   delay(500);
  }
  server.begin();

  self_ip = WiFi.localIP().toString();
  
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
            
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
        if (currentLine.endsWith("GET / ")){
          response = response_header + "{'networks':[";
          int n = WiFi.scanNetworks();

            if (n > 0) {
              for (int i = 0; i < n; ++i) {
                // Print SSID and RSSI for each network found
                String ssid = WiFi.SSID(i);
                int rssi = WiFi.RSSI(i);
                response += "{'SSID':'" + ssid + "','RSSI':" + String(rssi) + "},";
                delay(10);
              }
            }

          response += "]}";
          client.println(response);
        }
      }
    }
    client.stop();
  }
}
