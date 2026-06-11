import json
import boto3
from faker import Faker
from datetime import datetime
import random

fake = Faker()
s3 = boto3.client('s3')
BUCKET = "stap-raw-data-yourname"

def generate_order():
    return {
        "order_id": random.randint(1000, 9999),
        "customer_id": random.randint(1, 200),
        "product_id": random.randint(1, 50),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(10, 200), 2),
        "order_ts": datetime.now().isoformat()
    }

def upload_to_s3(orders, date_str):
    key = f"orders/dt={date_str}/orders_{date_str}_{random.randint(1,100)}.json"
    body = "\n".join([json.dumps(o) for o in orders])  # JSON lines format
    s3.put_object(Bucket=BUCKET, Key=key, Body=body)
    print(f"Uploaded {len(orders)} orders to s3://{BUCKET}/{key}")

if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    orders = [generate_order() for _ in range(200)]   # simulate 200 orders
    upload_to_s3(orders, today)