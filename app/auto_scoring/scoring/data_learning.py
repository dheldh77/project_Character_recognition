import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
from subprocess import check_output
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import pickle
import joblib
from sklearn.linear_model import LinearRegression

# 환자들에 대한 정보를 선형 모델로 기계학습 및 인자로 전달된 정보로 임상치매척도 판단
def learning_about_data():
    # train 데이터 읽어옴
    data = pd.read_csv('./scoring/train.csv',encoding='euc-kr')
    # 필요없는 속성 제거
    data.drop(["name", "Unnamed: 0"],axis=1, inplace = True)
    # CDR을 one-hot encoding 해줌
    # data = pd.get_dummies(data, columns=['CDR'], prefix='CDR')

    # y_0 = data['CDR_0.0'].values
    # y_1 = data['CDR_0.5'].values
    # y_2 = data['CDR_1.0'].values
    # y_3 = data['CDR_2.0'].values

    # x_data = data.drop(['CDR_0.0','CDR_0.5','CDR_1.0','CDR_2.0'],axis = 1)
    # y_list = [y_0, y_1, y_2, y_3]

    # 예측값 제거
    y = data['CDR'].values
    x_data = data.drop(['CDR'],axis = 1)

    # 평균값
    avg = {
        "ASF": data['ASF'].mean(),
        "nWBV" : data['nWBV'].mean(),
        "eTIV" : data['eTIV'].mean(),
        "MMSE" : data['MMSE'].mean(),
        "SES" : data['SES'].mean(),
        "MR_delay" : data['MR_delay'].mean(),
    }

    # 머신러닝
    model = LinearRegression()
    model.fit(x_data, y)
    print(x_data)

    # 저장
    joblib.dump(model, 'data_model.pkl')

    return avg


def check_CDR():
    #불러오기
    load_model = joblib.load('data_model.pkl')

    object = {
            "gender" : [1],
            "age" : [103],
            "ASF": [1.026],
            "nWBV" : [0.76],
            "eTIV" : [1711],
            "CDR" : [2],
            "MMSE" : [25],
            "SES" : [1],
            "educ" : [10],
            "hand" : [1],
            "MR_delay" : [540],
        }

    df = pd.DataFrame(object)
    temp = df.drop('CDR', axis = 1)


    prediction = load_model.predict(temp)
    print(prediction)
