from flask import Flask, request, render_template 
import RPi.GPIO as GPIO 
import time 

app = Flask(__name__) 

# Set up GPIO 
GPIO.setmode(GPIO.BOARD) 
output_pin = 11  # Physical pin number for output 
GPIO.setup(output_pin, GPIO.OUT)

# Set up servo motor 
servo_pin = 12  # Physical pin number for servo 
GPIO.setup(servo_pin, GPIO.OUT) 
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms period) 
pwm.start(0)

# Define your password 
correct_password = "your_password_here"

def unlock(): 
    pwm.ChangeDutyCycle(7.5)  # Rotate the servo to the middle position 
    time.sleep(1) 
    pwm.ChangeDutyCycle(0)  # Stop the servo 

def lock(): 
    pwm.ChangeDutyCycle(2.5)  # Rotate the servo to the locked position 
    time.sleep(1) 
    pwm.ChangeDutyCycle(0)  # Stop the servo 

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/unlock', methods=['POST']) 
def handle_unlock(): 
    password = request.form.get('password') 
    if password == correct_password: 
        unlock() 
        return "Servo unlocked." 
    else: 
        return "Incorrect password."
    
@app.route('/Lock')
def Lock(): 
    pwm.ChangeDutyCycle(12.5)  # Rotate the servo to the opposite direction 
    time.sleep(1) 
    pwm.ChangeDutyCycle(0)  # Stop the servo 
    return "Lock the Vault."

if __name__ == '__main__': 
    try: 
        app.run(debug=True, host='0.0.0.0') 
    finally: 
        # Clean up GPIO 
        GPIO.cleanup() 
