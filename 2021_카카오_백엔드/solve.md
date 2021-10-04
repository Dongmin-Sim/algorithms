# 2021 Dev-Matching 웹 백엔드 개발자(상반기)



<br>

## [Programming 1] 로또의 최고순위와 최저순위

#### 문제 요구사항

로또 최고순위와 최저순위 [문제 보러가기](https://programmers.co.kr/learn/courses/30/lessons/77484)

* 가려진 번호 `0` 이 포함된 구매 로또번호(`lottos`)와 당첨번호(`win_ums`)가 각각 리스트로 주어졌을 때,
* 가려진 번호를 고려하여 구매 로또번호로 당첨이 가능했던 최고순위와 최저순위를 알아내는 문제 



#### 풀이 

- 주어진 구매 로또번호(`lottos`)의 가려진 번호`0` 을 ` magic_num` 으로 정의
- 최저순위는 구매한 로또번호(`lottos`) 와 당첨번호(`win_nums`)를 비교하여 나온 순위,
- 최고순위는 최저순위에 ` magic_num` 의 수를 더하여 당첨될 수 있는 등수를 각각 리스트로 담아 리턴



#### 코드

[풀이코드 보러가기](https://github.com/Dongmin-Sim/algorithms/blob/main/2021_%EC%B9%B4%EC%B9%B4%EC%98%A4_%EB%B0%B1%EC%97%94%EB%93%9C/top_bottom_of_the_lottery..py)

<br>

---

<br>

## [Programming 2] 행렬 테두리 회전하기

#### 문제 요구사항

행렬 테두리 회전하기 [문제 보러가기](https://programmers.co.kr/learn/courses/30/lessons/77485)

* 행렬의 행(`rows`)과 열(`columns`), 테두리의 좌상단, 우하단좌표들의 모음(`queries`)이 주어질 때,
* `queries` 의 직사각형 테두리 부분안에 있는 숫자들을 시계방향으로 회전시키고, 각 `query` 마다 테두리에서 가장 작은  값을 구하는 문제

![example1.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/8c8cdd84-d0ec-4b9d-bdf7-f100d0098c5e/example1.png)



#### 풀이 

- 행과 열을 입력받아 숫자를 채워 `matrix`라는 2차원 배열을 생성
- `queries` 의 좌상단(`x1, y1`), 우하단(`x2, y2`) 좌표를 받아 회전과 가장 작은 값을 return 하는 `move` 함수 생성
- `queries` 를 모두 돌며 matrix 갱신 및 가장 작은 값을 순서대로 list 형식으로 return



**`move` 함수**

- 좌상단 값을 `temp` 변수에 저장 
  - 위의 첫번째 예시에서 좌상단 14를 temp 변수에 저장
- 좌상단을 기준으로 직사각형의 왼쪽, 하단, 오른쪽, 상단 방향으로 값을 하나씩 땡겨 좌상단 값을 채워감
  - 왼쪽 : 14 ↑ 20, 20 ↑ 26, 26 ↑ 27
  - 하단 : 27 ← 28, 28 ← 22
  - 오른쪽 : 22 ↓ 16, 16 ↓ 10, 10 ↓ 9
  - 상단 : 8 → 9, 14 → 8, 
- 채워가는 과정에서 가장 작은 값을 갱신
- 다 채워진 후 좌상단의 오른쪽 값에 temp 값을 삽입
  - 좌상단 오른쪽 값은 옮겨진 좌상단 값인 14가 한번 더 들어 갔으므로 `temp` 값을 넣어줌



#### 코드

[풀이코드 보러가기](https://github.com/Dongmin-Sim/algorithms/blob/main/2021_%EC%B9%B4%EC%B9%B4%EC%98%A4_%EB%B0%B1%EC%97%94%EB%93%9C/matrix_Rotation.py)

<br>

---

<br>

## [Programming 3] 다단계 칫솔 판매

#### 문제 요구사항

다단계 칫솔 판매 [문제 보러가기](https://programmers.co.kr/learn/courses/30/lessons/77486)

* 판매원의 이름(`enroll`), 판매원의 추천인(`referral`), 판매한 사람(`seller`), 판매한 사람의 판매량(`amount`)이 주어질 때, 
* 판매한 사람은 판매액의 90%를 가지고, 나머지 10%는 추천인에게 넘겨줌. (단, 10% 금액은 원 단위 절사, 1원 미만일 경우 모두 가짐)
* 판매원에게 배분된 이익금을 계산하여 배열로 리턴하는 문제

![그림7.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/970f1df0-4f00-480f-93a3-13c7e30b19cb/%E1%84%80%E1%85%B3%E1%84%85%E1%85%B5%E1%86%B77.png)

#### 풀이 

- 주어진 인자들을 이용하여 `{'판매원':['추천인', 0(이익금)]}` 꼴의 `parent_child` 딕셔너리를 생성
- 이익금을 계산할 `cal_money` 라는 함수 생성
- 이익금을 모두 계산한 뒤, `parent_child` 의 이익금 value만 리스트 형식으로 return



**`cal_money` 함수**

- 재귀함수로 동작, 판매인과 이익금을 인자로 받으며, 만약에 추천인이 `'-'` (최상단 노드) center이거나, 더 이상 배분한 이익금이 없을 때, 종료함.
- 만일 이익금이 1원 미만일 경우 모두 가지고 추천인에게 배분하지 않음
- 그렇지 않다면 이익금의 90%를 판매인의 이익금에 더하고 
- `parent_child` 에서 판매인의 추천인을 찾고, 남은 이익금(10%)를 다시 **`cal_money`** 재귀함수에 넘겨줌.



#### 코드

[풀이코드 보러가기](https://github.com/Dongmin-Sim/algorithms/blob/main/2021_%EC%B9%B4%EC%B9%B4%EC%98%A4_%EB%B0%B1%EC%97%94%EB%93%9C/selling_toothbrush.py)

<br>

---

<br>

## [SQL] 헤비유저가 소유한 장소

#### 문제 요구사항

헤비유저가 소유한 장소 [문제 보러가기](https://programmers.co.kr/learn/courses/30/lessons/77487)

* `ID`, `NAME`, `HOST_ID` 각각 공간의 아이디, 이름, 공간을 소유한 유저의 아이디의 컬럼을 가지고 있는 `PLACES` 테이블이 주어질 때, 공간을 2개 이상 등록한 사람을 '헤비유저' 라고 함. 
* 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회



#### 풀이 

**IN 풀이**

- `HOST_ID` 로 `GROUP BY`하여, `GROUP BY`의 `HAVING` 조건을 개수가 2개 이상으로 서브쿼리를 생성
- `WHERE` 절로 테이블의 `HOST_ID` 가 위의 서브쿼리 결과 중에 존재한다면 조회하고 `ID` 순으로 `ORDER BY`



**EXISTS 풀이**

- `EXISTS` 로 서브쿼리의 결과가 한 건이라도 존재하면 조회.
- `IN` 과 다르게 모든 값들을 확인하지 않음



#### 코드

[풀이코드 보러가기](https://github.com/Dongmin-Sim/algorithms/blob/main/2021_%EC%B9%B4%EC%B9%B4%EC%98%A4_%EB%B0%B1%EC%97%94%EB%93%9C/heavyUser.sql)



#### 참고

[rgnny.log - EXISTS 풀이참고](https://velog.io/@rgunny/SQLProgrammers-%ED%97%A4%EB%B9%84-%EC%9C%A0%EC%A0%80%EA%B0%80-%EC%86%8C%EC%9C%A0%ED%95%9C-%EC%9E%A5%EC%86%8C)