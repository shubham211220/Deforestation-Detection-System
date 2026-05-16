# Dataset Directory

Organize your training and test images here.

## Required Structure

```
dataset/
├── train/
│   ├── Forestation/
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   └── ...
│   └── De-Forestation/
│       ├── 1.jpg
│       ├── 2.jpg
│       └── ...
└── test/
    ├── Forestation/
    │   ├── 1.jpg
    │   └── ...
    └── De-Forestation/
        ├── 1.jpg
        └── ...
```

## Guidelines

- **Minimum**: 100 images per class
- **Recommended**: 500+ images per class
- **Format**: JPG, PNG
- **Size**: 150x150 (will be resized if different)
- **Balance**: Keep train/test ratio at 80/20

## Capture Tool

Use the built-in capture tool:
```bash
python src/training/ImageCapturer_For_Training.py
```
