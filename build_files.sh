python3 -m venv venv                  # Create a virtual environment
source venv/bin/activate               # Activate the virtual environment

# Install each package explicitly
pip install asgiref==3.8.1
pip install Django==5.1.2
pip install django-otp==1.5.4
pip install numpy==2.1.0
pip install pandas==2.2.3
pip install python-dateutil==2.9.0.post0
pip install pytz==2024.2
pip install sqlparse==0.5.1
pip install tzdata==2024.1
pip install whitenoise==6.8.2
pip install XlsxWriter==3.2.0
pip install zipp==3.20.0

# Collect static files for Django
python3 manage.py collectstatic --noinput
