
# Simularity_Analysis
* _해당 모듈에서는 서버에서 전달받은 음원과 서버에 존재하는 음원들간의 유사도를 분석하고 트랙의 장르를 예측해 제공하는 기능을 수행합니다._

## Definition
* 음원이란?
   * --- 
* 음원 추출
   * --- 
* 음원 분리
   * ---
## Function
* _해당 모듈의 기능을 명시하면 다음과 같습니다._
   * 1. 해당 음원과 서버에 존재하는 음원들간의 유사도를 분석한다.
      * BPM 분석
      * Melody 분석
      * 가사 분석
   * 2. 유사도 분석 후, 해당 수치가 절대값을 넘어가는 비교 대상 음원들을 서버로 전달한다.
   * 3. 음악의 장르를 예측/제공한다.

![Simularity_Analyzer]()

## Analysis
* MFCC
    * 오디오 신호에서 추출 할 수 있는 소리의 고유한 특징을 나타내는 수치인 MFCC(Mel -Frequency Cepstral Coefficient)를 유사도 분석 자료로 활용합니다.
    * 소리가 공명되는 특정 주파수 대역인 Formants를 연결한 곡선을 추출합니다.
* DTW
    * 음원을 20ms 정도 길이로 잘라내어 MFCC를 통한 특징 데이터 추출 후 DTW (Dynamic Time Warping) 기술을 이용합니다. 이때 산출되는 수치를 두 음원 간 유사도를 나타내는 지표로 이용합니다.  
## 참고 문헌
<blockquote>
https://scienceon.kisti.re.kr/commons/util/originalView.do?cn=JAKO201034049320557&oCn=JAKO201034049320557&dbt=JAKO&journal=NJOU00291367
   
   https://arxiv.org/pdf/1503.00022.pdf
</blockquote>

