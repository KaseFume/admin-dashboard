python3 -m venv venv          # Create a virtual environment using python3
source venv/bin/activate       # Activate the virtual environment
pip install -r requirements.txt # Install dependencies
python3 manage.py collectstatic --noinput # Collect static files