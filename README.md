# RAG Knowledge Base Assistant

A powerful Retrieval-Augmented Generation (RAG) system that enables users to build and query their own knowledge base from documents. This application uses advanced AI models to process documents, understand questions, and provide accurate answers with source citations.

## Key Features

- **Document Processing**
  - Supports multiple file formats (PDF, TXT, DOCX)
  - Intelligent text chunking for optimal context
  - Automatic metadata extraction and organization

- **Advanced RAG Implementation**
  - Uses state-of-the-art embedding models for semantic search
  - Implements vector database for efficient similarity search
  - Combines multiple AI models for optimal results:
    - Question-answering model (RoBERTa-based)
    - Summarization model (BART-based)
    - Custom embedding generation

- **Smart Query Processing**
  - Natural language question answering
  - Intelligent summarization capabilities
  - Context-aware responses
  - Source citation tracking
  - Confidence scoring for answers

- **User Features**
  - Secure user authentication
  - Document management
  - Interactive web interface
  - Real-time query processing
  - Response time optimization

## Technical Details

The system uses a sophisticated pipeline:
1. Document ingestion and processing
2. Text chunking and embedding generation
3. Vector storage for efficient retrieval
4. Query processing with multiple AI models
5. Response generation with source citations

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your_secret_key_here
```

4. Initialize the database:
```bash
python init_db.py
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
rag-agent-ai/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Project dependencies
├── init_db.py           # Database initialization
├── static/              # Static files (CSS, JS)
├── templates/           # HTML templates
└── src/
    ├── document_processor/  # Document processing modules
    ├── embeddings/         # Embedding generation
    ├── vector_store/       # Vector database operations
    ├── rag/               # RAG implementation
    └── auth/              # Authentication modules
```

## Usage

1. Register a new account or login
2. Upload your documents (PDF, TXT, or DOCX)
3. Wait for document processing (the system will automatically chunk and embed your documents)
4. Ask questions about your documents in natural language
5. Receive answers with:
   - Direct responses to your questions
   - Source citations from your documents
   - Confidence scores
   - Option to request summaries of specific sections

## Advanced Features

- **Smart Summarization**: Ask for summaries of specific sections or entire documents
- **Context-Aware Answers**: The system maintains context from your documents
- **Source Tracking**: Every answer includes references to the source material
- **Performance Optimization**: Built-in timeout handling and response optimization

## License

MIT License 