// projects.js

function loadProject() {
  window.location.href = "/load";
}

function newProject() {
  window.location.href = "/new";
}

const loadBtn = document.querySelector('#load-btn');
loadBtn.addEventListener('click', loadProject);

const newBtn = document.querySelector('#new-btn');
newBtn.addEventListener('click', newProject);