apt-get update && apt-get install -y python3-pip

pip install -r requirements.txt
python3.9 manage.py collectstatic