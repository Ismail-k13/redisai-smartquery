import redisai as rai

# Connect to RedisAI
con = rai.Client(host='localhost', port=6379)

# Ping RedisAI to check connection
print("✅ Connected to RedisAI")
