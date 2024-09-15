# Traffic Sign Recognition System

## Introduction
Traffic signs play a crucial role in road safety, providing necessary information to drivers, passengers, and autonomous vehicles. Traffic sign classification involves identifying which class a traffic sign belongs to, an essential task for autonomous vehicles.

This project implements a **Convolutional Neural Network (CNN)** model to classify traffic signs into different categories using image processing and deep learning techniques. The model is capable of real-time detection and classification, aiding in the development of **autonomous driving systems**.

## Objective
The objective of this project is to create a system that assists in recognizing traffic signs for autonomous vehicles, enhancing road safety and reducing accidents. The ultimate goal is to contribute toward fully autonomous vehicles by integrating advanced **traffic sign recognition** capabilities.

## Scope
Traffic signals are essential for the safety of vehicles and pedestrians. This project focuses on detecting Indian road traffic signs under various conditions (light, orientation, scale). Using deep learning (CNN) and data augmentation techniques, this system improves the detection and recognition performance of traffic signs.

## Study of Existing Systems
1. **Waymo (Google's Self-Driving Car Project)**  
   - **Advantages**: Robust navigation, real-world testing experience.  
   - **Disadvantages**: Limited deployment, high development costs.  
   - [Waymo Reference](https://waymo.com/)

2. **Tesla Autopilot**  
   - **Advantages**: Continuous software updates, large data collection.  
   - **Disadvantages**: Occasional misinterpretation, accidents.  
   - [Tesla Autopilot Reference](https://www.tesla.com/autopilot)

3. **Cruise (General Motors)**  
   - **Advantages**: Integration with mass production.  
   - **Disadvantages**: Limited operational areas.  
   - [Cruise Reference](https://www.cruise.com/)

## Project Description
This project builds a CNN model that classifies traffic signs from images. The **German Traffic Sign Recognition Benchmark (GTSRB)** dataset is used to train the model, which contains 43 classes of traffic signs. The system utilizes image processing techniques to resize images and prepare the dataset for classification.

The trained model is capable of detecting traffic signs in real-time, making it useful for **autonomous vehicles** and **advanced driver assistance systems (ADAS)**.

## Methodology
The project follows a structured approach:
1. **Dataset Exploration**: The **GTSRB dataset** is used for training and testing.
2. **Building the CNN Model**: A convolutional neural network is used to classify images.
3. **Training the Model**: The model is trained with a batch size of 64, and achieves stable accuracy after 15 epochs.
4. **Testing**: Images are resized to 30x30 pixels and fed into the model for prediction.

## Features
- **Traffic Sign Recognition**: Accurately recognizes and classifies traffic signs.
- **Real-time Decision Making**: Integrated into autonomous driving systems for real-time traffic navigation.
- **Integration with Traffic Rules**: Ensures compliance with traffic regulations.

## System Architecture
- **Sensor Suite**: Uses cameras, LiDAR, radar for real-time data capture.
- **Data Preprocessing**: Filters and fuses sensor data for accurate input.
- **CNN-based Detection**: Recognizes traffic signs and objects using CNN.
- **ADAS Algorithms**: Provides driver assistance features like lane-keeping and collision avoidance.
- **Decision-Making Engine**: Processes data for real-time decision making.

## User Interface
- **Dashboard**: Displays vehicle state, speed, and navigation.
- **Traffic Sign Display**: Shows recognized traffic signs and their meaning.
- **Manual Override Controls**: Allows the user to manually take control if necessary.

## Technology Stack
- **Programming Language**: Python
- **Libraries**: TensorFlow, NumPy, OpenCV, Matplotlib
- **Platform**: Visual Studio Code (VSCode)

## Testing Plan
1. **Traffic Sign Recognition Testing**: Ensure accurate detection and classification of signs.
2. **ADAS Algorithm Testing**: Validate lane-keeping and adaptive cruise control.
3. **Integration Testing**: Ensure smooth integration between sensor input, CNN, and ADAS.
4. **System Performance Testing**: Evaluate real-time performance and response times.

## Expected Outcome
- Enhance road safety by improving the accuracy of traffic sign detection.
- Provide real-time alerts and assistance in autonomous vehicles.
- Integration with driver assistance systems to improve traffic management and decision-making.

## Resources
- **Software**: Python, TensorFlow, OpenCV
- **Hardware**: 4GB RAM, Intel Core i3, 1TB Disk
- **Platform**: Visual Studio Code

## Limitations
Some limitations of traffic sign recognition include:
- **Illumination Variations**: May affect accuracy under different lighting conditions.
- **Occlusions**: Partially blocked signs can lead to recognition failure.
- **Complex Urban Scenarios**: Handling complex and unpredictable traffic situations can be challenging.

## References
1. **GTSRB Dataset**: [Link to dataset](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news)
2. **Waymo**: [Link](https://waymo.com/)
3. **Tesla Autopilot**: [Link](https://www.tesla.com/autopilot)
4. **Cruise**: [Link](https://www.cruise.com/)
5. **Uber ATG**: [Link](https://www.uber.com/us/en/autonomous/)
