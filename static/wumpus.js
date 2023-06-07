function sendPostRequest(data) {
  fetch('http://localhost:5000/wumpus', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
    main(data);
  });
}

fetch('http://localhost:5000/wumpus')
  .then(response => response.json())
  .then(data => {
    main(data);

/* 1초마다 POST 요청을 보낸다.
    setInterval(function() {
      sendPostRequest(data);
    }, 1000);
*/

  });


function main(data) {

    var agentMap = data.res.agent_map;
    var agentPosition = data.res.now_pos;
    var agentDirection = data.res.direction;
    var agentGold = data.res.hold_gold;
    var agentArrows = data.res.arrows;

    var tableContainer = document.querySelector(".table-container");
    var table = document.getElementById("table");
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
                if(agentMap[i][j][3]==1) cellImg.src="wall.png";
                else if(agentMap[i][j][6]==1) cellImg.src="pitch.png";
                else if(agentMap[i][j][7]==1) cellImg.src="visited.png";
                div.appendChild(cellImg);
            }

            // stench
            if(agentMap[i][j][0]==1) {
                var stenchImg = document.createElement("img");
                stenchImg.src = "stench.png";
                div.appendChild(stenchImg);
            }

            // breeze
            if(agentMap[i][j][1]==1) {
                var breezeImg = document.createElement("img");
                breezeImg.src = "breeze.png";
                div.appendChild(breezeImg);
            }

            // glitter
            if(agentMap[i][j][2]==1) {
                var glitterImg = document.createElement("img");
                glitterImg.src = "glitter.png";
                div.appendChild(glitterImg);
            }

            // wumpus
            if(agentMap[i][j][5]==1) {
                var wumpusImg = document.createElement("img");
                wumpusImg.src = "wumpus.png";
                div.appendChild(wumpusImg);
            }

            // agent
            if(agentPosition[0]==i && agentPosition[1]==j) {
                if(agentDirection[0]==1) agentImg.src="agente.png";
                else if(agentDirection[1]==1) agentImg.src="agentn.png";
                else if(agentDirection[2]==1) agentImg.src="agents.png";
                else agentImg.src="agentw.png";
                div.appendChild(agentImg);
            }

            cell.appendChild(div);
            row.appendChild(cell);
        }

        table.appendChild(row);
    }
    tableContainer.appendChild(table);

    document.querySelector("#go-forward").addEventListener("click", function() {
      data.res.action = 0;
      console.log(data);
      sendPostRequest(data);
    })
    document.querySelector("#turn-left").addEventListener("click", function() {
      data.res.action = 1;
      sendPostRequest(data);
    })
    document.querySelector("#turn-right").addEventListener("click", function() {
      data.res.action = 2;
      sendPostRequest(data);
    })

}
