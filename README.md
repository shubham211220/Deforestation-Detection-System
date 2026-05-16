# 🌲 Deforestation Detection System

A real-time computer vision system that detects deforestation using a CNN-based deep learning model. The system captures live video, analyzes forestation levels, and automatically sends WhatsApp alerts with location data when deforestation is detected.

---

## 📋 Table of Contents

- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Training Your Own Model](#-training-your-own-model)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)

---

## ✨ Features

- 🔴 **Real-time Detection**: Live webcam feed analysis for deforestation
- 🤖 **CNN-based Classification**: Deep learning model (Keras/TensorFlow) for forest vs deforestation
- 📊 **Green Percentage Analysis**: Pixel-level green coverage estimation
- 📍 **Location Tracking**: Automatic GPS coordinates and Google Maps link generation
- 📱 **WhatsApp Alerts**: Instant image + location alerts to configured mobile numbers
- 🔊 **Audio Alerts**: Text-to-speech notifications for detected events
- 📸 **Dataset Collection Tool**: Built-in utility to capture training images

---

## 🏗️ System Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Webcam Feed    │────▶│  GreenEstimator  │────▶│  CNN Model      │
│  (OpenCV)       │     │  (Pre-filter)    │     │  (Keras)        │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                              │                           │
                              ▼                           ▼
                    ┌──────────────────┐        ┌─────────────────┐
                    │  < 97% Green     │        │  Deforestation  │
                    │  (Proceed)       │        │  Detected       │
                    └──────────────────┘        └─────────────────┘
                                                         │
                              ┌────────────────────────┼────────────┐
                              ▼                        ▼            ▼
                    ┌──────────────────┐    ┌─────────────────┐  ┌─────────────┐
                    │  LocationFetcher │    │  WASender       │  │  Audio Alert│
                    │  (GPS + Maps)    │    │  (WhatsApp)     │  │  (gTTS)     │
                    └──────────────────┘    └─────────────────┘  └─────────────┘
```

> 📖 For detailed architecture, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Webcam
- WhatsApp Web logged in (for alerts)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Deforestation-Detection-System.git
cd Deforestation-Detection-System

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download or train the model
# Place your trained model as: models/deforestation_trained_data.h5

# 4. Run the detection system
python src/Starter.py
```

---

## 📁 Project Structure

```
Deforestation-Detection-System/
├── src/
│   ├── Starter.py                          🚀 Entry point
│   ├── detection/
│   │   └── Deforestation_Detection_init.py  Real-time detection
│   ├── training/
│   │   ├── DeForestation_Training.py        Model training
│   │   └── ImageCapturer_For_Training.py    Dataset collector
│   └── utils/
│       ├── GreenEstimator.py                Green pixel analysis
│       ├── LocationFetcher.py               GPS & maps
│       └── WASender.py                      WhatsApp alerts
├── models/              # Trained model storage
├── dataset/             # Training data (train/test)
├── docs/                # Documentation
├── assets/              # Graphs, samples, audio
├── logs/                # Runtime logs
└── temp/                # Temporary files
```

---

## 📖 Usage

### 1. Real-time Detection

```bash
python src/Starter.py
```

The system will:
1. Open webcam feed
2. Analyze the selected region
3. Send WhatsApp alert if deforestation detected
4. Press `q` to quit

### 2. Collect Training Data

```bash
python src/training/ImageCapturer_For_Training.py
```

- Press `SPACE` to capture an image
- Press `ESC` to quit
- Images saved to `dataset/train/` or `dataset/test/`

### 3. Train the Model

```bash
python src/training/DeForestation_Training.py
```

- Ensure dataset is in `dataset/train/` and `dataset/test/`
- Model saved to `models/deforestation_trained_data.h5`

> 📖 For detailed usage, see [docs/USAGE.md](docs/USAGE.md)

---

## 🧠 Training Your Own Model

1. **Collect Images**: Use `ImageCapturer_For_Training.py`
2. **Organize Dataset**:
   ```
   dataset/
   ├── train/
   │   ├── Forestation/
   │   └── De-Forestation/
   └── test/
       ├── Forestation/
       └── De-Forestation/
   ```
3. **Train**: Run `DeForestation_Training.py`
4. **Evaluate**: Check accuracy/loss graphs in `assets/graphs/`

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Computer Vision | OpenCV |
| Deep Learning | Keras, TensorFlow |
| Image Processing | PIL (Pillow) |
| Location Services | GeoPy (Nominatim) |
| Messaging | PyWhatKit (WhatsApp) |
| Audio | gTTS (Google TTS) |

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Dataset collected using custom image capture tool
- Model trained on forestation vs deforestation imagery
- Location services powered by OpenStreetMap (Nominatim)

---

> ⚠️ **Note**: This system uses WhatsApp Web automation. Ensure WhatsApp Web is logged in on your default browser before running.
