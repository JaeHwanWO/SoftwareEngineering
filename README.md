
# Simularity_Analysis
* _해당 모듈에서는 서버에서 전달받은 음원과 서버에 존재하는 음원들간의 유사도를 분석하고 트랙의 장르를 예측해 제공하는 기능을 수행합니다._

## Definition

* 음원 추출
   * 주어진 음원을 멜로디,MR, 가사 총 세가지로 분류하는 것
* 음원 분석
   * 분리된 세 종류의 결과를 가지고 각각의 유사도를 도출해내는 과정

## Function
* _해당 모듈의 기능을 명시하면 다음과 같습니다._
   * 1. 해당 음원과 서버에 존재하는 음원들간의 유사도를 분석한다.
      * BPM 분석
      * Melody 분석
      * 가사 분석
   * 2. 유사도 분석 후, 해당 수치가 절대값을 넘어가는 비교 대상 음원들을 서버로 전달한다.
   * 3. 음악의 장르를 예측/제공한다.

![Simularity_Analyzer](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/module.jpg)

## Analysis
* MFCC
    * 오디오 신호에서 추출 할 수 있는 소리의 고유한 특징을 나타내는 수치인 MFCC(Mel -Frequency Cepstral Coefficient)를 유사도 분석 자료로 활용합니다.
    * 소리가 공명되는 특정 주파수 대역인 Formants를 연결한 곡선을 추출합니다.
* DTW
    * 음원을 20ms 정도 길이로 잘라내어 MFCC를 통한 특징 데이터 추출 후 DTW (Dynamic Time Warping) 기술을 이용합니다. 이때 산출되는 수치를 두 음원 간 유사도를 나타내는 지표로 이용합니다.
 
## USE-CASE

| USE CASE UC-10                                      | Analyze                                              |
|-----------------------------------------------------|------------------------------------------------------|
| Related Requirements                                | REQ2, REQ3                                           |
| Initiating Actor                                    | Any of: Music uploader                               |
| Actor's goal                                        | 음원의 유사도를 비교분석한다.                          |
| Participating Actors                                | Database, ProcessViewer                              |
| Preconditions                                       | Database에 비교할 음원이 존재해야한다. 음원이 분류될 장르가 명시되어 있어야한다.    |
| Postconditions                                      | 음원의 유사도 값이 산출되고, 값에 따른 표절 여부가 판별된다.                  |
| Flow of Events for Main Success Scenario            |                                                      |
| →                                                   | 1. Music uploader가 시스템에 음원을 업로드 한다.                  |
| ←                                                   | 2. 업로드된 음원을 analyze하여 장르별로 분류한다.                     |
| ←                                                   | 3. 해당 장르에 속한 DB와 analyze를 수행한다.                      |
| ←                                                   | 4. 유사도를 산출해 나가면서 프로세스 진행 결과를 ProcessViewer를 통해 제공한다. |
| ←                                                   | 5. 산출된 유사도가 기준치 n보다 낮게 나올 경우 이는 표절이 아님을 판단한다.        |
| Flow of Events for Extensions (Alternate Scenarios) |                                                      |
| 3a. 장르가 혼합되어 특정 장르로 명확히 판단할수 없다.                    |                                                      |
| ←                                                   | 1. Analyzer를 통한 장르분석 결과값이 두번째로 높은 장르를 적용한다.          |
| 5a. 유사도가 기준치 n보다 높다.                                |                                                      |
| ←                                                   | 1. 이는 표절로 판단하여 결과를 전달한다.                             |


## UC Diagram for Simularity Analyzer
![UC for simularityAnalyzer](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/31.PNG)

## Domain Model for UC 9 & 10 
![DMforUC10](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/DMforuc10.png)
### Domain Model for UC 10
![UC10Dmodel-1](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/UC10Dmodel-1.png)

## Simple Summary of Sequence Diagram
| Name                                     | Function                                              |
|-----------------------------------------------------|------------------------------------------------------|
| Controller  |                    provides music source for analyzing and get the result of analysis                      |
| Genre |             analyzes the genre of given source and alert if the genre doesn't match with user input                  |
| BP |            provides the standard value for analyzing. It managed as object to use flexibly               |
| DB |            contains the source of music classified by genre                |
| Seperate  |           Seperate the music into melody, MR, lyrics part                               |
| Melody |            Compare the Melody with two provided music part                   |
| MR |             Compare the MR with two provided music part             |
| Lyrics |             Compare the lyrics with two provided music part               |
| Result |     Combine the result of melody, MR, lyrics with a computed weight. After that, compare the result with given standard n and add the music to the list if the percentage exceeds n |

## Sequence Diagram for Simularity Analyzer

![SeqDiagram1](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/SeqDiagram1.png)

## Variation of Sequence Diagram

![Var1](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/variation1.jpg)
![Var2](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/variation2.jpg)

## Class Diagram for Simularity Analyzer
![ClassDiagram](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/Class%20Diagram.jpg)

## Demo Play
![Structure](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/Structure.jpg)
![DemoRes](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/demores1.png)
![DemoRes2](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/demores2.png)
## Local DB
![DB](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/LocalDB.PNG)
## Analysis Result
![Result](https://github.com/JaeHwanWO/SoftwareEngineering/blob/simularity_analysis/Images/Result.PNG)

## 참고 문헌
<blockquote>
https://scienceon.kisti.re.kr/commons/util/originalView.do?cn=JAKO201034049320557&oCn=JAKO201034049320557&dbt=JAKO&journal=NJOU00291367
   
   https://arxiv.org/pdf/1503.00022.pdf
</blockquote>

