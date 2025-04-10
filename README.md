# Pump Longevity Tester

This is a Python script built for Raspberry Pi 5 to test the life expectancy of two pumps. It controls the pumps using GPIO pins and relays, and logs operational data to a CSV file for long-term analysis.

## 🧪 Purpose

The goal of this project is to run two pumps over extended periods and monitor their performance and longevity. This can help identify which pump lasts longer or if any failure patterns emerge over time.

## ⚙️ Features

- Controls two pumps via GPIO and relays
- Supports two test modes:
  - **Continuous Run**: Pumps run without stopping
  - **Timed Cycle**: Pumps run for 3 seconds, pause for 2 seconds
- Logs run data to a CSV file, including:
  - Timestamp
  - Runtime duration
  - Flow rate
  - Volume

## 📁 Logged Data

The script outputs a CSV file (e.g., `data/data.csv`) that contains time-series data of pump activity. This can be used for further analysis or troubleshooting.

## 📌 To-Do

- Add hardware setup instructions
- Implement alert/notification for pump failures
- Add option to upload logs to cloud storage (e.g., Google Drive, Dropbox)
- Include GUI or web dashboard for real-time monitoring

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Created with ❤️ using Raspberry Pi 5 and Python
