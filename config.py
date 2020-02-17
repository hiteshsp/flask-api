import os
DYNAMODB_TABLE=os.environ.get("TABLE_NAME")
SECRET_KEY=os.urandom(16)