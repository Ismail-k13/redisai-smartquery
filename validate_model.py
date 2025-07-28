import onnx

try:
    model = onnx.load("model/resnet50.onnx")
    onnx.checker.check_model(model)
    print("✅ ONNX model is valid.")
except Exception as e:
    print(f"❌ ONNX model validation failed: {e}")
