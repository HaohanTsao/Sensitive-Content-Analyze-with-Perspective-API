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

| index | value |
|------|----|
| True Positive | 15 |
| True Negative | 230 |
| False Positive | 0 |
| False Negative | 2 |

| index | value |
|------|----|
| Accuracy | 0.9924 |
| Recall | 0.8824 |
| Precision | 1.0000 |
| F1 Score | 0.9375 |

