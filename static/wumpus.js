/*
fetch('http://localhost:5000/wumpus')
  .then(response => response.json())
  .then(data => {
    main(data);

// 1초마다 POST 요청을 보낸다.
    setInterval(function() {
      sendPostRequest(data);
    }, 1000);

  });
*/

function main(data) {

    var agentMap = data.res.agent_map;
    var agentPosition = data.res.now_pos;
    var agentDirection = data.res.direction;
    var agentGold = data.res.hold_gold;
    var agentArrows = data.res.arrows;

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

    for (var i = 4; i >= 1; i--) { // table row
        var row = document.createElement("tr");

        for (var j = 1; j <= 4; j++) { // table cell
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
}


class Observer { // 상태를 갖는 객체

  staticData={};

  constructor() {
    fetch('http://localhost:5000/wumpus')
      .then(response => response.json())
      .then(data => {
        this.staticData = data; // GET response를 staticData에 저장
        console.log(this.staticData);
        main(this.staticData);
      });
  }

  sendPostRequest(action) {
    this.staticData.res.action=action;
    console.log(this.staticData);

    fetch('http://localhost:5000/wumpus', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.staticData)
    })
    .then(response => response.json())
    .then(data => {
      this.staticData = data; // POST response를 저장
      main(this.staticData);
    });
  }

}

const observer = new Observer();
console.log(observer.staticData); // 생성자를 통해 객체를 생성했는데 왜 초기화 되지 않았지?

document.querySelector("#go-forward").addEventListener("click", function() {
  observer.sendPostRequest(0); // 객체에 저장된 상태를 통해 POST 요청 send.
})

document.querySelector("#turn-left").addEventListener("click", function() {
  observer.sendPostRequest(1);
})

document.querySelector("#turn-right").addEventListener("click", function() {
  observer.sendPostRequest(2);
})
