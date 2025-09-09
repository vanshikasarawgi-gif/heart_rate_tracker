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

2. Enter heart rate → click **Add heart rate**.
3. Use buttons to see **Average**, **Max**, **Min**, or **Graph**.
4. Non-numeric input triggers an error popup automatically.
5. Uses Matplotlib to plot the graph

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
