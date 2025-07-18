<p align="center">
  <img src="docs/logo.png" alt="Open Rotor Copilot Logo" width="180"/>
</p>

<h1 align="center">Open Rotor Copilot: Neural Blackbox Analysis</h1>

<p align="center">
  <strong>AI-powered issue detection for FPV flight logs</strong><br/>
  Learn from flights. Parse telemetry. Find what went wrong.
</p>

---

## ✨ What is this?

**Open Rotor Copilot AI** is the brain of your drone's Copilot.  
It uses **language models (LLMs)** to analyze parsed Betaflight log data — identifying issues like:

- 🌀 Prop wash
- 🚨 Bad PID tuning or I-term windup
- 🛰️ GPS lock loss or unsafe RTH
- 🔋 Voltage sags and current spikes
- 🧭 Yaw drift or gyro instability

Whether you're flying freestyle, racing, or mapping, Copilot helps you **learn from your flight behavior automatically**.

---

## 🧠 How It Works

This module takes **structured telemetry** (parsed from `.bbl` logs) and feeds it into a **locally trained LLM** to detect flight issues.

You control the:
- 💾 Input format (CSV or JSON from parser)
- 🏷️ Labeled data for training
- 🔍 Inference backend (e.g. Hugging Face, local transformers)

---

## 📥 Input Format (Example)

Each flight log is parsed to rows like:

```csv
"loopIteration","time","axisP[0]","axisP[1]","axisP[2]","axisI[0]",...,"gpsDistance","gpsHomeAzimuth"
0,173075191,0,1,0,0,0,0,-1,0,...,0.0,0.0
4,173076431,0,1,0,0,0,0,-1,1,...,1.73e-10,340.2
```

or

```json
{
  "header": {
    "firmware": "Betaflight 4.5.1",
    "board": "SPEEDYBEEF7V3",
    "datetime": "2024-07-31T18:10:49Z",
    "gps_rescue": true
  },
  "frames": [
    { "time": 173075191, "axisP": [0,1,0], "motor": [348,348,...], "GPS_numSat": 8 },
    ...
  ]
}
```

## 🧠 Output

```json
[
  "prop wash detected on descent",
  "GPS rescue triggered with low satellite count",
  "I-term windup during throttle oscillation",
  "minor vibration on pitch axis during flip"
]
```

You can also configure outputs to include:
- 🕓 Time ranges (when issue happened)
- 🚦 Severity scores
- 📍 GPS location (if available)