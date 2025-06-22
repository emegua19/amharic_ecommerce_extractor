# Amharic E-commerce Data Extractor - Interim Report

##  Project Overview

This repository contains the interim submission for the **10 Academy Artificial Intelligence Mastery Program**, focused on the **"Building an Amharic E-commerce Data Extractor"** project ( **18 June – 24 June 2025**).

The project's objective is to build a system for **EthioMart** to consolidate **Telegram-based e-commerce data in Ethiopia**, extracting key entities like:

-  Product
-  Price
-  Location

using **Named Entity Recognition (NER)**. The data will eventually support a **FinTech vendor scorecard** for micro-lending.

### This interim report covers:
- **Task 1**: Data Ingestion and Preprocessing from Telegram channels  
- **Task 2**: Labeling a subset of the dataset in CoNLL format

---

##  Interim Submission Details

- **Date:** June 22, 2025, 20:00 UTC (11:00 PM EAT)
- **Deliverables:**
  - GitHub repository with code for Tasks 1 and 2
  - 1–2 page PDF summarizing data preparation and labeling at:  
    `reports/interim_report.pdf`

---

##  Folder Structure

```

/amharic\_ecommerce\_extractor
├── /src
│   ├── data\_handler.py         # Telegram scraping & preprocessing
│   ├── labeler.py              # CoNLL labeling
│   ├── ner\_model.py            # NER model logic (pending)
│   ├── interpreter.py          # Interpretability (pending)
│   └── vendor\_analytics.py     # Vendor scorecard logic (pending)
├── /utils
│   ├── config.py               # Config management
│   ├── logger.py               # Logging utility
│   └── amharic\_processor.py    # Amharic text normalization/tokenization
├── /data
│   ├── /raw                    # Raw Telegram data
│   ├── /processed              # Preprocessed and labeled CoNLL data
│   └── /metadata               # Telegram post metadata
├── /models
│   ├── /finetuned              # Fine-tuned models (pending)
│   └── /checkpoints            # Training checkpoints (pending)
├── /tests
│   ├── test\_data\_handler.py    # Unit tests for scraping
│   ├── test\_labeler.py         # Unit tests for labeling
│   └── test\_\*.py               # Placeholders for pending tests
├── /scripts
│   ├── run\_pipeline.py         # Run Tasks 1 and 2
│   └── run\_analytics.py        # For analytics (pending)
├── README.md                   # Project README
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignore rules
└── config.yaml                 # Telegram & channel configs

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd amharic_ecommerce_extractor
````

### 2. Install Dependencies

Ensure Python 3.10+ is installed, then:

```bash
pip install -r requirements.txt
```

Make sure the following packages are in `requirements.txt`:

```txt
telethon
pandas
pytest
pytest-mock
```

### 3. Configure the Project

Edit `config.yaml`:

```yaml
telegram:
  session_name: "session_name"
  api_id: your_api_id
  api_hash: your_api_hash

channels:
  - "t.me/Shageronlinestore"
  - "t.me/OtherChannel1"
  - "t.me/OtherChannel2"
  - "t.me/OtherChannel3"
  - "t.me/OtherChannel4"
```

Update `.gitignore`:

```
/data/raw/*
/data/metadata/*
/models/*
config.yaml
*.pyc
__pycache__/
```

### 4. Run the Pipeline

```bash
python -m scripts.run_pipeline
```

This will:

* Scrape messages from Telegram
* Preprocess Amharic text
* Label data into CoNLL format
  Output saved in: `data/processed/`

### 5. Run Tests

```bash
pytest tests/
```

---

##  Interim Progress

###  Task 1: Data Ingestion and Preprocessing

* **Implemented via:** `DataHandler` in `src/data_handler.py`
* **Channels:** Scrapes from 5+ Telegram channels listed in `config.yaml`
* **Text Handling:** Normalized and tokenized by `AmharicProcessor`
* **Output:** `data/processed/preprocessed_data.csv`
  *(includes tokens, views, timestamps)*
* **Status:**  Completed

---

###  Task 2: Labeling in CoNLL Format

* **Implemented via:** `Labeler` in `src/labeler.py`
* **Input:** `labeled_telegram_product_price_location.txt`
* **Output:** `data/processed/labeled_data.conll`
  *(Tagged with `B-PRICE`, `B-PRODUCT`, `B-LOCATION`, etc.)*
* **Status:**  Completed (30–50 labeled samples)

---

##  Next Steps

*  **Task 3–6:**

  * Implement `ner_model.py` for Amharic NER model
  * Add `interpreter.py` for SHAP or LIME-based interpretability
  * Finalize `vendor_analytics.py` for FinTech scoring
