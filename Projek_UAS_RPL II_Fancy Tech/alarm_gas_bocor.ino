#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

// Konfigurasi Wifi
const char *ssid = "IF8-BizGOD";
const char *password = "Gitugituwelah";

// Deklarasi pin sensor
#define sensorPin 14
#define sensorMQ A0
#define sensorMQDig 12
#define pinBuzzer 16

// Deklarasi variabel
String url;
WiFiClient client;

int bacasensor = 0;
float sensorVoltage;
float sensorValue;
int sensorDig;

// Deklarasi pin LED
int pinLED = 13;

void setup() {
  Serial.begin(9600);

  // Konfigurasi pin
  pinMode(pinLED, OUTPUT);
  pinMode(pinBuzzer, OUTPUT);
  pinMode(sensorMQ, INPUT);
  pinMode(sensorMQDig, INPUT);
  pinMode(sensorPin, INPUT);
  digitalWrite(pinBuzzer, HIGH);

  // Koneksi Wifi
  WiFi.hostname("NodeMCU");
  WiFi.begin(ssid, password);

  // Tunggu koneksi Wifi
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(pinLED, LOW);
    delay(500);
  }

  // Indikasi koneksi Wifi
  digitalWrite(pinLED, HIGH);
}

void loop() {
  // Baca nilai sensor
  sensorValue = analogRead(sensorMQ);
  sensorDig = digitalRead(sensorMQDig);
  sensorVoltage = sensorValue / 1024 * 100;
  bacasensor = digitalRead(sensorPin);

  // Deteksi api
  if (bacasensor == LOW || sensorDig == LOW) {
    // Tampilkan informasi di serial monitor
    Serial.print("Digital value: ");
    Serial.print(bacasensor);
    Serial.print(" Flame detected ");
    Serial.print("sensor voltage = ");
    Serial.print(sensorVoltage);
    Serial.print(" %");
    Serial.print("\t");
    Serial.print("sensor digital = ");
    Serial.println(sensorDig);

    // Aktifkan buzzer
    digitalWrite(pinBuzzer, LOW);

    // Kirim notifikasi WhatsApp
    kirim_wa("Peringatan!\nTerdeteksi adanya kebocoran gas di rumah anda, segera evakuasi!");

    // Tunggu 1 detik
    delay(1000);
  } else {
    // Tampilkan informasi di serial monitor
    Serial.print("Digital value: ");
    Serial.print(bacasensor);
    Serial.print(" No flame detected ");
    Serial.print("sensor voltage = ");
    Serial.print(sensorVoltage);
    Serial.print(" %");
    Serial.print("\t");
    Serial.print("sensor digital = ");
    Serial.println(sensorDig);

    // Matikan buzzer
    digitalWrite(pinBuzzer, HIGH);

    // Tunggu 1 detik
    delay(1000);
  }
}

void kirim_wa(String pesan) {
  // Buat URL untuk API CallMeBot
  url = "http://api.callmebot.com/whatsapp.php?phone=6282119701426&text=" + urlencode(pesan) + "&apikey=6088081";

  // Kirim pesan
  postData();
}

void postData() {
  // Deklarasi variabel status HTTP
  int httpCode;

  // Siapkan HTTPClient
  HTTPClient http;

  // Kirim request HTTP
  http.begin(client, url);
  httpCode = http.POST(url);

  // Periksa status HTTP
  if (httpCode == 200) {
    Serial.println("Notifikasi WhatsApp Berhasil Terkirim");
  } else {
    Serial.println("Notifikasi WhatsApp Gagal Terkirim");
  }
 
  // Tutup koneksi HTTP
  http.end();
}

String urlencode(String str) {
  String encodedString = "";
  char c;
  char code0, code1, code2;

  // Looping setiap karakter dalam string
  for (int i = 0; i < str.length(); i++) {
    c = str.charAt(i);

    // Konversi karakter spasi
    if (c == ' ') {
      encodedString += '+';
    }

    // Konversi karakter alfanumerik
    else if (isalnum(c)) {
      encodedString += c;
    }

    // Konversi karakter spesial
    else {
      code0 = (c & 0xf) + '0';
      if ((c & 0xf) > 9) {
        code1 = (c & 0xf) - 10 + 'A';
      } else {
        code1 = (c & 0xf) + '0';
      }
      c = (c >> 4) & 0xf;
      code2 = c + '0';
      if (c > 9) {
        code2 = c - 10 + 'A';
      } else {
        code2 = c + '0';
      }
      encodedString += '%';
      encodedString += code2;
      encodedString += code1;
    }
  }

  // Tampilkan string yang telah di-encode
  Serial.println(encodedString);
  return encodedString;
}
