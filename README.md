# `21대 국회의원 발의법안 네트워크 분석`
`network-analysis` `gephi`
- 발의법안을 분석하여 국회의원들간의 관계를 정량적으로 파악하기
- 참가자: 박솔희, 윤형준, 이시은, 정현우

## 요약
```
> python, gephi를 활용해 국회의원 social network analysis를 진행
> 전반적으로 같은 당 사람들끼리 법안발의를 많이 하고 다른 당 사람들끼리 교류가 적었음
> Community 시각화를 통해 임기 내 법안발의에 소홀히 하는 국회의원들이 outlier로 나타나는 것을 확인
> Closeness, Betweenness, Eigenvector centrality 등을 통해서 가장 열심히 일하는 국회의원이 누군지, 국회의원들 중심에서 broker 역할은 누가 하는지 등을 파악할 수 있었음
```
# 1. Social Network Analysis를 활용해 국회의원 관계 분석하기

## Q. 국회의원들의 관계는 정량적으로 어떻게 설명할 수 있을까?
- 법안발의 현황데이터를 통해 국회의원들이 어떤 국회의원과 법안을 발의했는지 분석하면 국회의원의 관계를 좀 더 정량적으로 파악할 수 있을 것이라고 생각하였음.
- 이에 법안 발의 현황 데이터를 크롤링하고 Social Network Analysis를 이용해 국회의원들 간의 관계를 분석하고 함

## 1) 데이터 확보
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/%EC%97%B4%EB%A0%A4%EB%9D%BC%EA%B5%AD%ED%9A%8C%20%EB%A9%94%EC%9D%B8.png?raw=true)
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/%EC%82%AC%EC%9D%B4%ED%8A%B8_%EB%B2%95%EC%95%88%20%ED%81%AC%EB%A1%A4%EB%A7%81.png?raw=true)
- 크롤링은 '열려라 국회'에서 공개한 법안내용을 활용하였음.

## 2) Node, Edge 정의
- Node: 국회의원 295명을 활용함 (크롤링 당시 2020.2월 당시 20대 국회의원이 295명)
- Edge: 함께 발의한 법안이 존재하는 경우에 edge를 생성해주었고, 법안 개수에 따라 Weight를 주었음.

## 3) Results
- python으로 법안 데이터를 network 분석용 dataframe으로 바꾸고 Gephi로 분석하였다.

### 3-1) Degree distribution
- Average Degree가 277.65로 나왔다. 
- Node의 개수가 295인 것을 고려하면 대부분의 의원들이 최소 1번 공동발의한 것을 알 수 있다.

### 3-2) Density, Diameter
- Density, Diameter 각각 0.941, 2가 나왔다. 
- Density가 1에 가깝게 나온 것을 보면 대부분의 의원들이 공동발의를 한 번씩은 진행한 것으로 해석가능하다. 
- 또한 node들이 대부분 연결되어 있기 때문에 diameter값이 2가 나왔다.

### 3-3) Network Outliers
- 전체적인 network는 밑의 그림과 같다.
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/%EA%B7%B8%EB%9E%98%ED%94%84_%EC%A0%84%EC%B2%B4.png?raw=true)

- 왼쪽에 허윤정 의원이 맨 왼쪽에 있다. 왜 community에 속하지 못하고 따로 떨어졌는지 확인해본 결과, 허윤정 의원이 20대 국회에서 발의한 법안이 3건밖에 되지 않았다.
- 다른 Node와 connection이 충분하지 못하였기 때문에 혼자 멀리 떨어져있게 된 것.(의원들 평균 발의법안 899건)
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/Network%20Outliers.png?raw=true)
- community에서 먼 9명의 국회의원들의 평균법안 살펴본 결과 144개였다. 전체 평균의 1/8 수준이어서 커뮤니티에서 멀어진 것으로 확인된다.

### 3-4) Network Communities
![](https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/Network%20Community.png?raw=true)
- 아웃라이어를 제거한 network를 보면 다음과 같이 크게 4가지 community가 있다.
- 더불어민주당, 미래통합당, 민생당, 정의당이 community를 구성하고 있다.
- 4개의 community 중에서는 미래통합당이 다른 community와는 멀리 떨어져 있는 모습을 확인할 수 있다.

<img src="https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/%EC%9D%B4%EC%B0%AC%EC%97%B4%EC%9D%98%EC%9B%90.png?raw=true" alt="alt text" width="500"/>

- 이찬열 의원은 미래통합당임에도 불구하고 더불어민주당, 민생당 community에 위치한다.
- 이찬열 의원은 선거 당시 더불어민주당 소속으로 당선된 뒤, 이후 당적을 2020년에 미래통합당으로 옮겼다. 그렇기에 더불어민주당 community에 가깝다.

<img src="https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/%EA%B7%B8%EB%9E%98%ED%94%84_%EC%9E%90%EC%9C%A0%ED%86%B5%ED%95%A9%EB%8B%B9%20%EC%AA%BD.png?raw=true" alt="alt text" width="500"/>

