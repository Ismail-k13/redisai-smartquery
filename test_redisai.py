import redisai as rai

# Connect to RedisAI
con = rai.Client(host='localhost', port=6379)

print("Connected:", con.ping())

# List all Redis keys (models, tensors, scripts, etc.)
print("All Redis Keys:")
for key in con.scan_iter():
    print("-", key.decode())
