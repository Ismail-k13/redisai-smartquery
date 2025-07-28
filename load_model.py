import redisai as rai
import os

try:
    # Check if ONNX file exists
    model_path = "model/resnet50.onnx"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"❌ Model not found at {model_path}")

    print("📦 ONNX model file found.")

    # Connect to RedisAI
    print("🔌 Connecting to RedisAI at localhost:6379...")
    con = rai.Client(host='localhost', port=6379)
    print("✅ Connected to RedisAI.")

    # Read model
    with open(model_path, "rb") as f:
        model_data = f.read()

    print("📤 Uploading model to RedisAI...")

    # Upload model (correct function is modelset)
    con.modelset(
        'resnet_model',
        backend='onnx',
        device='cpu',
        data=model_data
    )

    print("✅ Model successfully loaded into RedisAI.")

except Exception as e:
    print(f"❌ Error: {e}")
