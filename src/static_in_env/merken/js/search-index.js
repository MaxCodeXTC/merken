let searchBar = document.getElementById("search-bar");
let searchIcon = document.getElementById("search-icon");
let searchMessage = document.getElementById("search-message");
let clearMessage = document.getElementById("clear-message");
let searchModal = document.getElementById("search-modal");
let results = document.getElementById("results");

searchIcon.addEventListener("click", showModal);
searchModal.addEventListener("click", removeBackground);
searchBar.addEventListener("keyup", filterTopics);

let h2 = document.getElementsByTagName("h2");
let h3 = document.getElementsByTagName("h3");
let indexList = document.getElementById("indexList");
let h2Array = [];

pushArray(h2, h2Array);
createIndex(indexList, h2Array);

let index = document.getElementById("index");
let a = index.querySelectorAll("a");

replaceAddHref(a);
replaceAddId(h2);
replaceAddId(h3);

let topics = [];

pushArray(h2, topics);
pushArray(h3, topics);

for (let item of topics) {
  let link = replace(item);
  results.insertAdjacentHTML(
    "beforeend",
    `<a style="display:none" href="#${link}" class="results_a">\n <p class="results_p">${
      item.innerText
    }</p>\n </a>`
  );
}

let links = results.querySelectorAll("a");

function showModal() {
  searchModal.style.display = "block";
  searchBar.focus();
}

function filterTopics() {
  let search = searchBar.value.toUpperCase();
  if (searchBar.value.length > 0) {
    searchMessage.style.display = "none";
    clearMessage.style.display = "block";
    results.style.display = "block";
  } else {
    clearMessage.style.display = "none";
    searchMessage.style.display = "block";
    results.style.display = "none";
  }
  for (let item of links) {
    if (item.innerText.toUpperCase().indexOf(search) > -1) {
      item.style.display = "block";
    } else {
      item.style.display = "none";
    }
  }
}

function removeBackground(e) {
  if (e.target == searchBar) {
    searchBar.focus();
  } else if (e.target == clearMessage) {
    clearMessage.style.display = "none";
    searchMessage.style.display = "block";
    searchBar.value = "";
    searchBar.focus();
    for (let result of links) {
      result.style.display = "none";
    }
  } else {
    searchModal.style.display = "none";
  }
}

function replace(item) {
  return item.innerText.replace(/\s/g, "-");
}

function pushArray(array, newArray) {
  for (let item of array) {
    newArray.push(item);
  }
}

function replaceAddId(array) {
  for (let item of array) {
    item.id = replace(item);
  }
}

function createIndex(div, title) {
  for (let item in title) {
    let index = `<li><a href="">${title[item].innerText}</a></li>`;
    div.insertAdjacentHTML("beforeend", index);
  }
}

function replaceAddHref(array) {
  for (let item of array) {
    item.href = `#${replace(item)}`;
  }
}

document.onkeyup = function(e) {
  if (e.ctrlKey && e.which == 90) {
    showModal();
  } else if (e.which == 27) {
    searchModal.style.display = "none";
  }
};
