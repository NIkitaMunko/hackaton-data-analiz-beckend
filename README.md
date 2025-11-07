Getting Started
Run the backend server

From the project root, start the FastAPI server:

uvicorn server.server:app --reload

Test API requests

You can quickly test backend responses using a simple Node.js script:

cd server/test-requests
node index.js


This sends test requests to the FastAPI backend and logs the responses.

Project structure
hackaton-data-analiz-beckend/
│
├── server/                 # Backend API (FastAPI)
│   ├── server.py           # Main API entry point
│   └── test-requests/      # Node.js scripts to test API endpoints
│
├── llm/                    # Local LLM logic (inference, model handling)
│   ├── inference.py
│   └── llm.py
│
├── dataset/                # Datasets and training data
│   └── receipts.csv
│
└── README.md               # Project documentation