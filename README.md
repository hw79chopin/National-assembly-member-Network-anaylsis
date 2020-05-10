2020-1 데이터마이닝 수업 때 했던 프로젝트들을 모아두는 곳입니다.

# 목차
1. 각 파일들 설명
2. 프로젝트 과정 및 결과 설명

# 1. 각 파일들 설명
> crawler.py
- '열려라 국회' 사이트 크롤링 코드
 > Network_Analysis.ipynb
 - 크롤링한 코드로 네트워크 분석을 하기 위해 dataframe으로 바꿔주기. Network 분석 후 insight 도출
 > Data_cleansing_for_user_dic.ipynb
   - mecab user-dic을 추가하기 위해 랜덤으로 50개씩 법안을 보고 사용자사전 구축!
   
# 2. Social Network Analysis

## Q. 국회의원들의 관계는 정량적으로 어떻게 설명할 수 있을까?
- 법안발의 현황데이터를 통해 국회의원들이 어떤 국회의원과 법안을 발의했는지 분석하면 국회의원의 관계를 좀 더 정량적으로 파악할 수 있을 것이라고 생각하였음.
- 이에 법안 발의 현황 데이터를 크롤링하고 Social Network Analysis를 이용해 국회의원들 간의 관계를 분석하고 함

### 1) 데이터 확보
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/%EC%82%AC%EC%9D%B4%ED%8A%B8_%EB%B2%95%EC%95%88%20%ED%81%AC%EB%A1%A4%EB%A7%81.png?raw=true)
- 크롤링은 '열려라 국회'에서 공개한 법안내용을 활용하였음.

### 2) Node, Edge 정의
- Node: 국회의원 295명을 활용함 (크롤링 당시 2020.2월 당시 20대 국회의원이 295명)
- Edge: 함께 발의한 법안이 존재하는 경우에 edge를 생성해주었고, 법안 개수에 따라 Weight를 주었음.

### 3) results
- python으로 법안 데이터를 
#### Degree distribution
- Average Degree가 277.65로 나왔다. Node의 개수가 295인 것을 고려하면 대부분의 의원들이 최소 1번 공동발의한 것을 알 수 있다.

#### Density, Diameter
- Density, Diameter 각각 0.941, 2가 나왔다. Density가 1에 가깝게 나온 것을 보면 대부분의 의원들이 공동발의를 한 번씩은 진행한 것으로 해석가능하다. 또한 대부분 연결되어 있기 때문에 Diameter도 2가 나왔다.

#### Network
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/%EA%B7%B8%EB%9E%98%ED%94%84_%EC%A0%84%EC%B2%B4.png?raw=true)
- 전체적인 network는 위의 그림과 같다.
- 왼쪽에 허윤정 의원이 맨 왼쪽에 있다. 왜 community에 속하지 못하고 따로 떨어졌는지 확인해본 결과 허윤정 의원이 20대 국회에서 발의한 법안이 3건밖에 되지 않아서 다른 Node와 connection이 충분하지 못한 것. 뒤에 한계에서도 설명하겠지만 데이터의 오류였음 (다른 의원들의 평균 발의법안은 899건)
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/Network%20Outliers.png?raw=true)
- 다른 
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/Network%20Community.png?raw=true)
- 아웃라이어를 제거한 network를 보면 다음과 같이 크게 4가지 community가 있다.
- 더불어민주당, 미래통합당, 민생당, 정의당이 community를 구성하고 있다.
- 4개의 community 중에서는 미래통합당이 다른 community와는 멀리 떨어져 있는 모습을 확인할 수 있다.

### 한계
- '열려라 국회' 사이트도 [의안정보시스템](https://likms.assembly.go.kr/bill/main.do)에서 크롤링해오는 것이어서 간혹 크롤링 오류로 깨진 글자들이 발견되기도 하였음. 즉, 모든 법안 데이터를 오롯이 크롤링하기에는 무리가 있었음.
- 실례로 허윤정 의원이 20대 국회에서 발의한 법안은 총 27건인데  '열러라 국회'에는 3건밖에 크롤링되지 않는 등 데이터가 완벽하지 못했음.
- 

## 2-2. Final Term project
- git diff야 이놈좀 잡아봐
