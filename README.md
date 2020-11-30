## Eye-Blink-Detection

### Introduction
Interaction with computers in this modern era requires manual intervention of our limbs which could be quite difficult for a physically impaired person , so to ease it
the primary goal of this project is to develop a detection and interaction system based on the combination of of Eye-Blinks and facial movements that has the potential to establish a seamless connection between a person and a computer through voluntary blinks and/or subtle facial movements.

### Tools Used
I have used OpenCV, Python and dlib in this project.

### Concept


![WhatsApp Image 2020-11-30 at 18 27 52](https://user-images.githubusercontent.com/58965233/100612987-d420bd80-3339-11eb-8dd6-d49b50322ada.jpeg)





EAR(Eye-Aspect-Ratio) can be defined as the ratio between the sum of euclidean length of two vertical lines obtained by joining points p2,p6 and p3,p5 respectively to the euclidean lenth of horizontal line obtained by joining points p1 and p4.

 **EAR=||P2-P6|| + ||P3-P5|| / 2||P1-P4||**
 
When we close our eyes, the length of the vertical line decreases and start tending towards 0.So the eye aspect ratio also decreases. So just by observing the EAR we can come to the conclusion that the eye is blinking or not.  
 
 Also haar cascade algorithms are used for face detection and eye tracking is done  by geometrical features. 

### Summary
This project focuses on detecting eye-blinks and controlling mouse cursor movements using human limbs like face,eyes etc. This kind of systems can be very useful in creating real time applications which could be user friendly but quite beneficial for handicapped users.
