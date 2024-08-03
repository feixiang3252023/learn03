import redis  

# 连接到本地的 Redis 服务器  
r = redis.Redis(host='localhost', port=6379, db=0)  

# 字符串  
r.set('key', 'value')  
print(r.get('key').decode('utf-8'))  

# 列表  
r.lpush('my_list', 'element1')  
r.lpush('my_list', 'element2')  
print([elem.decode('utf-8') for elem in r.lrange('my_list', 0, -1)])  

# 集合  
r.sadd('my_set', 'element1')  
r.sadd('my_set', 'element2')  
print([elem.decode('utf-8') for elem in r.smembers('my_set')])  

# 哈希  
r.hset('my_hash', 'field1', 'value1')  
r.hset('my_hash', 'field2', 'value2')  
print({key.decode('utf-8'): value.decode('utf-8') for key, value in r.hgetall('my_hash').items()})  

# 有序集合  
r.zadd('my_zset', {'element1': 1, 'element2': 2})  
print([(elem.decode('utf-8'), score) for elem, score in r.zrange('my_zset', 0, -1, withscores=True)])