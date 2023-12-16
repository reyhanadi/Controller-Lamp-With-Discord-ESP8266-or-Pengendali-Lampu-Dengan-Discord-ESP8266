#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char *ssid = "your ssid";
const char *password = "your password wifi/hotspot";

// Deklarasikan pin relay sesuai dengan koneksi pada NodeMCU
const int lampu1Pin = 5;  // GPIO 5
const int lampu2Pin = 4;  // GPIO 4

ESP8266WebServer server(80);

void setup() {
  Serial.begin(115200);

  // Hubungkan ke WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  // Dapatkan dan cetak alamat IP lokal
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Konfigurasi pin relay
  pinMode(lampu1Pin, OUTPUT);
  pinMode(lampu2Pin, OUTPUT);

  // Tentukan penangan HTTP untuk menghidupkan/mematikan lampu 1
server.on("/lamp1_on", HTTP_GET, []() {
  digitalWrite(lampu1Pin, LOW);  // Ubah menjadi LOW untuk menyalakan
  server.send(200, "text/html", "Lampu 1 dihidupkan");
});

server.on("/lamp1_off", HTTP_GET, []() {
  digitalWrite(lampu1Pin, HIGH);   // Ubah menjadi HIGH untuk mematikan
  server.send(200, "text/html", "Lampu 1 dimatikan");
});

// Tentukan penangan HTTP untuk menghidupkan/mematikan lampu 2
server.on("/lamp2_on", HTTP_GET, []() {
  digitalWrite(lampu2Pin, LOW);  // Ubah menjadi LOW untuk menyalakan
  server.send(200, "text/html", "Lampu 2 dihidupkan");
});

server.on("/lamp2_off", HTTP_GET, []() {
  digitalWrite(lampu2Pin, HIGH);   // Ubah menjadi HIGH untuk mematikan
  server.send(200, "text/html", "Lampu 2 dimatikan");
});

  // Mulai server
  server.begin();
}

void loop() {
  server.handleClient();
}
