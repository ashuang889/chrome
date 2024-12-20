import plyvel

# 指定你的 LevelDB 数据库路径
db_path = '/path/to/your/LocalStorage/leveldb'

# 打开数据库
db = plyvel.DB(db_path, create_if_missing=False)

# 遍历数据库中的所有键值对
for key, value in db:
    print(f"Key: {key}, Value: {value}")

db.close()