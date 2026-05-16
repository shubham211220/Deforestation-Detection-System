# System Architecture

## Overview

The Deforestation Detection System is a real-time computer vision application that uses a Convolutional Neural Network (CNN) to classify forest regions as either "Forestation" or "De-Forestation".

## Flow Diagram

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│   START     │───▶│  Webcam      │───▶│  Region of  │───▶│  Resize to  │
│             │    │  Capture     │    │  Interest   │    │  150x150    │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
                                                                │
                                                                ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│   Display   │◀───│  Draw Boxes  │◀───│  CNN Model  │◀───│  Green %    │
│   Result    │    │  & Labels    │    │  Predict    │    │  Check      │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
      │
      ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Deforest.  │───▶│  Send Alert  │───▶│   STOP      │
│  Detected?  │    │  (WhatsApp)  │    │             │
└─────────────┘    └──────────────┘    └─────────────┘
```

## Component Breakdown

### 1. Detection Pipeline (`src/detection/`)

| File | Role |
|------|------|
| `Deforestation_Detection_init.py` | Main loop: capture → preprocess → classify → alert |

**Logic Flow:**
1. Open webcam (`cv2.VideoCapture`)
2. Define ROI (Region of Interest): `x=200, y=50, h=380, w=220`
3. Resize frame to `150x150` (model input size)
4. Check green percentage (`GreenEstimator`)
5. If `< 97%`, run CNN prediction
6. If prediction = 0 (deforestation), trigger alert after 150 consistent frames

### 2. Pre-Filter (`src/utils/GreenEstimator.py`)

**Purpose:** Quick pixel-level check before expensive CNN inference

**Algorithm:**
```
For each pixel (R, G, B):
    If R <= 110 AND G >= 110 AND B <= 110:
        Mark as GREEN (forest)
    Else:
        Mark as WHITE (non-forest)

Green % = (green_pixels / total_pixels) * 100
```

**Why:** Saves computation by skipping CNN on obviously non-forest images

### 3. CNN Model (`src/training/DeForestation_Training.py`)

**Architecture:**
```
Input: 150x150x3 (RGB image)

Conv2D(32) → MaxPool →
Conv2D(32) → MaxPool →
Conv2D(32) → MaxPool →
Flatten → Dense(100) → Dense(1, sigmoid)

Optimizer: Adam
Loss: Binary Crossentropy
Classes: Forestation (1) / De-Forestation (0)
```

**Training:**
- 150 epochs
- Data augmentation: shear, zoom, horizontal flip
- Batch size: 64

### 4. Alert System (`src/utils/`)

| File | Function |
|------|----------|
| `LocationFetcher.py` | Gets coordinates, generates Google Maps URL |
| `WASender.py` | Sends WhatsApp image + message via pywhatkit |

**Alert Message Format:**
```
Deforestation is happening with [X]% at this location:
https://www.google.com/maps/dir/[lat],[long]
```

### 5. Dataset Collection (`src/training/ImageCapturer_For_Training.py`)

**Controls:**
- `SPACE` — Capture image
- `ESC` — Quit

**Output:** `dataset/{train|test}/{Forestation|De-Forestation}/{number}.jpg`

## Data Flow

```
[Webcam] ──▶ [OpenCV Frame] ──▶ [ROI Crop] ──▶ [150x150 Resize]
                                              │
                                              ▼
                                    [GreenEstimator]
                                              │
                                    ┌─────────┴─────────┐
                                    ▼                   ▼
                              [>= 97% Green]      [< 97% Green]
                                    │                   │
                                    ▼                   ▼
                           [Skip: No Forest]    [CNN Model Predict]
                                                      │
                                              ┌───────┴───────┐
                                              ▼               ▼
                                        [Pred = 1]      [Pred = 0]
                                        [Forestation]   [De-Forestation]
                                                              │
                                                              ▼
                                                    [150 frames consistent?]
                                                              │
                                                              ▼
                                                    [YES] ──▶ [Send WhatsApp Alert]
                                                              [Location + Image]
                                                              [Audio Alert]
                                                              [Stop System]
```

## Model Performance

| Metric | Value |
|--------|-------|
| Training Accuracy | ~100% |
| Validation Accuracy | ~100% |
| Training Loss | ~0 |
| Validation Loss | ~0 |

> ⚠️ **Note:** The graphs show perfect accuracy which may indicate overfitting or a very clean dataset. Consider adding more diverse test data.

## File Dependencies

```
Starter.py
    └── Deforestation_Detection_init.py
            ├── GreenEstimator.py
            ├── LocationFetcher.py
            └── WASender.py
                    └── PyWhatKit_DB.txt (logs)

DeForestation_Training.py
    └── dataset/train/, dataset/test/

ImageCapturer_For_Training.py
    └── dataset/{train|test}/{Forestation|De-Forestation}/
```
