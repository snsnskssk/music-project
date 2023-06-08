import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json
MQTT_HOST = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60

MQTT_PUB_TOPIC = "mobile/bspsy/sensing"

client = mqtt.Client()

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUTTON = 24
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
buzzer_pin = 12
GPIO.setup(buzzer_pin, GPIO.OUT)

TRIG = 13
ECHO = 19

print("start")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try :
    while True :

        GPIO.output(TRIG, True)
        time.sleep(1)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0 :
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1 :
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        print("Distance : ", distance, "cm")
        
        sensing = {
            "distance": distance
        }
        value = json.dumps(sensing)
        client.publish(MQTT_PUB_TOPIC, value)
        print(value)
        
        if distance <= 5:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(261)
            time.sleep(1)
            p.stop()
        
        elif distance > 5 and distance <= 10:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(294)
            time.sleep(1)
            p.stop()
            
        elif distance > 10 and distance <= 15:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(329)
            time.sleep(1)
            p.stop()
            
        elif distance > 15 and distance <= 20:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(349)
            time.sleep(1)
            p.stop()
            
        elif distance > 20 and distance <= 25:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(392)
            time.sleep(1)
            p.stop()
        
        elif distance > 25 and distance <= 30:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(440)
            time.sleep(1)
            p.stop()
            
        elif distance > 30 and distance <= 35:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(493)
            time.sleep(1)
            p.stop()
        
        elif distance > 35 and distance <= 40:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(100)
            p.ChangeDutyCycle(90)
            p.ChangeFrequency(523)
            time.sleep(1)
            p.stop()
            
    
        
        if GPIO.input(BUTTON) == True:
            print("악기 종료")
            break
        
      
except :
    print("I'm done!")
    GPIO.cleanup()

