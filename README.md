# README for community

# Community
_ 유저들이 실제로 여러가지 기능들을 이용할 수 있는 커뮤니티를 구현하는 모듈이다.

# Function
* Personal Information Function ( 개인정보 기능 )
> 주로 개인정보와 관련된 내용을 다룬다.
  1. 회원가입/정보수정/회원탈퇴 
  ** 커뮤니티 서비스 이용을 위한 계정에 관련된 기능들이다.
  
  3. 로그인/로그아웃
  ** 로그인/로그아웃 기능을 제공한다

  5. 아이디/비밀번호찾기
  ** 아이디/비밀번호 찾는 기능을 제공한다.

  6. 등록 게시물 수정/확인/삭제
  ** 자신이 등록한 음원에 대한 기능들을 제공한다.

* Community Configuration Function ( 커뮤니티 구성 기능 )
> 커뮤니티 서비스에 대한 내용을 다룬다
  1. 공지사항 게시판
  ** 운영자들이 중요사항을 공지하는데 사용하는 게시판이다.
  3. 문의 게시판
  ** 유저들과 운영진이 소통할 수 있는 게시판이다.
  5. 자유 게시판
  ** 유저들과 유저들이 소통할 수 있는 게시판이다.
  7. 장르별 게시판
  ** 장르별로 유저들과 유저들이 소통할 수 있는 게시판이다.
