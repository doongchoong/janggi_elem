# janggi_elem

HTML에서 장기판 엘리먼트를 구현하는 프로젝트입니다. 

[https://doongchoong.github.io/janggi_elem/](https://doongchoong.github.io/janggi_elem/)


## 1. 기본 사용법

`janggi-board` 태그를 생성한뒤에  `janggi_board.js` 스크립트를 로드하면 
장기판이 생성됩니다. 

```html
<janggi-board></janggi-board>
<script src="js/janggi_board.js"></script>
```




## 2. 기능

### 2.1. Multi-Boards 

장기판 태그를 여러 개를 만들 수 있습니다.

```html
<janggi-board></janggi-board>
<janggi-board width="540px"></janggi-board>
<script src="js/janggi_board.js"></script>
```

### 2.2. Position

빈 장기판에서 기물들을 시작 위치시킬수 있습니다. 

1. "start" : 초 좌귀마, 한 우귀마  기본값으로 기물들이 위치합니다. 
2. "[left-knight][right-knight]" : [한][초] 시작 포지션입니다. 
    1) left-knight : 좌귀마
    2) right-knight : 우귀마
    3) doubled-knight : 양귀마
    4) coupled-knight : 원앙마
3. FEN : 체스의 FEN 표기법을 사용할 수 있습니다. 

```html
<janggi-board position="start"></janggi-board>
<janggi-board position="[doubled-knight][coupled-knight]"></janggi-board>
<janggi-board position="3aka3/9/4cc3/1ppppp3/r8/9/1PPPPP3/4CC3/9/3AKA3 w - - 0 1"></janggi-board>
<script src="js/janggi_board.js"></script>
```

### 2.3. Orientation

기본적으로 초의 방향에서 장기판이 보이지만 
한의 방향으로 변경할 수 있습니다. 

```html
<janggi-board position="start" orientation="han"></janggi-board>
<script src="js/janggi_board.js"></script>
```

### 2.4. Draggable 

기물을 드래그-드롭 할 수 있는 모드입니다. 
`draggable-piece` 어트리뷰트를 설정하면 됩니다.

```html
<janggi-board position="start" draggable-piece ></janggi-board>
<script src="js/janggi_board.js"></script>
```

### 2.5. Ilegalmove 

기물이 무규칙으로 마음대로 이동할 수 있는 모드입니다.
드래그드롭 모드일때 작동됩니다. 

```html
<janggi-board position="start" draggable-piece ilegalmove ></janggi-board>
<script src="js/janggi_board.js"></script>
```
