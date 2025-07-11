
#include<cvzone.h>

SerialData serialData(3,1); // 3 single digit values

int valsRec[3];

int red =8;
int green =9;
int blue = 10;

void setup() {

  serialData.begin();
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  pinMode(red,OUTPUT);

}

void loop() {
      serialData.Get(valsRec);
      digitalWrite(red,valsRec[0]);
      digitalWrite(blue,valsRec[1]);
      digitalWrite(green,valsRec[2]);
    
}
