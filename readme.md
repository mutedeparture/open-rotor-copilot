<p align="center">
  <img src="docs/logo.png" alt="Open Rotor Copilot Logo" width="180"/>
</p>

<h1 align="center">Open Rotor Copilot: Neural Blackbox Analysis</h1>

<p align="center">
  <strong>AI-powered issue detection for FPV flight logs</strong><br/>
  Learn from flights. Parse telemetry. Find what went wrong.
</p>

---

## What is this?

**Open Rotor Copilot AI** is an open-source LLM-driven project focused on interpreting drone telemetry, assisting with diagnostics, and providing actionable insights for both pilots and developers.

- Flight Log Analysis: Input drone logs (Betaflight Blackbox and similar), receive instant, natural language feedback on issues and flight performance.

- Feature-rich: Supports a wide set of aggregated features including gyro statistics, RC command metrics, voltage behavior, motor outputs, GPS, RSSI, accelerometer patterns, and more.

- Windowed Reasoning: Breaks logs into time windows, analyzes events in context, and describes conditions using human-friendly language.

- Compositional Explanations: For each window, outputs a concise, context-aware reason describing any detected issue or anomaly.

- Flexible, Extensible: Built for integration into other open drone ecosystems or research workflows.


---

## How It Works

This module takes **structured telemetry** (parsed from `.bbl` logs) and feeds it into a **locally trained LLM** to detect flight issues. For each segment, receive an explanation such as:

```bash
"Excessive vibration (gyro_std=123.56); Battery voltage sagged (vbat_drop=0.91V); Motor difference high (motor_diff_max=49.18)"
```

## Features

- 🛠️ Compatible with Drone Logs: Parses and processes logs from real flights or simulations

- 🧠 LLM-Friendly Inputs: Each window formatted as a descriptive string—ready for Hugging Face and other ML frameworks

- 💬 Human-Centric Reasons: Outputs are concise and helpful, designed for pilots, engineers, and AI systems alike

- 🔬 Advanced Feature Set: See below for the full list!

- 🤗 Hugging Face Ready: Designed for easy use with Hugging Face datasets and transformers

---

## Inference

```bash
pip install datasets transformers
```

### Using Fine-tune the Model

```python
from transformers import pipeline

# Load from Hugging Face model repo (after you train & push!)
pipe = pipeline("text2text-generation", model="rbarac/open-rotor-copilot")

# Example input string (from dataset)
test_input = "avg gyro_std = 32.8, motors_min = 15.8, vbat_drop = 0.91, ... (all your features)"
prompt = f"Flight log: {test_input}\nExplain:"

result = pipe(prompt)
print(result[0]['generated_text'])
```

