


int hand; 
Servo myservo;
int prevVal;
int firstTime;

const int pinTempSensor = A4; // Grove - Temperature Sensor connect to A5
int tempSample=0;

void setup() {
    Serial.begin(9600);
    hand = -1;
    pinMode(D4, OUTPUT);
    pinMode(D6, OUTPUT);
    myservo.attach(D3);
    int pos;
    //lcd.begin(16, 2);
    
}

void loop() {
    int analogValue = analogRead(A4);
                double voltage = 3.3 * ((double)analogValue / 4095.0);
                double temperature = ((voltage - 0.5) * 100) - 45;
                Serial.print(temperature);
                Serial.print(" ");
                Serial.println(temperature);
    if (Serial.available()>0)
    {
        
        if (firstTime == 1)
        {
            prevVal = Serial.read();
            hand = prevVal;
        }
        else
        {
            hand = Serial.read();
        }
        
        if (prevVal != hand)
        {
            
            
            if (hand == 48)
            {
                tempSample = 1;
                digitalWrite(D4, LOW);
                digitalWrite(D6, HIGH);
         
                myservo.write(180);
                delay(750);
                myservo.write(90);
                Serial.print(temperature);
                Serial.print(" ");
                Serial.println(temperature);
                
            }
            else if (hand == 49)
            {
                digitalWrite(D4, HIGH);
                digitalWrite(D6, LOW);
              
                myservo.write(0);
                delay(750);
                myservo.write(90);
                tempSample=0;
                Serial.print(temperature);
                Serial.print(" ");
                Serial.println(temperature);
            }
            else if (hand == 50)
            {
                digitalWrite(D4, LOW);
                digitalWrite(D6, LOW);
              
                myservo.write(90);
                
                
            }
            
           
            if (hand == 48 || hand == 49)
            {
                prevVal = hand;
            }
            Serial.flush();
            
        }
    }
 
}
