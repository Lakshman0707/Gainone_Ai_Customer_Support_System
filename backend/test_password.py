from authentication.auth import verify_password

hashed_password = "$2b$12$W2pPj3eL4t1mQm2R2dLQ4eQj3gD8g0J4P0xP5F5VhN7xO9iL2mC2K"

print(verify_password("1234", hashed_password))