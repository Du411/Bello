from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Database settings
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')

    # Server settings
    SERVER_HOST = os.getenv('SERVER_HOST')
    SERVER_PORT = int(os.getenv('SERVER_PORT'))


##Test
print("=== Environment Variables ===")
print(f"DB_NAME: {Config.DB_NAME}")
print(f"DB_USER: {Config.DB_USER}")
print(f"DB_PASSWORD: {Config.DB_PASSWORD}")
print(f"DB_HOST: {Config.DB_HOST}")
print(f"DB_PORT: {Config.DB_PORT}")
print(f"SERVER_HOST: {Config.SERVER_HOST}")
print(f"SERVER_PORT: {Config.SERVER_PORT}")
print("==========================")