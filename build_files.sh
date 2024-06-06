# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip within the virtual environment
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip install -r requirements.txt
python3.9 manage.py collectstatic