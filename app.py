import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from src.auth.auth import init_db, get_user_by_id, create_user, get_user_by_username
from src.rag.rag_engine import RAGEngine
from config import Config
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
init_db(app)

# Initialize RAG engine
rag_engine = RAGEngine()

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        user = create_user(username, email, password)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        flash('Username already exists')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            logger.info(f"Processing uploaded file: {filename}")
            rag_engine.add_document(filepath)
            return jsonify({'message': 'File processed successfully'})
        except Exception as e:
            logger.error(f"Error processing file: {str(e)}", exc_info=True)
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/ask', methods=['POST'])
@login_required
def ask_question():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400
    
    try:
        logger.info(f"Processing question: {data['question']}")
        start_time = time.time()
        
        # Set a timeout of 30 seconds
        timeout = 30
        result = rag_engine.process_query(data['question'])
        
        processing_time = time.time() - start_time
        logger.info(f"Question processed in {processing_time:.2f} seconds")
        
        if processing_time > timeout:
            logger.warning(f"Processing took longer than {timeout} seconds")
            return jsonify({
                'error': 'Processing took too long. Please try a more specific question or summarize a smaller portion of the text.'
            }), 408
        
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}", exc_info=True)
        return jsonify({
            'error': 'An error occurred while processing your question. Please try again with a different question or format.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 