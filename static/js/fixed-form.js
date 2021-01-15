function crossClick() {
	document.getElementById("darkForForm").classList.remove("active");
}

function order(){
	document.getElementById("darkForForm").classList.add("active");
}

function orderAndChangeLink(actionLink){
	document.getElementById("darkForForm").classList.add("active");
	document.getElementById("darkForm").action = actionLink;
}