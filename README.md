# 🌡️ Northwest India Weather Prediction with Urbanization Analysis

Welcome to the **Northwest India Weather Prediction** project! This repository contains a Streamlit-based web app for predicting temperatures in the northwest Indian subcontinent with ±4°C precision, using 50 years of data, and analyzing urbanization trends via satellite imagery proxies. 🚀

## 🌟 Project Overview
This project uses an LSTM model (GPU-accelerated) to predict daily temperatures, incorporating urbanization effects. It includes visualizations for temperature trends and urbanization growth, making it interactive and insightful for climate researchers and urban planners.

## 🚀 Getting Started
### Prerequisites
- Python 3.9+
- CUDA-enabled GPU (optional, for faster training)
- Internet connection for initial setup

### Installation
1. Clone this repository:

2. Create a virtual environment:

3. Install dependencies:

## 🛠️ Usage
Run the web app locally:
This will open in your default browser at `http://localhost:8501`. Interact with the app to view predictions and urbanization trends!

## 🔧 Technologies Used
| Library         | Version    | Purpose                     |
|-----------------|------------|-----------------------------|
| Python          | 3.9+       | Core language               |
| PyTorch         | 2.5.1      | LSTM model, GPU acceleration|
| NumPy           | 1.26.0     | Numerical computations      |
| Pandas          | 2.2.0      | Data manipulation           |
| Matplotlib      | 3.8.0      | Plotting                    |
| Scikit-learn    | 1.4.0      | Data preprocessing          |
| Streamlit       | 1.32.2     | Web app interface           |

## ⚡ Shortcuts
- **R**: Rerun the app without resetting session state (press "R" in the browser).
- **F5**: Refresh the browser to reload the app.
- **Ctrl+C**: Stop the Streamlit server in the terminal.
- For custom button shortcuts, install `streamlit-shortcuts` via `pip install streamlit-shortcuts` and follow its documentation.

## 📊 Screenshots
![Climate Prediction Model Image](https://raw.githubusercontent.com/stlala25/PehliAwaaz-Climate_Prediction_Model/master/images.jpeg)

### 🏆 Achievement
The screenshot above, captured on **October 29, 2023**, showcases a key success of our model. It predicted rainfall in **Delhi NCR** after **9 days** (on **November 7, 2023**) with an alpha value of **0.89**, indicating high confidence. This prediction aligned closely with the **India Meteorological Department (IMD)** readings, validating the model’s accuracy and reliability for real-world climate events in the region.

## 🤝 Contributing
Feel free to fork, improve, and submit pull requests! For issues, open a ticket in the Issues tab.

## 📞 Contact
For questions, reach out to [sarthak.a.work@gmail.com].

---

torch==2.5.1
numpy==1.26.0
pandas==2.2.0
matplotlib==3.8.0
scikit-learn==1.4.0
streamlit==1.32.2
Made with ❤️ using Streamlit and PyTorch!
