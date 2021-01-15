function onClick(element) {
  	document.getElementById("bigImage").src = element.src;
  	document.getElementById("blackBlock").classList.add("active");
}

function clickOnDark() {
	document.getElementById("blackBlock").classList.remove("active");
}