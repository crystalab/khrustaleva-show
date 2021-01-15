$(document).ready(function(){
	$(".hero-block").slice(0, 3).show();
	var f = true;
	$("#moreHeroes").on('click', function(e){
		if(f){
			e.preventDefault();
			$(".hero-block:hidden").slideDown();
			f = false;
			$("#moreHeroes").text("Свернуть")
		}else{
			e.preventDefault();
			$(".hero-block").slice(3).slideUp();
			f = true;
			$("#moreHeroes").text("Больше героев")
		}
	})
})