import pandas as pd
import json

# CSVファイルからデータを読み込む
data = pd.read_csv("typhoon-position_converted_2001-2023.csv")

# GeoJSONオブジェクトを初期化
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# 台風番号と台風名でデータをグループ化
grouped = data.groupby(['台風番号', '台風名'])

# 各台風の経路をLineStringとしてGeoJSONに追加
for (num, name), group in grouped:
    line = {
        "type": "Feature",
        "properties": {
            "台風番号": str(num),  # 台風番号を文字列に変換
            "台風名": name
        },
        "geometry": {
            "type": "LineString",
            "coordinates": group[['経度', '緯度']].values.tolist()
        }
    }
    geojson["features"].append(line)

# 生成したGeoJSONデータをファイルに保存
with open("typhoon-position_converted_paths_2001-2023.geojson", 'w', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False)
