# 2023_ai
【배경】

본 프로젝트의 목적은 여러분이 인공지능 교과목에서 배운 지능형 소프트웨어
패러다임에 대한 이해를 바탕으로 지능형 시스템의 간단한 예제인 Wumpus
World를 프로그래밍하는 것입니다.
 여러분이 익숙한 프로그래밍 언어를 선택할 수 있으며, Wumpus World에서
에이전트의 이성적인 행동을 구현해 보십시오. 또한, 팀 프로젝트를 수행함으로써 협력작업 및 각자 맡은 일의 효율적이며 공정한 분배를 추구할 것입니다. 즐거운 프로젝트가 되기를 바랍니다.

【Project Guideline】

1. 팀 구성 (1-4명, 최대 4명) 및 역할 분담
2. Wumpus World 도메인에 대한 분석: Percept, Reasoning, Action
3. 사용하고자 하는 프로그래밍 언어
4. Project 추진 일정
5. 발표일정
 - 5/9(화): 프로젝트 제안서 발표 및 제출:
 - 6/6(화), 6/8(목), 6/13(화): 프로젝트 발표
 - 6/22(목) 17시: 최종보고서 제출
 
【Project 내용】

Wumpus World의 기초적인 형태를 구현해 본다. n 에이전트가 처한 환경
탐험하는 에이전트가 처한 환경은 4×4 격자로 구성되어 있으며, (1,1) 격자는
안전하다(safe)고 가정한다. 4×4 격자 세계(Grid World)의 고정된 위치에 금(gold), wumpus 괴물 및 웅덩이(pitch)가 존재한다. wumpus 괴물 및 웅덩이가 발생할 확률은 각각의 격자에서 독립적이며, 0.10으로 가정한다. 에이전트가 금을 획득하여 [1,1] 격자로 되돌아오면 탐험은 종료된다. 에이전트의 센서를 통한 입력은 다음과 같다:
[Stench, Breeze, Glitter, Bump, Scream]
- Stench: wumpus 괴물의 존재 여부
- Breeze: 웅덩이의 존재 여부
- Glitter: 금(gold)의 존재 여부
- Bump: 벽(wall)의 존재 여부
- Scream: wumpus 괴물이 에이전트가 쏜 화살에 의하여 제거되었는지에 대한 여부

에이전트의 행동은 다음과 같다:
[GoForward, TurnLeft, TurnRight, Grab, Shoot, Climb]
- GoForward: 에이전트가 한 격자를 이동한다. 
- TurnLeft: 현재 격자에서 왼쪽으로 90도 방향 전환한다. 
- TurnRight: 현재 격자에서 오른쪽으로 90도 방향 전환한다. 
- Grab: 금(gold)을 잡는다. 
- Shoot: 현재 에이전트의 방향으로 화살을 쏜다. 
- Climb: 에이전트가 금을 획득하여 [1,1] 격자로 되돌아 오면, 동굴을 빠져나간다.

에이전트의 기본 값

에이전트는 안전한 (1,1) 격자에서 출발한다. 즉, (1,1) 격자에는 wumpus 괴물과 웅덩이가 존재하지 않으며, 금 역시 존재하지 않는다. 에이전트는 처음에
동쪽(East)을 향하고 있으며, 화살을 총 2개 가지고 있다.

입출력 화면

Wumpus World에서 에이전트의 이동과 현재까지 에이전트가 탐험한 결과에
대한 격자 세계를 표현한다. 텍스트 모드 혹은 그래픽 모드로 표현할 수 있다.

프로그래밍 언어

 자유롭게 선택함 (C++, Python, Java, Lisp 등)

프로그래밍 고려사항

 에이전트가 처한 환경으로부터 센서를 통한 입력의 처리, 각각의 에이전트의 구조에 의한 추론 및 에이전트의 이성적인 행동으로 하나의 프로그래밍 주기가 구성될 수 있도록 한다.
 에이전트가 Wumpus 괴물 혹은 웅덩이에 의하여 죽을 경우에는 에이전트가 ***죽기직전까지*** 인식된 상황(state)을 유지하여 반복할 수 있다.
