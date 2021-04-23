# 소프트웨어 공학: NFT기반 음원 저작권 사이트 'Crypto Music'

## Team Member
| 이름 | 학과 | 학번 |
|---|:---:|:---:|
|김현석|컴퓨터공학과|20163828|
|나원후|컴퓨터공학과|20173709|
|박민기|컴퓨터공학과|20170807|
|정재민|컴퓨터공학과|20153153|
|조민수|컴퓨터공학과|20161851|
|조성규|컴퓨터공학과|20170562|
|조예진|소프트웨어학부|20186570|

## Background
  이 프로젝트의 의의는, 음악가들의 공유한 창작물의 저작권을 보호함에 있다. 블록체인 중 NFT의 위변조가 불가능한 특성을 살려서, originality를 보장할 수 있다. 사용자는 표절에 대해서 걱정하지 않고 자신의 저작물을 보호받을 수 있다. 또한, 유사도 검출 서버에 의해서 새로운 저작물이 다른 창작자의 창작물을 표절한것인지 알 수있고, 서버의 기준에 의해서 등록될지 여부를 결정한다. 

## SubGroups
    * 나원후, 정재민, 조예진 - NFT token generation
    * 김현석, 조민수 - Community
    * 조성규, 박민기 - Simularity Anaylysis
  https://github.com/JaeHwanWO/SoftwareEngineering/tree/ntf_generator
  https://github.com/JaeHwanWO/SoftwareEngineering/tree/community
  https://github.com/JaeHwanWO/SoftwareEngineering/tree/simularity_analysis
  
  
## Brief System Requirements
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



## Convention
    * README.md 작성 방식은 GITHUB의 [standard_readme](https://github.com/RichardLitt/standard-readme/blob/master/spec.md#specification) 방식을 사용한다.
    * MarkDown은 [이문서](https://heropy.blog/2017/09/30/markdown/) 를 참조한다. 

    * 우리 프로젝트는 7개의 브랜치로 나누어져 있다. 
      * main: 이 README를 작성하기 위한 브랜치이다. 다른용도로는 사용하지 않는다. 
      * meeting_log: 전체 zoom/대면 미팅 시 작성하는 회의록을 보관하는 브랜치이다. 

      * problem_statement: purpose, scope, objective, succesive criteria 정의
      * RAD(requirement_analysis_document): 요구명세서 브랜치이다. 
      * system_model
        * Use case model
        * domain model
        * user interface mockups

      * ntf_generator: work product by 나원후, 정재민, 조예진
      * community: work product by 김현석, 조민수
      * simularity_analysis: 조성규, 박민기
