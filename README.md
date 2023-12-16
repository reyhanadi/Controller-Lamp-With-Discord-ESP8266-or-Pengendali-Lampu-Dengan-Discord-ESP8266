# Controller-Lamp-With-Discord-ESP8266-or-Pengendali-Lampu-Dengan-Discord-ESP8266
Prototype Number V-1 Discord Controller Lamp

Thanks For my friends help me to learn this , my first try is explode fuse on stalvolt and burn the 1 port relay haha, its everything okay now , not a big damage

- HATI HATI DALAM MENJALANKAN PROJECT INI SAYA TIDAK BERTANGGUNG JAWAB UNTUK KECELAKAN ATAU APAPUN YANG TERJADI
- ANDA HARUS MEMPELAJARAI DAN HATI HATI SAAT MEMPELAJARI TENTANG KELISTRIKAN 
- KARENA PROJECT INI TERDAPAT TEGANGAN TINGGI 

Jika Anda Tidak tahu rangkaian atau kelistikan project anda tanyakan ahlinya atau temanmu

Alat yang saya Gunakan adalah:
1. ESP 8266
2. 4 RELAY MODULE
3. 2 LAMPU
4. KABEL FEMALE TO FEMALE, MALE TO MALE, FEMALE TO MALE
5. 2 FITTING LAMPU PLAFON/GANTUNG
6. MCB FOR SAFETY
7. STEKER
8. KABEL TEMBAGA BUKAN SERABUT UKURAN 1.5 PANJANG 

Instalasi dan Penggunaan Bot Discord dengan NodeMCU (Arduino)
Langkah-langkah Instalasi:

1.	Persiapkan NodeMCU:
•	Hubungkan NodeMCU ke komputer dan pastikan telah menginstal Arduino IDE serta mengonfigurasi pengaturan ESP8266 pada Arduino IDE.

2.	Unduh Libraries yang Diperlukan:
•	Pastikan telah mengunduh dan menginstal dua library Arduino: ESP8266WiFi dan ESP8266WebServer. Anda dapat mengunduhnya melalui Arduino Library Manager.

3.	Atur Koneksi WiFi pada NodeMCU:
•	Isi SSID dan password WiFi pada bagian const char *ssid dan const char *password sesuai dengan koneksi WiFi yang akan digunakan.

4.	Definisikan Pin Relay:
•	Sesuaikan pin relay pada NodeMCU dengan mengganti nilai lampu1Pin dan lampu2Pin sesuai dengan koneksi yang digunakan.

5.	Atur IP Address NodeMCU:
•	Sesuaikan IP address NodeMCU pada bagian lamp_ip sesuai dengan IP yang akan diberikan kepada NodeMCU.

6.	Unggah Kode ke NodeMCU:
•	Unggah kode Arduino ke NodeMCU melalui Arduino IDE.

7.	Jalankan NodeMCU:
•	Nyalakan NodeMCU dan pastikan terhubung ke WiFi dengan mengecek output Serial Monitor pada Arduino IDE.

Langkah-langkah Penggunaan Bot Discord:
1.	Persiapkan Bot Discord:
•	Buat bot Discord di Portal Pengembang Discord dan dapatkan token bot.

2.	Atur Token dan Server ID:
•	Ganti nilai your token bot discord dengan token bot yang telah Anda dapatkan.
•	Gantilah id server anda pada baris channel = bot.get_guild(id server anda).text_channels[0] dengan ID server Discord yang diinginkan.

3.	Jalankan Bot:
•	Jalankan script Python dan pastikan bot terhubung ke server Discord.

4.	Gunakan Perintah Bot:
•	Di server Discord, gunakan perintah seperti l1n untuk menyalakan Lampu 1 atau l2m untuk mematikan Lampu 2.
Catatan: Pastikan untuk menjaga keamanan token bot dan informasi sensitif lainnya agar tidak disertakan dalam repositori publik di GitHub.

Kekurangan Project ini adalah 
- Tidak ada library Discord di aplikasi arduino saya harap kedepanya disediakan library langsung seperti telegram agar mudah membuat atau mengembangkan iot dengan discord
- IP masih lokal 
- Tidak bisa di dijalankan di hosting atau replit karena menggunakan ip lokal jadi tidak akan terkoneksi iot dengan bot


