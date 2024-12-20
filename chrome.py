import plyvel
import json

def export_to_json(db_path, output_file):
    try:
        db = plyvel.DB(db_path, create_if_missing=False)
        data = {}
        
        for key, value in db:
            data[key.decode('utf-8', 'ignore')] = value.decode('utf-8', 'ignore')
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"数据已导出到 {output_file}")
        db.close()
    except Exception as e:
        print(f"导出失败: {e}")

if __name__ == "__main__":
    db_path = '/tool/leveldb/chrome/leveldb'  # 替换为你的 LevelDB 文件路径
    output_file = 'leveldb_data.json'          # 输出文件路径
    export_to_json(db_path, output_file)
