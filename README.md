# Sensitive-Content-Analyze-with-Perspective-API

This project utilizes the Perspective API by Google to analyze and detect sensitive content in text.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/HaohanTsao/Sensitive-Content-Analyze-with-Perspective-API.git
    cd Sensitive-Content-Analyze-with-Perspective-API
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Setting up API Key

1. Create a `.env` file in the root directory.

2. Add your Google Cloud Platform (GCP) API key to the `.env` file:

    ```env
    API_KEY=your_GCP_api_key_here
    ```

    Replace `your_GCP_api_key_here` with your actual GCP API key.

## Usage
Checkout and run the `quickstart.py` to try:

```bash
python quickstart.py
```

## Test

| Actual / Predicted | Predicted Positive (1) | Predicted Negative (0) |
|--------------------|------------------------|------------------------|
| Actual Positive (1) | 15 (TP)                | 2 (FN)                 |
| Actual Negative (0) | 0 (FP)                 | 230 (TN)               |

