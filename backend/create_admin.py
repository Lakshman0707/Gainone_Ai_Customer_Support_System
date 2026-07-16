from authentication.auth import hash_password
from app.database import SessionLocal
from models.admin import Admin

db = SessionLocal()

password = hash_password("1234")

print("Generated Hash:", password)

new_admin = Admin(
    name="Nandita",
    email="admin@gainone.com",
    password=password
)

db.add(new_admin)
db.commit()

print("Admin Created Successfully")

db.close()