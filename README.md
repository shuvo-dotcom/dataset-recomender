# Dataset Recomender 

This repository provides a **Dataset Recommender System** that uses LangChain for generating recommendations, web scraping for gathering dataset details, **Astra DB** for storing and managing the dataset metadata, and integrates with **Groq API** and Hugging Face models for enhanced query capabilities. 

---

## Features
- **Scraping Dataset Metadata**: Collect dataset details from specified URLs using web scraping techniques.
- **Storage with Astra DB**: Store and manage scraped data in Astra DB, a scalable and serverless database.
- **Recommendation Engine**: Generate dataset recommendations using LangChain.
- **Query Enhancement**: Leverage Groq API and Hugging Face (HF) models to refine recommendations and answer user queries.

---

## Architecture

![screenshot](https://github.com/shuvo-dotcom/dataset-recomender/blob/main/static/Screenshot%202024-11-29%20at%2010.04.14%E2%80%AFPM.png)

1. **Web Scraping**: Extract dataset descriptions and metadata from target URLs.
2. **Astra DB Integration**: Save scraped data in Astra DB for persistence and efficient querying.
3. **LangChain Recommendation**: Build conversational recommendations using LangChain's robust chaining capabilities.
4. **Groq API + HF Integration**:
   - Use **Groq API** for structured querying and transformations.
   - Utilize Hugging Face models for natural language processing to enhance user interactions.

---

## Installation

### Prerequisites
- Python 3.8+
- Astra DB account (sign up [here](https://www.datastax.com/astra))
- Groq API key (sign up [here](https://groq.com/))
- Hugging Face account and API token (sign up [here](https://huggingface.co/))

### Steps
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
   - Add your Groq API key and Hugging Face API token to the `.env` file:
     ```env
     ASTRA_DB_BUNDLE_PATH=./secure-connect-database.zip
     GROQ_API_KEY=your_groq_api_key
     HF_API_TOKEN=your_huggingface_api_token
     ```

5. **Run the setup script**
   ```bash
   python setup.py
   ```

---

## Usage

### Step 1: Scrape URLs for Dataset Metadata
Use the scraping module to gather dataset metadata from a list of URLs:
```bash
python scrape_urls.py --urls "https://example.com/dataset1,https://example.com/dataset2"
```

### Step 2: Store Data in Astra DB
The scraped metadata is automatically stored in Astra DB for easy retrieval.

### Step 3: Generate Recommendations
Run the recommendation engine:
```bash
python recommend.py --query "datasets for natural language processing"
```

### Step 4: Query Using Groq API and HF
Use advanced query capabilities:
```bash
python enhanced_query.py --query "What is the best dataset for text classification?"
```

![screenshot](https://github.com/shuvo-dotcom/dataset-recomender/blob/main/static/Screenshot%202024-11-29%20at%2010.13.38%E2%80%AFPM.png)
---

## Folder Structure
```
dataset-recommender/
├── scrape_urls.py         # Module for scraping dataset metadata
├── recommend.py           # Recommendation engine using LangChain
├── enhanced_query.py      # Advanced querying using Groq API and HF
├── astra_db/              # Astra DB integration scripts
├── langchain/             # LangChain configuration and pipelines
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .env                   # Environment variables
```

---

## Contributing
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Contact
For questions or suggestions, reach out to:
- **Author**: Suvajit Lodh  
- **LinkedIn**: [Suvajit Lodh](https://www.linkedin.com/in/suvajitlodh)  
- **Email**: reachshuvojit@gmail.com

--- 

Happy Recommending! 😊