# -*- coding: utf-8 -*-
# CSVファイルのマージ
import glob
import pandas as pd


def CsvFileMerge():
    # フォルダ内のファイルパスを取得
    All_Files = glob.glob('./csv/*.csv', recursive=True)
    print(All_Files)

    # フォルダ中の全CSVをマージ
    list = []
    for file in All_Files:
        list.append(pd.read_csv(file, index_col=0,
                    encoding='shift-jis', dtype=object))
        print(file)
        df = pd.concat(list, sort=False)

    # CSV出力
    df.to_csv('typhoon-position_2001-2023.csv', encoding='utf-8')
    print(u'処理終了')


CsvFileMerge()
