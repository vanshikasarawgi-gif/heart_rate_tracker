# ❤️ Heart Rate Tracker

A **Python GUI app** to track, analyze, and visualize heart rate data over time. Built with **Tkinter**, **CSV**, and **Matplotlib**.

---

## **✨ Features**

* Add new heart rate entries with timestamps.
* Automatic warnings for **high (>100 bpm)** and **low (<60 bpm)** heart rates.
* View **average**, **maximum**, and **minimum** heart rates.
* Plot a **graph** of heart rate over time (last 20 entries).
* Stores data in `heart_rate.csv`.

---

## **💻 Usage**

1. Run the app:

```bash
python main.py
```

2. Enter your heart rate in the input box and click Add heart rate.

3. Use the buttons to:

   . Average heart rate → shows average bpm and normal/out-of-range status.

   . Maximum heart rate → shows highest recorded bpm and timestamp.

   . Minimum heart rate → shows lowest recorded bpm and timestamp.

   . Show Graph → plots the heart rate over time.

4. Warnings pop up if heart rate is high or low.

5. Invalid input (non-numeric) is automatically caught and shows an error.

---

## **📁 File Structure**

```
heart-rate-tracker/
├── main.py               # Main code
├── heart_rate.csv        # CSV data (auto-generated)
├── heart.png             # GUI image
└── README.md             # Project description
```

---
