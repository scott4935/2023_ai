function main(data) {

    var agentMap = data.res.agent_map;
    var agentPosition = data.res.now_pos;
    var agentDirection = data.res.direction;
    var agentGold = data.res.hold_gold;
    var agentArrows = data.res.arrows;
    var actList = data.res.act_list;

    // 기존 테이블을 삭제한다.
    var tableContainer = document.querySelector(".table-container");
    while(tableContainer.hasChildNodes()) {
      tableContainer.removeChild(tableContainer.firstChild);
    }

    var table = document.createElement("table");
    var agentImg = document.createElement("img");

    var gold = document.querySelector("#hold_gold");
    var arrows = document.querySelector("#hold_arrows");

    gold.textContent = agentGold;
    arrows.textContent = agentArrows;

    // 승리조건
    if(agentGold===1 && agentPosition[0]===1 && agentPosition[1]===1) {
      isEnd=1;
    }

    // 테이블 생성
    for (var i = 5; i >= 0; i--) { // table row
        var row = document.createElement("tr");

        for (var j = 0; j <= 5; j++) { // table cell
            var cell = document.createElement("td");
            var div = document.createElement("div");

            // 맵의 뒷배경(wall pitch visited)
            if(agentMap[i][j][3]!=0 || agentMap[i][j][6]!=0 || agentMap[i][j][7]!=0){
                var cellImg = document.createElement("img");
                if(agentMap[i][j][3]==1) cellImg.src="img/wall.png";
                else if(agentMap[i][j][6]==1) cellImg.src="img/pitch.png";
                else if(agentMap[i][j][7]==1) cellImg.src="img/visited.png";
                div.appendChild(cellImg);
            }

            // stench
            if(agentMap[i][j][0]==1) {
                var stenchImg = document.createElement("img");
                stenchImg.src="img/stench.png";
                div.appendChild(stenchImg);
            }

            // breeze
            if(agentMap[i][j][1]==1) {
                var breezeImg = document.createElement("img");
                breezeImg.src="img/breeze.png";
                div.appendChild(breezeImg);
            }

            // glitter
            if(agentMap[i][j][2]==1) {
                var glitterImg = document.createElement("img");
                glitterImg.src="img/glitter.png";
                div.appendChild(glitterImg);
            }

            // wumpus
            if(agentMap[i][j][5]==1) {
                var wumpusImg = document.createElement("img");
                wumpusImg.src="img/wumpus.png";
                div.appendChild(wumpusImg);
            }

            // agent
            if(agentPosition[0]==j && agentPosition[1]==i){
                if(agentDirection[0]==1) agentImg.src="img/agente.png";
                else if(agentDirection[1]==1) agentImg.src="img/agentn.png";
                else if(agentDirection[2]==1) agentImg.src="img/agentw.png";
                else agentImg.src="img/agents.png";
                div.appendChild(agentImg);
            }

            cell.appendChild(div);
            row.appendChild(cell);
        }

        table.appendChild(row);
    }
    tableContainer.appendChild(table);

    // act-list
    var actContainer = document.querySelector(".act-container");
    while(actContainer.hasChildNodes()) {
      actContainer.removeChild(actContainer.firstChild);
    }

    var acts = document.createElement("ul");
    for(var i=0; i<actList.length; i++) {
      var listItem = document.createElement('li');
      listItem.textContent = actList[i];
      acts.appendChild(listItem);
    }
    actContainer.appendChild(acts);
}

// start & reset
document.querySelector("#reset").addEventListener("click", function() {
  isEnd = 0;
  observer.sendGetRequest();
})
document.querySelector("#start").addEventListener("click", function() {
  intervalId = setInterval(checkAndSendPost, 500); // 1초마다 POST request
})


class Observer { // 상태를 갖는 객체

  staticData={};

  constructor() {
    fetch('http://110.9.188.36:5000/wumpus')
      .then(response => response.json())
      .then(data => {
        this.staticData = data; // GET response를 staticData에 저장
        console.log(this.staticData);
        main(this.staticData);
      });
  }

  sendPostRequest() {
    fetch('http://110.9.188.36:5000/wumpus', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.staticData)
    })
    .then(response => response.json())
    .then(data => {
      this.staticData = data; // POST response를 저장
      main(this.staticData);
      console.log(this.staticData); // response 확인 용도
    });
  }

  sendGetRequest() {
    fetch('http://localhost:5000/wumpus')
      .then(response => response.json())
      .then(data => {
        this.staticData = data; // GET response를 staticData에 저장
        console.log(this.staticData);
        main(this.staticData);
      });
  }
}

const observer = new Observer();
var isEnd=0;
var intervalId;

function checkAndSendPost() { // 승리조건 만족 시 종료
  if(isEnd === 1) {
    clearInterval(intervalId);
    alert("YOU WIN!");
  }
  else observer.sendPostRequest();
}
