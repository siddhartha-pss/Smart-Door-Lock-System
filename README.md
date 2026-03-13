# Smart-Door-Lock-System
Secure web-based access control system using Raspberry Pi, Flask, and servo/GPIO control.

## Abstract
The project aims to create a secure web-based access control system utilizing a Raspberry Pi to control both a servo motor and a GPIO pin. The system includes a Flask web server running on the Raspberry Pi, allowing users to input a password via a web interface. Upon entering the correct password, the system triggers actions such as unlocking a mechanism controlled by the servo motor and sending a logic signal to the GPIO pin. The project employs Python programming, Flask web development framework, RPi.GPIO library for GPIO control, and servo motor control to achieve its objectives.

## Objectives
The objective of this project is to develop a secure and accessible control system using a Raspberry Pi for home automation or small-scale access control applications.

**Key objectives include:**
1. **Password-Protected Access:** Implement a Flask web server to provide a user-friendly interface for password entry.  
2. **Servo Motor Control:** Enable the Raspberry Pi to control a servo motor, allowing for the physical manipulation of mechanisms like locks or barriers upon successful password entry.  
3. **GPIO Signal Transmission:** Utilize GPIO pins to send logic signals, enabling the Raspberry Pi to interface with external devices or systems based on the authentication outcome.  
4. **Security:** Ensure the system's security by implementing password authentication and preventing unauthorized access to the control functions.  
5. **Reliability and Robustness:** Develop the system to be reliable and robust, capable of operating continuously and handling various environmental conditions.  
6. **Scalability:** Design the system with the potential for scalability, allowing for future expansion and integration with additional features or devices.  
7. **User-Friendly Interface:** Create a user-friendly web interface for seamless interaction with the control system, enhancing usability and accessibility.  

## Components Required
- **Servo motor**  
- **Breadboard**  
- **Raspberry Pi**  
- **Connecting wires**

## Working
1. Once the connections are done, power on the Raspberry Pi board and compile the code to check for any errors.  
2. After compilation, click the link that appears in the shell of the compiler. This will lead you to the login page.  
3. Enter the password you set up.  
   - If the correct password is entered, the servo motor will rotate, unlocking the mechanism, and **"SERVO UNLOCKED"** will appear on the screen.  
   - If the wrong password is entered, the servo motor will remain in its current position, keeping the door locked, and **"INCORRECT PASSWORD"** will appear on the screen.  
4. To lock the door again, a link is provided below the password input box. Once clicked, the servo motor rotates back to its original position.  


