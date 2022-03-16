# 将数据库query返回的object列表转换为json
def covert_str_to_json(dbrows):
    rows = [row for row in dbrows]
    new_rows = []
    for row in rows:
        data = row.to_dict()
        new_rows.append(data)
    return new_rows