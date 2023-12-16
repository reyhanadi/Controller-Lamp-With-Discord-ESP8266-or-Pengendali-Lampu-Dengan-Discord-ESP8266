# Controller-Lamp-With-Discord-ESP8266-or-Pengendali-Lampu-Dengan-Discord-ESP8266
Prototype Number V-001 Discord Controller Lamp

Instalasi dan Penggunaan Bot Discord dengan NodeMCU (Arduino)
Langkah-langkah Instalasi:

Persiapkan NodeMCU:

Hubungkan NodeMCU ke komputer dan pastikan telah menginstal Arduino IDE serta mengonfigurasi pengaturan ESP8266 pada Arduino IDE.
Unduh Libraries yang Diperlukan:

Pastikan telah mengunduh dan menginstal dua library Arduino: ESP8266WiFi dan ESP8266WebServer. Anda dapat mengunduhnya melalui Arduino Library Manager.
Atur Koneksi WiFi pada NodeMCU:

Isi SSID dan password WiFi pada bagian const char *ssid dan const char *password sesuai dengan koneksi WiFi yang akan digunakan.
Definisikan Pin Relay:

Sesuaikan pin relay pada NodeMCU dengan mengganti nilai lampu1Pin dan lampu2Pin sesuai dengan koneksi yang digunakan.
Atur IP Address NodeMCU:

Sesuaikan IP address NodeMCU pada bagian lamp_ip sesuai dengan IP yang akan diberikan kepada NodeMCU.
Unggah Kode ke NodeMCU:

Unggah kode Arduino ke NodeMCU melalui Arduino IDE.
Jalankan NodeMCU:

Nyalakan NodeMCU dan pastikan terhubung ke WiFi dengan mengecek output Serial Monitor pada Arduino IDE.
Langkah-langkah Penggunaan Bot Discord:

Persiapkan Bot Discord:

Buat bot Discord di Portal Pengembang Discord dan dapatkan token bot.
Atur Token dan Server ID:

Ganti nilai your token bot discord dengan token bot yang telah Anda dapatkan.
Gantilah id server anda pada baris channel = bot.get_guild(id server anda).text_channels[0] dengan ID server Discord yang diinginkan.
Jalankan Bot:

Jalankan script Python dan pastikan bot terhubung ke server Discord.
Gunakan Perintah Bot:

Di server Discord, gunakan perintah seperti l1n untuk menyalakan Lampu 1 atau l2m untuk mematikan Lampu 2.
Catatan:
Pastikan untuk menjaga keamanan token bot dan informasi sensitif lainnya agar tidak disertakan dalam repositori publik di GitHub.

English:

Installation and Usage of Discord Bot with NodeMCU (Arduino)
Installation Steps:

Prepare NodeMCU:

Connect NodeMCU to your computer and ensure you have Arduino IDE installed and configured with ESP8266 settings.
Download Required Libraries:

Make sure you have downloaded and installed two Arduino libraries: ESP8266WiFi and ESP8266WebServer. You can download them through the Arduino Library Manager.
Configure WiFi Connection on NodeMCU:

Fill in the SSID and password of your WiFi in the const char *ssid and const char *password sections accordingly.
Define Relay Pins:

Adjust the relay pins on NodeMCU by changing the values of lampu1Pin and lampu2Pin according to your wiring.
Set NodeMCU IP Address:

Adjust the NodeMCU IP address in the lamp_ip section according to the IP you want to assign to NodeMCU.
Upload Code to NodeMCU:

Upload the Arduino code to NodeMCU through the Arduino IDE.
Run NodeMCU:

Power up NodeMCU and ensure it connects to WiFi by checking the Serial Monitor output in the Arduino IDE.
Discord Bot Usage Steps:

Prepare Discord Bot:

Create a Discord bot on the Discord Developer Portal and obtain the bot token.
Configure Token and Server ID:

Replace the value your token bot discord with your obtained bot token.
Replace id server anda in the line channel = bot.get_guild(id server anda).text_channels[0] with the desired Discord server ID.
Run the Bot:

Run the Python script and ensure the bot connects to the Discord server.
Use Bot Commands:

In the Discord server, use commands such as l1n to turn on Lamp 1 or l2m to turn off Lamp 2.
