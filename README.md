## Cross-Language Personalization for Dataset Selection Using BAAI
General Embedding  

This repository provides a **Dataset Recommender System** that uses Flask for a web interface, LangChain for dataset recommendations, and integrates with **Astra DB**, **Groq API**, Hugging Face models, and a custom **translation module** for multilingual support.  

---

## **Features**  
- **Web Interface with Flask**: User-friendly interface for dataset recommendations.  
- **Multilingual Query Support**: Translate user queries into English using the `translator.py` module.  
- **Scraping Dataset Metadata**: Collect dataset details from specified URLs.  
- **Storage with Astra DB**: Scalable database for storing dataset metadata.  
- **Recommendation Engine**: Generate dataset recommendations using LangChain.  
- **Advanced Querying**: Utilize Groq API and Hugging Face models for enhanced query capabilities.  

---

## **Architecture**  

![screenshot](https://github.com/shuvo-dotcom/dataset-recomender/blob/main/static/Screenshot%202024-11-29%20at%2010.04.14%E2%80%AFPM.png)

1. **Web Scraping**: Extract dataset descriptions and metadata from URLs.  
2. **Astra DB Integration**: Store and retrieve dataset metadata for efficient querying.  
3. **Flask Web App**: Serve the recommendation engine through a web interface.  
4. **Translator Module**:  
   - Use `translator.py` to support multilingual queries by translating them into English.  
5. **LangChain + Groq API + Hugging Face Integration**:  
   - Generate personalized recommendations and enhance query handling.  

---

## **Installation**  

### **Prerequisites**  
- Python 3.8+  
- Astra DB account (sign up [here](https://www.datastax.com/astra))  
- Groq API key (sign up [here](https://groq.com/))  
- Hugging Face account and API token (sign up [here](https://huggingface.co/))  

### **Steps**  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/dataset-recommender.git
   cd dataset-recommender
   ```  

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Set up Astra DB**  
   - Create a database in Astra DB.  
   - Download the secure connect bundle and place it in the project root.  
   - Update the `.env` file with your database details.  

4. **Configure API keys**  
   Add your Astra DB, Groq API, and Hugging Face credentials to the `.env` file:  
   ```env
   ASTRA_DB_BUNDLE_PATH=./secure-connect-database.zip
   GROQ_API_KEY=your_groq_api_key
   HF_API_TOKEN=your_huggingface_api_token
   ```  

5. **Run the application**  
   Start the Flask web application:  
   ```bash
   python app.py
   ```  

---

## **Usage**  

### **Access the Web Interface**  
1. Launch the Flask app by running `python app.py`.  
2. Open your browser and navigate to `http://127.0.0.1:5000`.  

### **Features Available in the Web App**  
- **Scrape Dataset Metadata**: Upload URLs to scrape dataset metadata.  
- **Multilingual Query Translation**: Submit queries in your preferred language; the `translator.py` module will translate them to English.  
- **Generate Recommendations**: Enter queries like "datasets for text classification" to receive recommendations.  
- **Advanced Queries**: Use enhanced query capabilities powered by Groq API and Hugging Face.  

---

![screenshot](https://github.com/shuvo-dotcom/dataset-recomender/blob/main/static/Screenshot%202024-11-29%20at%2010.13.38%E2%80%AFPM.png)

## **Folder Structure**  

```
dataset-recommender/
├── app.py                # Main Flask application
├── translator.py         # Multilingual translation module
├── templates/            # HTML templates for the web interface
├── static/               # Static files (CSS, JS, images)
├── scraping/             # Web scraping module
├── langchain/            # LangChain configuration and pipelines
├── astra_db/             # Astra DB integration scripts
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables
```  

---

## **Contributing**  

1. Fork the repository.  
2. Create a new feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m 'Add some feature'`).  
4. Push to the branch (`git push origin feature-name`).  
5. Open a Pull Request.  

---

## **License**  

This project is licensed under the MIT License. See `LICENSE` for more details.  

---

## **Contact**  
For questions or suggestions, reach out to:  
- **Author**: Suvajit Lodh  
- **LinkedIn**: [Suvajit Lodh](https://www.linkedin.com/in/suvajitlodh)  
- **Email**: reachshuvojit@gmail.com  

---  

Happy Recommending! 😊  

Let me know if you'd like further refinements!
