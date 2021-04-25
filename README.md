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
