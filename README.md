# Emotion Analysis with Psychobot

## Overview
Psychobot is an advanced emotion analysis tool designed to analyze and categorize emotions from various inputs. Leveraging machine learning and deep learning models, it provides an intuitive interface for users to interact with the emotion analysis features.


![](https://github.com/naufalprtm/-emotion/raw/83df07e1d6efd5b7d8ed8d0c5076f85152ec0ecf/b94519679f4e0bacfad9c944d4d399ed.jpg)

## Project Structure
```
psychobot/
│
├── docker-compose.yml           # Docker Compose configuration file
├── Dockerfile                    # Dockerfile for building the Psychobot image
│
├── pyemotion/                   # Main application code
│   ├── server.py                # Flask server for handling requests
│   ├── lightgbm_training.py      # Training script for LightGBM model
│   ├── llm_inference.py          # Inference script for LLM
│   ├── cnn_training.py           # Training script for CNN model
│   ├── models/                   # Directory containing trained models
│   │   ├── lightgbm_model.pkl    # LightGBM model file
│   │   ├── vectorizer.pkl        # Vectorizer for text data
│   │   └── cnn_model.h5          # CNN model file
│   ├── database.py               # Database interaction layer
│   ├── auth.py                   # Authentication functions
│   ├── utils.py                  # Utility functions
│   ├── emotion_analysis.py        # Emotion analysis logic
│   └── config.py                 # Configuration settings
│
├── cudaemotion/                  # CUDA-optimized components
│   ├── image_preprocessing.cpp    # C++ code for image preprocessing
│   ├── llm_cuda_inference.py      # CUDA implementation for LLM inference
│   └── utils_cuda.py              # CUDA utility functions
│
├── templates/                    # HTML templates for the frontend
│   ├── index.html                # Main landing page
│   ├── login.html                # User login page
│   ├── register.html             # User registration page
│   ├── profile.html              # User profile page
│   ├── emotions.html             # Page to display emotions
│   └── error.html                # Error handling page
│
├── static/                       # Static files (CSS, JS, images)
│   ├── style.css                 # Custom styles
│   ├── app.js                    # JavaScript for client-side functionality
│   ├── bootstrap.min.css         # Bootstrap CSS for responsive design
│   ├── bootstrap.bundle.min.js    # Bootstrap JS bundle
│   └── images/                   # Image assets
│       ├── logo.png              # Logo image
│       └── placeholder.png        # Placeholder image
│
└── data/                         # Dataset files
    ├── data_emotion.csv          # Dataset for training emotions
    ├── image_emotion_data.csv     # Image dataset for emotion classification
    └── emotion_labels.json        # Emotion labels and definitions
```
### Installation
Prerequisites
Ensure that you have Docker and Docker Compose installed on your machine. You can download them from the following links:

- **Docker Installation**
- **Docker Compose Installation**
- **Build the Docker Image**

To build the Docker image for the Psychobot application, navigate to the project directory and run:
```
docker build -t psychobot .
```

Run the Application
You can run the application using Docker with the following command:

```
docker run -p 5000:5000 psychobot
```
Alternatively, you can use Docker Compose to build and run the application:

```
docker-compose build
docker-compose up
```

### Usage
Once the application is running, you can access it in your web browser at http://localhost:5000. From there, you can interact with the various features provided by Psychobot, including emotion analysis and user authentication.

### API Endpoints
- **POST /analyze: Analyze the emotion of a given text/image.**
- **GET /emotions: Retrieve a list of recognized emotions.**
- **Refer to the API documentation for more details on usage and parameters.**

### Contributing
- **We welcome contributions to improve Psychobot! If you would like to contribute, please fork the repository, make your changes, and submit a pull request.**