- 미래통합당 community쪽에는 미래통합당, 무소속, 미래한국당 의원들이 섞여있다.
- 미래한국당이 미래통합당의 위성정당이이기에 같은 community에 속해있는 것을 확인할 수 있다.

> ### Degree Centrality
- Degree Centrality는 직접 연결되어 있는 node의 수를 의미한다.
- 높으면 영향력이 크다고 말할 수 잇다.
- density에서 확인한 바와 같이 degree가 전반적으로 높다.
- 그 중에서 degree가 높은 의원을 살펴보면 김관영(바른미래당 원내대표), 박주선(국회부의장), 주승용(국회부의장), 이동섭(바른미래당 원내대표 권한대행) 등 국회에서 영향력이 큰 의원들이었다.
- 가장 높은 degree를 가지는 이개호, 이찬열 의원은 뒤에서 확인하겠지만 다른 centrality도 높다.

> ### Betweenness Centrality
<img src="https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/betweenness%20centrality%20%EC%8B%9D.png?raw=true" alt="alt text" width="200"/> where, gjk = the number of geodesics connecting jk, gjk(i)= the number that actor i is on
- Betweenness Centrality는 각 노드 사이의 최단거리 중 특정 노드를 지나가는 비율을 의미한다.   
- 즉, broker 역할을 한다고 말할 수 있다.
<img src="https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/betweenness%20centrality.png?raw=true" alt="alt text" width="400"/>  

- Betweenness Centrality가 가장 높은 의원은 이개호(더불어민주당), 이찬열(미래통합당)의원이다.  
- 이 두 의원들이 다른 정당 사람들과도 활발하게 법안을 발의하는 broker의 역할을 하고 있다.

> ### Closeness Centrality
<img src="https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/closeness%20centrality%20%EC%8B%9D.png?raw=true" alt="alt text" width="200"/> where, d(i,j) = the shortest path from i to j
- Closeness Centrality는 특정 node에서 다른 node까지의 최단거리의 역수의 합이다.
- 모든 node까지 가장 빨리 도달할 수 있는 node에 가중치를 두는 방법이다.
- Closeness Centrality가 높은 node는 정보 확산에 중요한 역할을 한다고 볼 수 있다.
- 대부분의 의원들 Closeness Centrality가 높다. 그 중에서 유난히 높은 의원들을 정리하자면 다음과 같다. (당명 가나다순)
  - 더불어민주당: 이개호, 이찬열, 변재일
  - 미래통합당: 김삼화, 이동섭, 이명수
  - 민생당: 조배숙, 주승용, 최경환, 최도자, 황주홍, 김관영, 김경진, 박주선, 김동철
- 위 의원들은 국회에서 법안의 확산에 중요한 역할을 한다고 볼 수 있으며, 특히 민생당 (전 바른미래당) 의원들이 많은 것으로 보아 바른미래당의 중도보수 성격으로 진보와 보수 사이에서 법안 확산의 역할을 많이 맡았다고 생각한다.

> ### Eigenvector centrality
<img src="https://github.com/hw79chopin/National-Assembly-member-recommender/blob/master/data/Eigenvector%20closeness%20%EC%8B%9D.png?raw=true" alt="alt text" width="200"/>  

- Eigenvector centrality는 degree가 높은 이웃들을 많이 가질수록 가중치를 주는 방식이다.  
- Eigenvector centrality가 높으면 중요한 사람들과의 연결관계가 많다고 볼 수 있다.  
- Eigenvector centrality가 높은 의원들을 정리하자면 다음과 같다. (당명 가나다순)  
  - 더불어민주당: 이개호, 이찬열, 변재일  
  - 미래통합당: 김삼화, 이동섭, 이명수  
  - 민생당: 조배숙, 주승용, 최경환, 최도자, 황주홍, 김관영, 김경진, 박주선, 김동철  
- Closeness centrality가 높은 의원들이 Eigenvector centrality도 높게 나왔다.  
- 이는 법안 확산에 기여를 많이 하는 의원들이 국회 법안 발의에서 중요한 사람들과도 많이 연결되어 있다고 해석할 수 있다.  

# 2. 한계
- '열려라 국회' 사이트도 [의안정보시스템](https://likms.assembly.go.kr/bill/main.do)에서 크롤링해오는 것이어서 간혹 크롤링 오류로 깨진 글자들이 발견되기도 하였음. 즉, 모든 법안 데이터를 오롯이 크롤링하기에는 무리가 있었음.
-  허윤정 의원이 20대 국회에서 발의한 법안은 총 27건인데  '열러라 국회'에는 3건밖에 크롤링되지 않는 등 데이터가 완벽하지 못했음.

# 3. 각 파일들 설명
> crawler.py
- '열려라 국회' 사이트 크롤링 코드
