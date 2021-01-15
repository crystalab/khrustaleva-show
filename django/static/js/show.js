$(document).ready(function(){
	$(".show-block").slice(0, 3).show();
	var f = true;
	$("#moreShow").on('click', function(e){
		if(f){
			e.preventDefault();
			$(".show-block:hidden").slideDown();
			f = false;
		}else{
			e.preventDefault();
			$(".show-block").slice(3).slideUp();
			f = true;
		}
	})
})