#include <Ethernet.h>
#include <EthernetUdp.h>
#include <EEPROM.h>
#define UDP_PORT 8888 

IPAddress TERMINAL(192, 168, 100, 223);
IPAddress knu(192, 168, 100, 49);
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED}; // MAC-адрес
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
EthernetUDP Udp;

String states[3]={"whating","worck","done"};
int pointer=0;

void setup() {
  Serial3.begin(9600);
  Ethernet.begin(mac, knu);
  Udp.begin(UDP_PORT);
  Serial.begin(9600);
  Serial.println("Ethernet and UDP initialized");
  Serial3.println("whating");  
  delay(300);
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    packetBuffer[packetSize] = '\0';
    if (strcmp(packetBuffer, "whating") == 0) {
      Serial3.println("whating");
      Serial.println("whating");   
    }
    if (strcmp(packetBuffer, "worck") == 0) {
      Serial3.println("worck");
      Serial.println("worck");
    }
    if (strcmp(packetBuffer, "done") == 0) {
      Serial3.println("done");
      Serial.println("done");
      }
  }
  if (Serial3.available() > 0) {
    String receivedData = Serial3.readStringUntil('\n');
    sendUdp(TERMINAL,receivedData);
    Serial.println(receivedData); 
  }
  
}

void sendUdp(IPAddress adr, String msg) {
  char out[msg.length() + 1];
  msg.toCharArray(out, msg.length() + 1);
  Udp.beginPacket(adr, UDP_PORT);
  Udp.write(out);
  Udp.endPacket();
}
