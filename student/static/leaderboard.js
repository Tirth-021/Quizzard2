const socket = new WebSocket('ws://' + window.location.host + '/ws/leaderboard/');
socket.onmessage = function(e) {
const data = JSON.parse(e.data);
const leaderboardTable = document.getElementById('leaderboard');

// data.forEach(function(entry) {
// const row = leaderboardTable.insertRow(-1);
// const userCell = row.insertCell(0);
// const scoreCell = row.insertCell(1);
// const questionCell = row.insertCell(2);
//
//
// userCell.innerText = entry.user;
// scoreCell.innerText = entry.score;
// questionCell.innerText = entry.question;
// });
};