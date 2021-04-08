# README for ntf_generator

## 1. NFT란?
    * non fungible token으로, fungible이 '대체 가능한'이라는 뜻이라서, NFT는 대체가 불가능한(유일한) 토큰을 말한다. 
    * 일반적인 bitcoin과 달리, 교환할 수 없다. 
    * 기존에 인디 음악가들은 저작권 등록을 하는데 돈이 들어서 자신의 저작권을 주장하기 힘들어지는 순간들이 있었다. NTF는 완전 무료이고, 조작 불가능한 기록이 남기 때문에 굳이 돈을 들여 저작권 등록을 하지 않아도 온전한 기록을 남길 수 있다.

## 2. 어떤 합의 알고리즘을 사용할것인가?

## 3. ERC721 Standard?
    * ERC721에서는 [다음과같은](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/IERC721.sol) 함수들을 필수적으로 구현해야 한다. 

      * function balanceOf(address _owner) external view returns (uint256);
        * address를 인자로 받아서, address가 가지고 있는 token의 갯수를 리턴한다. 
        


## 4. 개발 환경 정의
  * programming language: Solidity
  * 


## 5. 참고 자료
* [Jumping into Solidity](https://anallergytoanalogy.medium.com/jumping-into-solidity-the-erc721-standard-part-1-e25b67fc91f3)
* [ERC-721 토큰 설계 방법론](https://brunch.co.kr/@curg/20)