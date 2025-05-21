# 📧 Spam Detection API (Python + FastAPI)

A beginner-friendly machine learning API that detects whether a given text message is **SPAM** or **NOT SPAM**, using:

* Python 🐍
* Scikit-learn 🤖
* FastAPI 🚀
* TF-IDF Vectorization
* Naive Bayes Classifier

---

## 🗂️ Project Structure

```
spam_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── routes/
│   │   └── spam.py          # API endpoint(s)
│   ├── models/
│   │   └── request.py       # Input validation models
│   ├── services/
│   │   └── spam_detector.py # Core ML logic
│   └── utils/
│       └── model_loader.py  # Load vectorizer & model
│
├── data/
│   └── spam_data.tsv        # Your dataset
├── model/
│   ├── vectorizer.pkl       # Saved TF-IDF vectorizer
│   └── spam_model.pkl       # Trained model
├── trainModel.py
├── spam_data.py
├── requirements.txt         # Packages
└── README.md                # Optional docs
```

---

## 📦 Setup Instructions

### ✅ Prerequisites

* Python 3.8 or newer
* pip (Python package installer)

### 🔧 Step-by-step

```bash
# 1. Clone the repository (or download manually)
git clone https://github.com/obirikan/spam_classifer_api.git
cd spam_api

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure the dataset is available
# Make sure 'spam_data.tsv' is in the project root folder

# 5. Train the model
python trainModel.py

# 6. Run the FastAPI app
uvicorn api.main:app --reload
```

---

## 🔍 API Usage

### 📬 Endpoint: `POST /predict`

**Request Body (JSON):**

````json
{
  "message": "Congratulations! You've won a free ticket!"
}

**Response:**
```json
{
  "prediction": "spam"
}
````

---

## 🧠 How It Works

* **TF-IDF** is used to convert text messages into numerical vectors.
* A **Multinomial Naive Bayes** classifier is trained on the vectorized data.
* FastAPI handles HTTP requests and returns predictions in real-time.

---

## 📁 Dataset Info

This project uses the [SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection).

* Format: TSV (Tab-separated)
* Labels: `ham` (not spam), `spam`

Make sure to rename the downloaded file to `spam_data.tsv` and place it in the root directory.

---

## ✍️ Author

* Name: obirikan
* GitHub: [obirikan](https://github.com/obirikan)

---

## ✅ To-Do

* [ ] Add frontend (optional)
* [ ] Add logging and error handling
* [ ] Deploy to cloud (e.g., Render, Vercel, Railway)

---

## 📜 License

MIT License
