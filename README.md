
# Simularity_Analysis
* 해당 모듈에서는 전달받은 음원과 서버에 존재하는 음원들간의 장르 및 유사도를 분석하는 기능을 동작합니다.

## Analysis
* MFCC
    * 오디오 신호에서 추출 할 수 있는 소리의 고유한 특징을 나타내는 수치인 MFCC(Mel -Frequency Cepstral Coefficient)를 유사도 분석 자료로 활용합니다.
    * 소리가 공명되는 특정 주파수 대역인 Formants를 연결한 곡선을 추출합니다.
* DTW
    * 음원을 20ms 정도 길이로 잘라내어 MFCC를 통한 특징 데이터 추출 후 DTW (Dynamic Time Warping) 기술을 이용합니다. 이때 산출되는 수치를 두 음원 간 유사도를 나타내는 지표로 이용합니다.  
## 참고 문헌
<blockquote>

</blockquote>

