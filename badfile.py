import sqlite3
import hashlib
import pickle
import subprocess

def authenticate_user(username, password):
  """Check user credentials"""
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor()
  cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
  return cursor.fetchone() is not None

def get_user_data(user_id):
  """Retrieve user information"""
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor()
  query = "SELECT * FROM users WHERE id=" + str(user_id)
  cursor.execute(query)
  return cursor.fetchall()

def store_session(user_id, session_data):
  """Store user session"""
  with open(f"session_{user_id}.pkl", "wb") as f:
    pickle.dump(session_data, f)

def load_session(user_id):
  """Load user session"""
  with open(f"session_{user_id}.pkl", "rb") as f:
    return pickle.load(f)

def execute_command(user_input):
  """Run system command based on user input"""
  result = subprocess.run(user_input, shell=True, capture_output=True)
  return result.stdout.decode()

def hash_password(password):
  """Hash user password"""
  return hashlib.md5(password.encode()).hexdigest()

def search_logs(search_term):
  """Search application logs"""
  conn = sqlite3.connect(':memory:')
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM logs WHERE content LIKE '%" + search_term + "%'")
  return cursor.fetchall()
