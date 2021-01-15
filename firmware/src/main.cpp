#include <Arduino.h>
#include <NewPing.h>
#include <ESP8266HTTPClient.h>
#include "ESP8266WiFi.h"

#define ECHO_PIN 0 // D3
#define TRIGGER_PIN 2 // D4
#define MAX_DISTANCE 200

const char* ssid = "EASIN__BASNETWORK"; //Enter SSID
const char* password = "easin@1122"; //Enter Password

String msg;
String endpoint = "http://192.168.0.108:8000/api/v1/sensor-data/";
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
float dist_cm;
 
void setup() {
 
  Serial.begin(115200);
 
  delay(1000);
 
  WiFi.begin(ssid, password);
 
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting..");
  }
 
  Serial.print("Connected to WiFi. IP:");
  Serial.println(WiFi.localIP());
}
 
void loop() {
  if (WiFi.status()!=WL_CONNECTED){
    Serial.println("Wifi disconnected");
    WiFi.begin(ssid, password);
    delay(1000);
  }
  HTTPClient http;
  http.begin(endpoint);
  delay(50);
  dist_cm = sonar.ping_cm();
  delay(50);
  String content = "distance=" + String(dist_cm);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  delay(1000);
  int httpResponse = http.POST(content);
  Serial.print("HTTP Response code: ");
  Serial.println(httpResponse);
  Serial.println(content);
  http.end();

}