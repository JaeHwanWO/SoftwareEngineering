# README for ntf_generator

## 1. NFT란?
   - non fungible token으로, fungible이 '대체 가능한'이라는 뜻이라서, NFT는 대체가 불가능한(유일한) 토큰을 말한다. 
   - 일반적인 bitcoin과 달리, 교환할 수 없다. 
   - 기존에 인디 음악가들은 저작권 등록을 하는데 돈이 들어서 자신의 저작권을 주장하기 힘들어지는 순간들이 있었다. NTF는 완전 무료이고, 조작 불가능한 기록이 남기 때문에 굳이 돈을 들여 저작권 등록을 하지 않아도 온전한 기록을 남길 수 있다.

## 2. ERC721 Standard?
   - ERC721에서는 [다음과같은](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/IERC721.sol) 함수들을 필수적으로 구현해야 한다. 

   - function balanceOf(address _owner) external view returns (uint256);
        * address를 인자로 받아서, address가 가지고 있는 token의 갯수를 리턴한다. 

## 3. Diagram
![cryptomusicstructure](https://user-images.githubusercontent.com/80820556/114187056-8b7dae80-9982-11eb-8e56-21e6d21a865d.jpg)

## 4. 개발 환경 정의
  * programming language: Solidity

## 5. 참고 자료
* [Jumping into Solidity](https://anallergytoanalogy.medium.com/jumping-into-solidity-the-erc721-standard-part-1-e25b67fc91f3)
* [ERC-721 토큰 설계 방법론](https://brunch.co.kr/@curg/20)

## USE CASE UC-9

| Related Requirements | REQ2, REQ3 |
|---|:---|
| Initiating Actor                                                 | Any of: music uploader, plagiarist                                                                                                                                                                                       |
| Actor's goal                                                     | 자신의 음원을 System에 등록해 저작권을 보호받을 수 있다.                                                                                                                                                                                      |
| Participating Actors                                             | Chain, Analyzer, other music uploader                                                                                                                                                                                    |
| Preconditions                                                    | music uploader/plagiarist가 System에 로그인한 상태여야한다.                                        System이 사용자에게 접근 가능한 UI를 보여준다.                                                                                                    |
| Postconditions                                                   | Chain에 음원이 등록된다.                                             사용자의 음원의 저작권이 보호됨을 알리는 토큰을 발행, 제공한다.                                                                                                                        |
| Flow of Events for Main Success Scenario                         |                                                                                                                                                                                                                          |
| →                                                                | 1. System에서 음원 등록 버튼을 누른다.                                                                                                                                                                                               |
| ←                                                                | 2. music uploader/plagiarist 에게 음원 등록 UI를 보여준다.            Ex) 음원 이름, 음원 파일, 장르, 음원에 대한 설명, 태그, 가사, 앨범 아트                                                                                                                |
| →                                                                | 3. music uploader/plagiarist이 UI에 세부사항을 적고 System에 음원을 제출한다.                                                                                                                                                             |
|                                                                  | 4. UC-10과정 수행한다.                                                                                                                                                                                                         |
| →                                                                | 5. music uploader이 변조하지 않은 패킷을 포장해서 System에 업로드한다.                                                                                                                                                                       |
| ←                                                                | 6. 50%이상의 other music uploader가 패킷이 위변조가 없다고 판단하여 music uploader 에게 음원을 chain에 등록할 수 있는 권한을 준다                                                                                                                           |
| →                                                                | 7. music uploader가 chain에 음원을 등록한다.                                                                                                                                                                                      |
| ←                                                                | 8. 그 음원에 대한 토큰을 music uploader가 받는다.                                                                                                                                                                                     |
| Flow of Events for Extensions (Alternate Scenarios)              |                                                                                                                                                                                                                          |
| 3a.  music uploader/plagiarist가 음원 이름, 음원 파일, 장르에 대한 설명을 적지 않는다. |                                                                                                                                                                                                                          |
| ←                                                                | 1. UI의 upload 버튼이 비활성화 된다.                                                                                                                                                                                               |
| ←                                                                | 2. System이 (amusic uploader/plagiarist가 적지 않은 세부사항을 기록하여 music uploader/plagiarist에게 알린다.                                                                                                                                |
| 5a. music uploader가 변조한 패킷을 포장해서 System에 업로드한다.                  |                                                                                                                                                                                                                          |
| ←                                                                | 1. 50%미만의 other music uploader가 패킷이 위변조가 없다고 판단하여 music uploader 에게 음원을 chain에 등록할 수 있는 권한을 주지 않는다.                                                                                                                      |
| 6a. 50%미만의 other music uploader가 패킷이 위변조가 없다고 판단한다.              |                                                                                                                                                                                                                          |
| ←                                                                | 1. music uploader 에게 음원을 chain에 등록할 수 있는 권한을 주지 않는다.


## Domain Model for UC-9, 10
 ![domainmodel_9_10](https://user-images.githubusercontent.com/80820556/115983979-886bfa80-a5df-11eb-979b-2da7b252bb82.jpg)

## UC Diagram for NFT Generator
![UseCase_TokenGenerator](https://user-images.githubusercontent.com/80820556/115984035-e3055680-a5df-11eb-86b1-297fc8cb4417.jpg)

## Object Sequence Diagrams for NFT Generator
### draft
![NFTGENERATOR_OSD](https://user-images.githubusercontent.com/80820556/118351086-ccc23900-b594-11eb-9d58-e7fb1edf2cfe.jpg)

### specification
![NFTGENERATOR_OSD_2](https://user-images.githubusercontent.com/80820556/118351089-d186ed00-b594-11eb-888e-c2b3cd5c5ca7.jpg)

![NFTGENERATOR_OSD_3](https://user-images.githubusercontent.com/80820556/118351072-c207a400-b594-11eb-9063-e59b7f724fda.jpg)

### final product
![NFTGENERATOR_OSD_4](https://user-images.githubusercontent.com/80820556/118351095-d6e43780-b594-11eb-8d07-11fa19770ab1.jpg)



## Class Diagram for NFT Generator
![NFTGENERATOR_ClassDiagram](https://user-images.githubusercontent.com/80820556/118351059-aac8b680-b594-11eb-8bfe-87f9efcd7163.jpeg)


