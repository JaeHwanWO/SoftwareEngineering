# Customer‘s Requirements

1. 저작권
    1. 자신의 고유한 창작물이 저작권이 지켜져 악의적인 표절로부터 보호받고 싶다.
    1. 자신이 등록한 음원의 저작권이 안전하게 보호되어야 한다. (저작자의 저작권이 악의적으로 변경되면 안된다.)

2. 유사도
    1. 자신의 음원을 시스템에 등록을 할 때, 자신의 창작물이 기존에 있는 음원들과 어느정도 유사한지 궁금하다.
    1. 검증을 할 때 전체적인 느낌도 판단해서 지표를 산출 했음 좋겠다. (#참조1)
        1. 다만 이 지표는 음악 전문가와 일반 청취자들을 구별해서 판단하여 전문가에 우선순위를 두어야 한다.
        2. 장르와 클리셰를 염두에 두고 코드의 진행 방식과 같은 요소로 판단해야한다. 
      ex. swing장르 아이유 분홍신 vs nekta here’s us 일반인이 듣기엔 곡이 비슷하나 전문가가 들을때는 다를 수 있다.
    1. 패러디와 구별이 되어야 한다. (#참조2)
    1. 표절로 판단이 되었을 때 어떤 음원과 유사한지 결과가 나왔으면 좋겠다.
    1. 표절 검증이 빠르고 정확해야한다.

3. 조회
    1. 스트리밍과는 별개로, 자신의 창작물을 포함하여 등록된 음원들을 조회할 수 있으면 좋겠다.
    1. 악의적인 표절을 한 음원도 시스템에 등록이 되어 저작권 침해를 한 창작자를 알 수 있어야 한다.


| Identifier | Size | Reequirement |
|---|:---:|:---:|
| REQ-1 | 1 | 아직 가입하지 않은 유저는 음원 제공자(musician) 또는 청취자(listener)로 회원가입할 수 있다. |
| REQ-2 | 5 | 음원제공자로서 자신의 음원의 분석이 어느정도 진행되었는지 알 수 있다. |
| REQ-3 | 10 | 표절자(악의적 음원제공자)는 시스템에 음원을 등록할 수 없을 것이다. 시스템은 유사도를 통해 표절을 판단할 것이다. |
| REQ-4 | 3 | 청취자로서, 무료로 음원을 청취할 수 있다. |
| REQ-5 | 2 | 청취자로서, 음원 게시물에 ‘좋아요’를 누를 수 있고, 댓글을 달 수 있다. |
| REQ-6 | 2 | 청취자로서, 음원이 타 음원과 유사하다고 느끼면 신고할 수 있다. |
| REQ-7 | 3 | 신고를 많이 받은 음원은 커뮤니티의 토론 부분에 등록된다 |
| REQ-8 | 1 | 회원으로서, 토론에 참여할 수 있다. |
| REQ-9 | 4 | 음원제공자로서, 토론에서 더 높은 영향력을 끼친다 |
| REQ-10 | 1 | 유저는 음원을 검색할 수 있다.  |
| REQ-11| 1 | 유저는 음원을 다른 유저에게 공유할 수 있다. |
| REQ-12 | 1 | 유저는 자신만의 플레이리스트를 만들 수 있다. |


## User Interface Requirement
  | Actor | Actor's Goal | Use-Case Name |
|---|:---:|:---:|
| User | 회원가입 | SignIn(UC-1) |
| User | '좋아요' | Like(UC-2)|
| User | 다른 사용자에게 공유 | Share(UC-3) |
| User | 음원 검색 | Search(UC-4) |
| User | 플레이리스트 만들기 | Playlist(UC-5) |
| User | 댓글 달기 | Comment(UC-6) |
| User | 해당 음원이 다른 음원들과 유사하다고 느끼면 신고할 수 있다. | Discuss(UC-7) |
| User | 토론에 참여 | Discuss(UC-7) |
| Listner | 음원을 청취할 수 있다 | Stream(UC-8) |
| musician | 음원을 등록하고, 저작권 승인되었는지 확인 | Publish(UC-9)  |
| musician| 음원제공자로서 자신의 음원 분석이 얼마나 진행되었는지 알 수 있다 | Analyze(UC-10) |
| post | ‘좋아요’ 저장 | Like(UC-2) |
| post | 공유기능 제공 | Share(UC-3) |
| post | 음원검색 기능 제공 | Search(UC-4) |
| post | 플레이리스트 제공 | Playlist(UC-5) |
| post | 댓글 제공 | Comment(UC-6) |
| report board | 신고를 많이 받은 음원은 커뮤니티의 토론 부분에 등록된다. | Discuss(UC-7) |
| analyzer | 음원의 유사도를 비교분석한다. | Analyze(UC-10) |

## Requirement per Use-Case

| Requirement | PW | UC1 | UC1 | UC1 | UC1 | UC1 | UC1 | UC1 | UC1 | UC1 | UC1 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| req1 |1 |O||||||||||
| req2 | 5|||||||||O|O|
| req3 |10 |||||||||O|O|
| req4 |3 ||||||||O|||
| req5 | 2||O|||||||||
| req6 |2 |||||||O||||
| req7 |3 |||||||O||||
| req8 |1 ||||||O|O||||
| req9 |4 ||||||O|O||||
| req10 |1 ||||O|||||||
| req11|1 |||O||||||||
| req12 |1 |||||O||||||
| Max PW |-|1|2|1|1|1|4|4|3|10|10|
| Total PW |-|1|2|1|1|1|5|10|3|15|15|

## 참조1
<blockquote>
“표절”이란 일반적으로 두 저작물간의 실질적으로 표현이 유사한 경우는 물론 전체적인 느낌이 비슷한 경우까지를 의미하며, 그 안에는 타인의 저작물을 자신이 창작작한 것처럼 속였다는 도덕적 비난이 강하게 내포되어 있습니다. 따라서 타인의 저적물의 창작적 표현을 복제하였을 경우에는 표절의 문제가 발생할 수 있습니다(한국저작권위원회, 저작권자동상담시스템).  

음악저작물의 저작권 침해여부를 판단하는 것은 쉬운 일은 아니지만, 일반적으로 가락, 리듬, 화음의 3가지 요소의 실질적 유사성 여부가 일반적인 기준이 됩니다. 특히 가락이 가장 중요한 요소를 차지하게 되는데, 개별적인 음표의 유사성보다는 그 음표가 어떻게 결합되어 연속되었는지가 중요합니다. 이와 같이 음악저작물의 저작권 침해여부를 판단하는 것은 쉬운 일은 아닙니다.  

다만 판례에 따른 법률적 판단기준을 살펴보면  

① 기존 저작물을 이용하였을 것, 즉 창작적 표현을 복제 하였을 것  

② 기존의 저작물에 ‘의거’하여 이를 이용하였을 것  

③ 원저작물과의 사이에 실질적유사성이 있을 것 등입니다.  

https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=705&ccfNo=3&cciNo=1&cnpClsNo=2 참조
</blockquote>

## 참조2
<blockquote>
패러디(Parody)”란 표현의 형식을 불문하고 원작을 이용하여 원작 자체나 사회적 상황에 대하여 풍자적, 해학적 방식으로 비평하거나 웃음을 이끌어 내는 것으로써, 표절이 되지 않습니다. 패러디는 비평적 모방이라고 할 수 있는데, 유명한 원작을 대상으로 하고 누구든지 원작을 떠올릴 수 있는 방법으로 창조적 모방을 한다는 점에서 원작을 몰래 모방하는 표절과 구분하고 있습니다.  


패러디가 표절로 인정되지 않는 이유는 기존 작품의 비평, 풍자를 위한 모방은 자유로운 표현행위로써 헌법상의 표현의 자유로 보호받아야 하며, 또한 새로운 문화의 향상발전이라는 「저작권법」의 목적과도 부합하기 때문입니다.  

「저작권법」 제28조에서 “공표된 저작물은 보도·비평·교육·연구 등을 위하여 정당한 범위 안에서 공정한 관행에 합치되게 이를 인용할 수 있다”고 규정하는 것을 패러디의 근거로 생각할 수 있습니다. 

따라서 우리 「저작권법」상 적법한 패러디가 되기 위해서는  

① 비평 목적이 있어야 하며  

② 정당한 범위 안에서  

③ 공정한 관행에 따라 원작을 이용해야 합니다.  


우리 법원도 “컴백홈” 사건에서 당해 저작물에 대한 비평과 풍자는 패러디로 보호된다고 인정하면서도 원곡의 특징을 흉내 내어 단순히 웃음을 자아내는 정도는 패러디로 볼 수 없다고 판결하였습니다(서울고등법원 2010.10.13. 선고. 2010나35260 판결).  

https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=705&ccfNo=3&cciNo=1&cnpClsNo=2 참조
</blockquote>
