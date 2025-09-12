# 🔗 **Cyber Security URL Analyzer – Machine Learning Powered Threat Detection**

## 🌟 **Overview & Impact**

Cybercrime is evolving faster than ever. Phishing, malware, and defacement attacks are becoming increasingly sophisticated, and millions of new malicious URLs are generated every day. Traditional blacklist-based tools often fail to catch these new threats, leaving users vulnerable to identity theft, data breaches, and financial loss.

This project **fills that critical gap** by creating a **Machine Learning powered URL Analyzer** that can:

* Detect malicious URLs **before they even appear in blacklists**
* Accurately separate safe URLs from unsafe ones with **97%+ accuracy**
* Classify unsafe URLs into **Phishing, Malware, and Defacement** with **96%+ precision**
* Identify **over 4400 unsafe URLs more effectively than publicly available models**
* Deploy instantly via **FastAPI backend and intuitive frontend**, making it practical for real-world use

> **Impact:** Protects users proactively from cybercrime. This system is **data-driven, reliable, and highly accurate**, capable of preventing potential cyber threats before they reach victims.

---

## ✨ **Key Features & Highlights**

* **Hierarchical / Cascaded Model Architecture:**

  1. **Random Forest** → Binary classification (Safe vs Unsafe)
  2. **XGBoost** → Multi-class classification (Phishing, Malware, Defacement)

* **Extensive Feature Engineering:**

  * 20+ handcrafted URL-based features extracted for maximum accuracy
  * Includes protocol, domain & subdomain count, path & query length, frequency of special characters, digit/letter ratio, and more
  * Focus on unusual patterns and anomalies, which often signal malicious behavior

* **High Performance:**

  * Overall accuracy: \~97%
  * Precision: \~96%
  * Recall for unsafe URLs: **0.96+**
  * **Successfully segregated over 4400 unsafe URLs** better than existing online models

* **User-Friendly Frontend:**

  * Clean and simple HTML/CSS/JS interface
  * Users can submit URLs and immediately see the safety status

* **Production-Ready Backend:**

  * FastAPI server ensures fast response times
  * Dockerized deployment (\~2GB optimized image) for easy scaling and portability

---

## 🏗️ **System Architecture & Workflow**

<img width="1024" height="1024" alt="workflow" src="https://github.com/user-attachments/assets/28573f05-e992-4d6a-b9a9-a49094557195" />

**How it works:**

1. **User Input:** Enter a URL in the frontend interface.
2. **Feature Extraction:** The URL is parsed into multiple components—protocol, hostname, domain, subdomain, port, path, query, fragment—and additional engineered features are computed.
3. **Binary Classification:** Random Forest predicts whether the URL is safe or unsafe.
4. **Multi-class Classification:** If unsafe, XGBoost classifies the URL into **Phishing, Malware, or Defacement**.
5. **Output:** Results are instantly displayed on the frontend with clear labels.

> **Why this architecture matters:** The hierarchical approach ensures that unsafe URLs are accurately detected first, then further classified, **maximizing recall for threats while maintaining high precision**.

---

## ⚙️ **Tech Stack**

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Machine Learning Models:** Random Forest, XGBoost, LightGBM
* **Data Handling:** Pandas, NumPy
* **Deployment:** Docker (\~2GB optimized image)
* **Training Environment:** Google Colab

---

## 📊 **Dataset & Class Distribution**

* **Source:** Kaggle Phishing/Malware URL dataset (\~651k rows)

* **Columns:**

  * `url` → The raw URL input
  * `label` → Target class (Benign, Phishing, Malware, Defacement)

* **Class Imbalance:**

  * 428k benign URLs
  * \~230k unsafe URLs

* **Approach:** Combined unsafe categories for binary classification, then separated in the second stage for multi-class classification to improve recall

> **Why it matters:** Real-world data is often imbalanced. This approach ensures the system doesn’t miss unsafe URLs while maintaining robust classification for multiple threat types.

---

## 🔬 **Data Preprocessing & Feature Engineering**

* Minimal preprocessing (no missing values)
* Extracted **20+ handcrafted features** relevant to malicious behavior:

  * Protocol type (HTTP/HTTPS)
  * Subdomain & domain characteristics
  * Path and query length
  * Frequency of special characters
  * Ratio of digits to letters
* **Train-Test Split:** 80/20 stratified to maintain class distribution
* **Binary Labeling:** Safe vs Unsafe URLs in first step for hierarchical processing

> **Key Insight:** Instead of converting URLs into embeddings, feature engineering focused on unusual patterns that indicate malicious activity, leading to **better performance than traditional vectorization methods**.

---

## 🤖 **Model Selection & Hierarchical Approach**

**Cascaded Architecture:**

1. **Binary Classification – Random Forest**

   * Predicts Safe vs Unsafe URLs
   * Focused on maximizing **recall** for unsafe URLs
   * Baseline accuracy: \~97%

2. **Multi-class Classification – XGBoost**

   * Classifies unsafe URLs into Phishing, Malware, Defacement
   * Prioritized precision while maintaining high recall
   * Segregated **over 4400 unsafe URLs**, outperforming publicly available models

**Hyperparameter Tuning:**

* RandomizedSearchCV used to optimize recall for unsafe URLs
* Gradient-based models explored (XGBoost, LightGBM) to push classification boundaries
* Trade-off analysis: Focused on recall first, then optimized precision

**Challenges & Achievements:**

* Implemented gradient-based models for the first time in this domain
* Built hierarchical architecture from scratch under **9-5 industry-style constraints**
* Dockerized backend for **scalable, portable deployment**
* Achieved a **robust, high-precision, high-recall solution**, ready for real-world usage

---

## 📈 **Results & Performance**

| Metric                           | Binary (Safe/Unsafe) | Multi-class (Unsafe Types) |
| -------------------------------- | -------------------- | -------------------------- |
| Accuracy                         | 97%                  | 94%                        |
| Precision                        | 96%                  | 95%                        |
| Recall                           | **0.96+**            | 93%                        |
| F1-score                         | 96%                  | 94%                        |
| Unsafe URLs correctly identified | **4400+**            | N/A                        |

> **Remarkable Outcome:** The hierarchical approach ensures high recall for unsafe URLs, proactively catching new threats that single-model systems or traditional blacklists would miss.

---

## 🚀 **How to Run Locally**

1️⃣ **Clone Repository:**

```bash
git clone https://github.com/<your-username>/url-analyzer.git
cd url-analyzer
```

2️⃣ **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3️⃣ **Run FastAPI Server:**

```bash
uvicorn app:app --reload
```

4️⃣ **Open Frontend:**
Visit `http://127.0.0.1:8000` to test your URL Analyzer

---

## 📦 **Future Improvements**

* Implement **feedback loop** to allow continuous model learning from user input
* Add **offline & online inbuilt detection model** for instant evaluation
* Train on **real-world streaming URL data** to dynamically adapt to new threats
* Optimize **Docker image size** for faster deployment
* Develop a **browser extension** or **enterprise API** for wider adoption

---

## 🤝 **Contributing**

Pull requests are welcome! For major changes, open an issue to discuss ideas first.

---

## 📜 **License**

MIT License – free to use and modify

---


---

If you want, I can also **draft a polished GitHub folder structure with placeholders for screenshots, Docker files, ML models, and requirements.txt**, so your repo **looks extremely professional and complete**, making it perfect to share with recruiters.

Do you want me to do that next?
