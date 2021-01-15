$(document).ready(function(){
	$(".quest-block").slice(0, 3).show();
	var f = true;
	$("#moreQuests").on('click', function(e){
		if(f){
			e.preventDefault();
			$(".quest-block:hidden").slideDown();
			f = false;
			$("#moreQuests").text("Свернуть")
		}else{
			e.preventDefault();
			$(".quest-block").slice(3).slideUp();
			f = true;
			$("#moreQuests").text("Больше квестов")
		}
	})
})