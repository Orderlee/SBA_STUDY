import numpy as np
import matplotlib.pyplot as plt
import os
import json
import pandas as pd

corr_list=[]
mychart='../mychart/'
plt.rc('font',family='applegothic')

def correlation(x,y): # 상관계수를 구해주는 함수
    bar_x = x.mean()
    #print(type(x.mean()))
    bar_y= y.mean()

    bunja = np.sum((x-bar_x)*(y-bar_y))
    #print('분자 : ', bunja)

    left = np.sum((x-bar_x)**2)
    right = np.sum((y-bar_y)**2)
    bunmo = np.sqrt(left*right)
    #print('분모 : ', bunmo)

    return bunja / bunmo


def setScatterGraph(tour_table,visit_table,tourpoint):
    # tour_table : 관광지 입장 정보
    # visit_table : 3개국 관광객 수
    # tourpoint :관광지 이름(예시 : 경복궁)

    tour = tour_table[tour_table['resNm'] == tourpoint]
    merge_table = pd.merge(tour,visit_table,left_index=True,right_index=True)
    #print('^'*30)
    #print(merge_table)

    mylist = [['china','중국인'],['japan','일본인'],['usa','미국인']]
    imsi = []
    imsi.append(tourpoint) #방문지 추가

    fig = plt.figure() # 새로운 도화지를 준비한다.

    print('['+ tourpoint + '] 작업중입니다.')

    for onedata in mylist:
        plt.xlabel(onedata[1] + ' 입국수') # 예시) 중국인 입국수
        plt.ylabel('외국인 입장객수')
        # 해당국가의 컬럼만 추출
        x_data=list(merge_table[onedata[0]])
        y_data=list(merge_table['ForNum'])

        cor = correlation(np.array(x_data),np.array(y_data))
        cor = round(cor, 2) # 자릿

        if cor == 0:
            print('상관계수가 0 입니다.')
            return

        plt.title(tourpoint + '-' + onedata[1]+'상관 관계 분석(' + str(cor) + ')')
        plt.scatter(x_data,y_data, edgecolors='none',alpha=0.75,s=6,c='black')

        # savefig : 해당 이미지를 파일 형식으로 저장하는 함수
        plt.savefig(mychart + tourpoint +'(' + onedata[1] +').png')

        mytuple = (onedata[1],cor) # ('중국인',012)
        imsi.append(mytuple) # 예시) ['창덕궁',('중국인',0.12)]

    corr_list.append(imsi)


# end def setScatterGraph


def main():
    if not os.path.exists(mychart):
        os.mkdir(mychart)
    # .은 현재폴더, ..는 상위 폴더
    filename = '../data/touristResourceStat(서울특별시 2015~2019).json'
    jsonTP=json.loads(open(filename,'rt',encoding='utf-8').read())
    # print(type(jsonTP))
    # print(jsonTP)
    tour_table= pd.DataFrame(jsonTP,columns=('yyyymm','resNm','ForNum'))
    print(type(tour_table))
    print(tour_table.head()) # 전체 데이터중에서 앞 5개만
    #print(tour_table)
    print('-'*30)
    #'yyyymm'컬럼을 색인으로 지정하세요
    tour_table=tour_table.set_index('yyyymm')
    print(tour_table)

    filename = '../data/immigrationTouristStat 미국(275)_(2015~2019).json'
    jsonTP = json.loads(open(filename, 'rt', encoding='utf-8').read())
    usa_tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'visit_cnt'))
    # visit_cnt 칼럼을 국가 이름으로 변경
    usa_tour_table=usa_tour_table.rename(columns={'visit_cnt':'usa'})
    # 'yyyymm' 칼럼을 색인으로 변경
    usa_tour_table=usa_tour_table.set_index('yyyymm')
    print(usa_tour_table)

    filename ='../data/immigrationTouristStat 일본(130)_(2015~2019).json'
    jsonTP= json.loads(open(filename,'rt', encoding='utf-8').read())
    #print(jsonTP)
    japan_tour_table = pd.DataFrame(jsonTP,columns=('yyyymm','visit_cnt'))
    japan_tour_table = japan_tour_table.rename(columns={'visit_cnt':'japan'})
    japan_tour_table = japan_tour_table.set_index('yyyymm')
    print(japan_tour_table)

    filename='../data/immigrationTouristStat 중국(112)_(2015~2019).json'
    jsonTP=json.loads(open(filename,'rt',encoding='utf-8').read())
    #print(jsonTP)
    china_tour_table = pd.DataFrame(jsonTP,columns=('yyyymm','visit_cnt'))
    china_tour_table = china_tour_table.rename(columns={'visit_cnt':'china'})
    china_tour_table = china_tour_table.set_index('yyyymm')
    print(china_tour_table.head())

    #merge : 2개의 데이터 프레임을 합쳐주는 기능
    fv_table=pd.merge(china_tour_table,japan_tour_table,left_index=True, right_index=True)
    fv_table=pd.merge(fv_table,usa_tour_table,left_index=True,right_index=True )
    print(fv_table.head())

    # resNm : 방문지(목록)
    resNm=tour_table.resNm.unique()
    print(resNm)
    for tourpoint in resNm:
        setScatterGraph(tour_table,fv_table,tourpoint)
        #break #차후 삭제 예정

    print('-'*30)
    print(corr_list)


if __name__ == '__main__':
    main()


print('finished')