* Main Function ( 주요기능 )
> NFT를 활용한 음원등록에 관한 내용이다. [NFT](https://github.com/JaeHwanWO/SoftwareEngineering/tree/ntf_generator)
  1. 음원등록
  ** 핵심 기능으로, Simularity Analysis를 통과한 음원을 블록체인 노드에 패킷포장하여 업로드한다. [Simularity Analysis](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/README.md)
  ** 이 후 과반수의 블록체인노드들(음원등록자들)이 패킷에 대한 무결성 검사를 실시한다.
  ** 이 두 과정들을 통과하면 블록체인노드에 추가된다.
  //패킷검사 및 등록승인(투표)
  //---------------------------------------
  ** 유저가 올린 음악을 등록할 수 있게 한다.
* Secondary Function ( 부차적기능 )
  1. 음악검색
    ** 등록된 음원 중 조건부로 검색하는 기능을 제공한다. ( 가수별 검색, 나라별 검색, 장르별 검색 ... )
  3. 음악평가
    ** 등록된 음원을 평가하고, 피드백을 제공하는 기능이다. ( 추천, 댓글 )
    
* Display Function ( 디스플레이 기능 )
  1. 관심음악
    ** 음악평가에서 추천을 누른 아티스트의 음악들을 표시한다.
  2. 관련음악
    ** 유저의 음악과 유사도가 높은 음악을 표시한다
    //유사도 검사
  5. 탑 리스트
    ** 조회수가 많은 순서대로 나열해준다.
  3. 레코드 리스트
    ** 특정 기록을 달성한 음악을 표시하는 리스트이다 ( 조회수 1등을 장기간 유지한 기록, 플레이시간이 제일 긴 기록 )
  4. 추천 리스트
    ** 특정 기준에 따라 음악들을 추천해주는 리스트이다 ( 추천수가 많은 아티스트의 최신음악, 최근 조회수가 급격히 올라가는 음악 )
    // 알고리즘을 통한 유저들 맞춤 리스트를 제공한다 

# USE CASE
| USE CASE UC-1                                       | SignIn                                                                     |
|-----------------------------------------------------|----------------------------------------------------------------------------|
| Related Requirements                                | REQ1                                                                       |
| Initiating Actor                                    | Any of: musician, listener                                                 |
| Actor's goal                                        | 시스템에 접근할 수 있는 권한 획득                                                        |
| Participating Actors                                | Post                                                                       |
| Preconditions                                       | Database에 사용자의 정보가 있어야한다. System이 사용자에게 접근 가능한 UI를 보여준다.                   |
| Postconditions                                      | Database에 사용자의 정보가 저장된다.                                                   |
| Flow of Events for Main Success Scenario            |                                                                            |
| ←                                                   | 1. System이 user에게 로그인 UI를 띄워준다.                                            |
| →                                                   | 2. user(musician / listener)가 유효한 ID와 PW를 입력한다.                            |
| ←                                                   | 3. 시스템이 (a)정보가 유효함을 인증하고, (b)user(musician/listener)에게 로그인이 성공했음을 알린다.     |
|                                                     |                                                                            |
| Flow of Events for Extensions (Alternate Scenarios) |                                                                            |
| 2a. user(musician / listener)가 유효하지 않은 정보를 입력한다.    |                                                                            |
| ←                                                   | 1. System이 (a)오류를 감지하고 (b)user(musician/listener)에게 회원가입 버튼을 띄워준다.         |
| 2a.1a 유저가 회원가입 버튼을 클릭한다.                            |                                                                            |
| ←                                                   | 1. System이 user에게 회원가입 UI를 띄워준다.                                           |
| →                                                   | 2. user로 부터 유효한 ID와 PW를 입력한다.                                              |
| ←                                                   | 3. 시스템이 (a)정보가 유효함을 인증하고, (b) database에 저장하고, (c) user에게 회원가입이 성공했음을 알린다.  |


| USE CASE UC-2                            | Like                                                                                       |
|------------------------------------------|--------------------------------------------------------------------------------------------|
| Related Requirements                     | REQ5                                                                                       |
| Initiating Actor                         | Any of: User                                                                               |
| Actor's goal                             | 해당 음악에 Like 등록                                                                             |
| Participating Actors                     | Post                                                                                       |
| Preconditions                            | Database에 음원 정보가 있어야 한다.  System이 user에게 좋아요 버튼과 좋아요 개수를 표시하는 UI를 보여준다. 사용자가 좋아요 버튼을 누른다.  |
| Postconditions                           | Database에 좋아요의 정보가 저장된다.                                                                   |
| Flow of Events for Main Success Scenario |                                                                                            |
| ←                                        | 1. 성공 여부에 따라 좋아요 버튼의 색깔과 like count 수를 변경하여 UI에 표시한다.                                      |

| USE CASE UC-3                            | Share                           |
|------------------------------------------|---------------------------------|
| Related Requirements                     | REQ11                           |
| Initiating Actor                         | Any of: user                    |
| Actor's goal                             | 해당 음악을 다른 유저에게 전달한다.            |
| Participating Actors                     | Post                            |
| Preconditions                            | 공유 버튼을 누른다.                     |
| Postconditions                           | 사용자 클립보드에 해당 URL이 복사된다.         |
| Flow of Events for Main Success Scenario |                                 |
| ←                                        | 1. 사용자 클립보드에 해당 게시물의 URL이 복사된다. |

| USE CASE UC-4                                       | Search                                                                    |
|-----------------------------------------------------|---------------------------------------------------------------------------|
| Related Requirements                                | REQ5                                                                      |
| Initiating Actor                                    | Any of: user                                                              |
| Actor's goal                                        | 사용자가 검색한 게시물을 보여준다.                                                       |
| Participating Actors                                | Post                                                                      |
| Preconditions                                       | Database에 음원 이름과 가수 list가 있어야한다. 사용자가 유효한 input을 넣고 search button을 클릭한다.  |
| Postconditions                                      | 이름, 가수와 일치하는 음원 목록을 보여준다.                                                 |
| Flow of Events for Main Success Scenario            |                                                                           |
| →                                                   | 1. System은 해당 text로 목록의 이름과 가수들을 찾아서 매칭된 전체 목록을 보내준다.                     |
| ←                                                   | 2. 사용자는 목록에서 선택하여 해당 게시물로 이동할 수 있다.                                       |
| Flow of Events for Extensions (Alternate Scenarios) |                                                                           |
| 2a. 검색 결과가 없는 경우                                    |                                                                           |
| ←                                                   | 1. data가 없다는 alert를 띄워 준다.                                                |

| USE CASE UC-5                            | Playlist                                           |
|------------------------------------------|----------------------------------------------------|
| Related Requirements                     | REQ12                                              |
| Initiating Actor                         | Any of: user                                       |
| Actor's goal                             | 원하는 음악이 들어간 플레이리스트를 생성한다.                          |
| Participating Actors                     | Post                                               |
| Preconditions                            | 사용자가 음악들을 선택한다. DB에 요청한 음원이 있어야한다. 사용자가 생성버튼을 누른다. |
| Postconditions                           | 플레이 리스트를 생성한다                                      |
| Flow of Events for Main Success Scenario |                                                    |
| ←                                        | 1. 시스템이 해당 음악을 사용자의 플레이리스트에 추가한다.                  |

| USE CASE UC-6                                       | Comment                             |
|-----------------------------------------------------|-------------------------------------|
| Related Requirements                                | REQ8, REQ9                          |
| Initiating Actor                                    | Any of: user, post                  |
| Actor's goal                                        | 사용자가 게시글에 comment를 추가한다.            |
| Participating Actors                                | Post                                |
| Preconditions                                       | 사용자가 댓글을 입력한다. 사용자가 comment버튼을 누른다. |
| Postconditions                                      | 해당 post에 입력된 comment를 추가한다.         |
| Flow of Events for Main Success Scenario            |                                     |
| →                                                   | 1. System이 user가 작성한 comment를 추가한다  |
| Flow of Events for Extensions (Alternate Scenarios) |                                     |

| USE CASE UC-7                            | Discuss                    |
|------------------------------------------|----------------------------|
| Related Requirements                     | REQ8, REQ9                 |
| Initiating Actor                         | Any of: user               |
| Actor's goal                             | 사용자가 토론을 진행할 수 있다.         |
| Participating Actors                     | Post                       |
| Preconditions                            | 사용자가 보낸 신고가 누적된다.          |
| Postconditions                           | 사용자가 Discuss 를 볼 수 있다.     |
| Flow of Events for Main Success Scenario |                            |
| →                                        | 1. System이 새로운 post를 생성한다. |
| ←                                        | 2. Alert를 띄워 사용자들에게 보여준다.  |

| USE CASE UC-12                                      | Report                                 |
|-----------------------------------------------------|----------------------------------------|
| Related Requirements                                | REQ-6, REQ-7, REQ-8                    |
| Initiating Actor                                    | Any of: user                           |
| Actor's goal                                        | 부적절한 게시물을 신고한다                         |
| Participating Actors                                | Post                                   |
| Preconditions                                       | 사용자가 해당 음악을 선택한다. 사용자가 신고버튼을 누른다.      |
| Postconditions                                      | Database에 신고의 정보가 저장된다.                |
| Flow of Events for Main Success Scenario            |                                        |
| →                                                   | System은 해당 음악을 post에 추가시키고 token을 할당한다 |
| Flow of Events for Extensions (Alternate Scenarios) |                                        |
| 1a. 적절하지 않은 신고사유인 경우                                |                                        |
| →                                                   | 해당 음악에 token을 추가하지 않는다                 |

# DOMAIN MODEL
![DM_UC-1](https://user-images.githubusercontent.com/75295665/115984625-1e555480-a5e3-11eb-82a0-1616186f8896.png)
![DM_UC-2](https://user-images.githubusercontent.com/75295665/115984627-231a0880-a5e3-11eb-8f04-9da25617a671.png)
![DM_UC-3](https://user-images.githubusercontent.com/75295665/115984631-244b3580-a5e3-11eb-99b6-f7b5e6fe7a2d.png)
![DM_UC-4](https://user-images.githubusercontent.com/75295665/115984632-2614f900-a5e3-11eb-84aa-f05533ccf00e.png)
![DM_UC-5](https://user-images.githubusercontent.com/75295665/115984633-27462600-a5e3-11eb-8a1f-8a6d989720b9.png)
![DM_UC-6](https://user-images.githubusercontent.com/75295665/115984637-2b724380-a5e3-11eb-96bf-4ae805925176.png)
![DM_UC-7](https://user-images.githubusercontent.com/75295665/115984639-2ca37080-a5e3-11eb-98ba-b1880f45cf0d.png)
![DM_UC-8](https://user-images.githubusercontent.com/75295665/115984641-2dd49d80-a5e3-11eb-89a9-bc2dda1b6216.png)
![DM_UC-11](https://user-images.githubusercontent.com/75295665/115984644-31682480-a5e3-11eb-90d7-3ca5d3b7f8b9.png)
![DM_UC-12](https://user-images.githubusercontent.com/75295665/115984645-32995180-a5e3-11eb-9297-465cee731e9b.png)

# UC Diagram for Community
![제목 없음](https://user-images.githubusercontent.com/75295665/115984648-34631500-a5e3-11eb-9a35-6de2bad0007d.png)

우선 우리 프로젝트의 주된 목표이자 기능인 REPORT와 DISCUSS 클래스에 주목을 하여 작성을 하였다. 
그리고 SIGNIN을 기반으로 작동되어야하기 때문에 SIGNIN까지 총 3개의 USERCASE에 맞춰서 진행하였다.
![20210513_153202](https://user-images.githubusercontent.com/75295665/118364855-36623780-b5d5-11eb-8946-1f4d16982ba0.jpg)
초기 모델이다. 모두 단순한 기능만 작동하도록 하였다. 
SIGNIN같은 경우 입력한 INFO가 USERSTORAGE에 있는 지 확인하고 있으면 setValid를 하여 권한을 주는 기능
REPORT는 해당음악의 MUSICINFO에 접근하여 reportcount를 올리고 reportcount가 1이면 새로운 POST를 만드는 것.
DISCUSS는 discuss를 실행하면 checker가 DB에 접근해 reportcount의 수가 기준과 비교하여 보다 높은 음악들은 Alert를 하는 기능만 구현하였다.
그 이후 회의에서 
1.	USERINFO같은 경우 특정횟수 이상 오입력시 막아버리는 기능
2.	REPORT에서는 새로운 BP(business policy)클래스를 도입하여 reportcount의 기준을 객체화시키는 기능
3.	DISCUSS에서는 위의 REPORT처럼 Alert의 기준을 객체화 시키고 각 상황에 따른 Alert를 구현하는 기능 
의 개선점을 찾았다.


![20210515_215953](https://user-images.githubusercontent.com/75295665/118364884-4d088e80-b5d5-11eb-98f7-e44e0afd8b3e.jpg)
![20210515_220034](https://user-images.githubusercontent.com/75295665/118364885-4da12500-b5d5-11eb-8c01-88b9fa8938f9.jpg)
![a](https://user-images.githubusercontent.com/75295665/118364905-6dd0e400-b5d5-11eb-84b5-963afed5c466.jpg)
1번째 수정모델이다.
1번요구(USERINFO)는 alt와 numofAttempts, denyAttempts를 이용하여 구현하였다.
2번요구, 3번요구는 공통으로 BP 클래스를 생성하여 변수를 넘겨주었고
3번 요구에서는 받아오는 변수에 따라 alt를 사용하였다.
그리고 2번째 회의를 거쳤다.
![report](https://user-images.githubusercontent.com/75295665/118449513-3164cb80-b72e-11eb-8c49-01b081b4cf02.jpg)
![discuss](https://user-images.githubusercontent.com/75295665/118449520-332e8f00-b72e-11eb-8af3-8fc14fd17aa3.jpg)


2번째 수정모델이다
REPORT 와 DISCUSS에 공통적인 부분을 찾기도 하였고 DISCUSS의 PRECONDITION이 REPORT의 발생인 점을 감안하여 두개를 하나로 합치기로 결정하였다. POST를 생성하는 기능은 POST객체에서 하도록 하였고(createPOST), 또한 POST가 계속 생성되는 문제점이 있어 기준을 넘어서는 것에 관해서는 단지 POST내용을 업데이트 하는 것으로 결정하였다. (updatePOST)

![SIGNIN](https://user-images.githubusercontent.com/75295665/118459414-b5bb4c80-b736-11eb-81ea-06eae327d1b8.png)
![REPORT_DISCUSS](https://user-images.githubusercontent.com/75295665/118460064-527dea00-b737-11eb-9370-f39c1e6bd17b.png)


2번의 회의를 거쳐 나온 최종본이다.


![1](https://user-images.githubusercontent.com/75295665/118365300-0a47b600-b5d7-11eb-8e55-88675cd4ebd3.png)
- SIGNIN
![2](https://user-images.githubusercontent.com/75295665/118365304-0b78e300-b5d7-11eb-8598-cf77b5ce1f67.png)
- REPORT & DISCUSS
바탕으로 그린 Class Diagram이다.

* Demo
> main
<img width="959" alt="main" src="https://user-images.githubusercontent.com/75295665/120929380-c9e5de80-c723-11eb-9553-0cd5026f868a.png">

> login 
<img width="956" alt="signin" src="https://user-images.githubusercontent.com/75295665/120929397-db2eeb00-c723-11eb-86ec-088099de87fa.png">


> musicinfo
<img width="960" alt="musicinfo_1" src="https://user-images.githubusercontent.com/75295665/120929409-e4b85300-c723-11eb-96e1-d17fb763d9de.png">

<img width="960" alt="musicinfo_2" src="https://user-images.githubusercontent.com/75295665/120929410-e5e98000-c723-11eb-84ce-d2c74f99ea79.png">

> report
<img width="959" alt="report" src="https://user-images.githubusercontent.com/75295665/120929421-ed108e00-c723-11eb-819e-5b086f4382fd.png">


