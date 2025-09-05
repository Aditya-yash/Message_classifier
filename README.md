# Message_classifier
It classifies messages as spam or not spam
1. **Get the dataset**
- Download the SMS Spam Collection dataset from UCI and place file at `backend/data/SMSSpamCollection`.
2. **Train**
- `cd backend`
- `python3 -m venv venv && source venv/bin/activate`
- `pip install -r requirements.txt`
- `python train.py` (creates `model.joblib`)
3. **Run with Docker Compose (locally)**
- `docker-compose up --build`
- frontend available at `http://localhost/` and backend at `http://localhost:5000/api/predict`


4. **Deploy on AWS EC2 (summary)**
- Launch an EC2 instance (Ubuntu or Amazon Linux 2).
- Create a Security Group that allows inbound 22 (SSH), 80 (HTTP) and any other ports you need.
- SSH into instance, install Docker & Docker Compose (or use Amazon Linux `amazon-linux-extras install docker`).
- `git clone` this repo on the instance, run `docker-compose up -d --build`.
- Point your domain or public IP to the instance.
