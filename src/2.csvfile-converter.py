import pandas as pd

# CSVファイルの読み込み（'台風番号'と'台風名'を文字列として読み込む）
typhoon_data = pd.read_csv(
    "typhoon-position_2001-2023.csv", dtype={'台風番号': str, '台風名': str})

# UTCの日時を作成
typhoon_data['日時（UTC）'] = pd.to_datetime(typhoon_data[['年', '月', '日']].astype(str).agg('-'.join, axis=1) + ' ' +
                                         typhoon_data['時（UTC）'].astype(str) + ':00')

# UTCをJSTに変換
typhoon_data['日時（JST）'] = typhoon_data['日時（UTC）'] + pd.Timedelta(hours=9)

# 必要な列を選択
formatted_typhoon_data_extended = typhoon_data[[
    '日時（JST）', '日時（UTC）', '台風番号', '台風名'] + list(typhoon_data.columns[6:-2])]

# データをCSVファイルとして出力
formatted_typhoon_data_extended.to_csv(
    "typhoon-position_converted_2001-2023.csv", index=False)
