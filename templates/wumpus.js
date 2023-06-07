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
    main(data.res);
  });
}

fetch('http://localhost:5000/wumpus')
  .then(response => response.json())
  .then(data => {
    main(data.res);
    sendPostRequest(data);

    setInterval(function() {
      sendPostRequest(data);
    }, 1000);
  });


  function main(res) {

    var agentMap = res.agent_map;
    var agentPosition = res.now_pos;
    var agentDirection = res.direction;
    var agentGold = res.hold_gold;
    var agentArrows = res.arrows;

    var tableContainer = document.getElementById("table-container");
    var table = document.getElementById("table");
    var agentImg = document.createElement("img");

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
  }
