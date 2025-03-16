# GDGoC Competition


## 1. Guide
Step 1: Create env
```bash
python3 -m venv venv
```
Step 2: Install library
```bash
pip install -r requirements.txt
```
Step 3: Run file convert_data2images.py
```bash
python3 convert_data2images.py
```
## Data folder struct
---
```
data
├── test
│   └── PDF
└── train
    ├── JSON
    └── PDF
```

After run convert_data22images.py:
```
data
├── images
│   ├── test
│   └── train
├── test
│   └── PDF
└── train
    ├── JSON
    └── PDF
```