________________________________________


English:

Important Safety Disclaimers:
1.	Disclaimer of Responsibility:
•	Caution: Exercise extreme caution when executing this project. I do not take responsibility for any accidents or incidents that may occur during the implementation or operation of this project.

2.	Electrical Knowledge and Precautions:
•	Safety First: It is crucial to study and exercise caution when delving into the realm of electronics and electricity. Given the presence of high voltage in this project, a thorough understanding of electrical principles is necessary.

3.	High Voltage Warning:
•	Handle with Care: This project involves high voltage components. Always be aware of the potential dangers associated with high voltage, and take appropriate precautions to ensure personal safety.
Additional Notes:

Seek Expert Advice:
•	If you are unfamiliar with circuitry or electrical systems, it is strongly advised to consult with experts or seek guidance from knowledgeable individuals. Always prioritize safety and seek assistance from friends or professionals.

List of Equipment Used:
1.	ESP 8266:
•	The primary microcontroller used for IoT communication.
2.	4-Relay Module:
•	Used for controlling multiple electrical devices independently.
3.	2 Lamps:
•	Light sources controlled by the relay module.
4.	Various Cables:
•	Includes female-to-female, male-to-male, and female-to-male cables for wiring.
5.	2 Lamp Holders (Fitting Lampu Plafon/Gantung):
•	Fixtures for holding the lamps.
6.	MCB (Miniature Circuit Breaker):
•	Implemented for safety to protect against overcurrent.
7.	Power Plug (Steker):
•	Provides power supply to the circuit.
8.	Copper Wire (Kabel Tembaga):
•	Specifically, non-stranded copper wire with a size of 1.5 for electrical connections. Ensure proper insulation and quality.

Installation and Usage of Discord Bot with NodeMCU (Arduino)
Installation Steps:

1.	Prepare NodeMCU:
•	Connect NodeMCU to your computer and ensure you have Arduino IDE installed and configured with ESP8266 settings.

2.	Download Required Libraries:
•	Make sure you have downloaded and installed two Arduino libraries: ESP8266WiFi and ESP8266WebServer. You can download them through the Arduino Library Manager.

3.	Configure WiFi Connection on NodeMCU:
•	Fill in the SSID and password of your WiFi in the const char *ssid and const char *password sections accordingly.

4.	Define Relay Pins:
•	Adjust the relay pins on NodeMCU by changing the values of lampu1Pin and lampu2Pin according to your wiring.

5.	Set NodeMCU IP Address:
•	Adjust the NodeMCU IP address in the lamp_ip section according to the IP you want to assign to NodeMCU.

6.	Upload Code to NodeMCU:
•	Upload the Arduino code to NodeMCU through the Arduino IDE.

7.	Run NodeMCU:
•	Power up NodeMCU and ensure it connects to WiFi by checking the Serial Monitor output in the Arduino IDE.

Discord Bot Usage Steps:
1.	Prepare Discord Bot:
•	Create a Discord bot on the Discord Developer Portal and obtain the bot token.

2.	Configure Token and Server ID:
•	Replace the value your token bot discord with your obtained bot token.
•	Replace id server anda in the line channel = bot.get_guild(id server anda).text_channels[0] with the desired Discord server ID.

3.	Run the Bot:
•	Run the Python script and ensure the bot connects to the Discord server.

4.	Use Bot Commands:
•	In the Discord server, use commands such as l1n to turn on Lamp 1 or l2m to turn off Lamp 2.

Shortcomings of this Project:

- Lack of Discord Library in Arduino:
One limitation is the absence of a dedicated Discord library for Arduino applications. It is suggested that in the future, a specific library for Discord be provided, similar to the simplicity found in libraries for other platforms like Telegram. This would facilitate the creation and development of IoT projects with Discord integration.
  
- Local IP Address:
The current implementation uses a local IP address for communication between the Discord bot and the IoT device (NodeMCU). It would be beneficial to explore options for dynamic or global IP addresses to enhance accessibility and connectivity.

- Limited Hosting Compatibility:
Due to the reliance on a local IP address, the project may face challenges when deployed on hosting services or platforms like Replit. As it stands, the local IP setup restricts the ability to seamlessly connect the IoT device with the Discord bot in hosting environments.
