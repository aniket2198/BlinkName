int led = D7;

void setup() {
    pinMode(led, OUTPUT);
}


char *aniket[6] = {".-", "-.","..", "-.-", ".", "-"};

int dot = 500;


void flash(char character[]){
    for(int i=0; i<strlen(character); i++){
        if(character[i] == '.'){
            digitalWrite(led, HIGH);
            delay(dot);
            digitalWrite(led, LOW);
        }
        else if(character[i] == '-'){
            digitalWrite(led, HIGH);
            delay(dot*3);
            digitalWrite(led, LOW);
        }
        delay(dot);
    }
}

int counter = 0;
int i = 0;

void loop() {
   
   
    if(counter < 6){
       
        flash(aniket[counter]);
        counter++;
    }
}
