# Usage Guide

## Table of Contents

1. [Setup & Installation](#setup--installation)
2. [Running Detection](#running-detection)
3. [Collecting Training Data](#collecting-training-data)
4. [Training the Model](#training-the-model)
5. [Configuration](#configuration)
6. [Troubleshooting](#troubleshooting)

---

## Setup & Installation

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install opencv-python keras tensorflow geopy pywhatkit gTTS pillow numpy matplotlib keyboard
```

### Step 2: Prepare WhatsApp Web

1. Open your default browser
2. Go to [web.whatsapp.com](https://web.whatsapp.com)
3. Scan QR code with your phone
4. Keep the browser tab open

> ⚠️ **Important:** WhatsApp Web must be logged in for alerts to work

### Step 3: Place Trained Model

Download or train the model and place it at:
```
models/deforestation_trained_data.h5
```

---

## Running Detection

### Basic Usage

```bash
python src/Starter.py
```

This uses the default phone number: `+919168917291`

### Custom Phone Number

Edit `src/Starter.py`:
```python
Deforestation_Detection_init.initDetection("+91YOUR_NUMBER_HERE")
```

### What Happens During Detection

1. **Webcam opens** — Position camera toward forest area
2. **ROI appears** — Red/blue rectangle shows analysis region
3. **Real-time analysis** — Green % and CNN prediction displayed
4. **Alert triggered** — If deforestation detected for 150 frames:
   - WhatsApp image sent to configured number
   - Location link included
   - System stops automatically

### Controls

| Key | Action |
|-----|--------|
| `q` | Quit detection |

---

## Collecting Training Data

### Start Capture Tool

```bash
python src/training/ImageCapturer_For_Training.py
```

### Setup Dataset Structure

Before capturing, ensure folders exist:
```
dataset/
├── train/
│   ├── Forestation/
│   └── De-Forestation/
└── test/
    ├── Forestation/
    └── De-Forestation/
```

### Configure Capture

Edit these lines in `ImageCapturer_For_Training.py`:
```python
typename = "train"          # "train" or "test"
state_type = "Forestation"  # "Forestation" or "De-Forestation"
```

### Capture Controls

| Key | Action |
|-----|--------|
| `SPACE` | Capture current frame |
| `ESC` | Quit capture tool |

### Tips for Good Dataset

- Capture 200+ images per class
- Vary lighting conditions
- Include different angles
- Keep ROI consistent
- Balance train/test split (80/20)

---

## Training the Model

### Prerequisites

1. Dataset organized in `dataset/train/` and `dataset/test/`
2. Each folder has `Forestation/` and `De-Forestation/` subfolders
3. Minimum 100 images per class recommended

### Run Training

```bash
python src/training/DeForestation_Training.py
```

### Training Output

| Output | Location |
|--------|----------|
| Trained Model | `models/deforestation_trained_data.h5` |
| Accuracy Graph | `assets/graphs/Model_Accuracy_Graph.png` |
| Loss Graph | `assets/graphs/Model_Loss_Graph.png` |

### Training Parameters

Edit `DeForestation_Training.py` to adjust:
```python
epochs = 150        # Increase for better accuracy
batch_size = 64     # Reduce if OOM error
input_shape = (150, 150, 3)  # Image dimensions
```

---

## Configuration

### Change Detection Region

Edit `Deforestation_Detection_init.py`:
```python
x = 200    # X position of ROI
y = 50     # Y position of ROI
h = 380    # Height of ROI
w = 220    # Width of ROI
```

### Change Green Threshold

Edit `Deforestation_Detection_init.py`:
```python
if(defpercantage < 97):  # Lower = more sensitive, Higher = stricter
```

### Change Alert Threshold

Edit `Deforestation_Detection_init.py`:
```python
if(count >= 150):  # Frames needed to trigger alert
```

### Change Location

Edit `LocationFetcher.py`:
```python
location = geolocator.geocode("Your City Name")
```

---

## Troubleshooting

### Webcam Not Opening

```
Error: cap.isOpened() returns False
```
**Fix:** Change camera index in `Deforestation_Detection_init.py`:
```python
cap = cv2.VideoCapture(0)  # Try 0, 1, 2...
```

### Model Not Found

```
Error: No such file or directory: 'deforestation_trained_data.h5'
```
**Fix:** Ensure model is at `models/deforestation_trained_data.h5` and update path in code.

### WhatsApp Not Sending

```
Error: WhatsApp Web not logged in
```
**Fix:** 
1. Open browser
2. Navigate to web.whatsapp.com
3. Log in with QR scan
4. Keep browser open during detection

### Green Estimator Always 0%

**Fix:** Adjust color thresholds in `GreenEstimator.py`:
```python
if(R <= 110 and G >= 110 and B <= 110):  # Adjust these values
```

### Out of Memory During Training

**Fix:** Reduce batch size:
```python
batch_size = 32  # Instead of 64
```

---

## File Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| `src/Starter.py` | Main entry | Start detection |
| `src/detection/Deforestation_Detection_init.py` | Detection engine | Don't edit unless customizing |
| `src/training/DeForestation_Training.py` | Model trainer | Retrain with new data |
| `src/training/ImageCapturer_For_Training.py` | Data collector | Build dataset |
| `src/utils/GreenEstimator.py` | Pre-filter | Tune sensitivity |
| `src/utils/LocationFetcher.py` | GPS utility | Change location |
| `src/utils/WASender.py` | WhatsApp sender | Configure messaging |
