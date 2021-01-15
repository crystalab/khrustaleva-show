$(document).ready(function(){
	$(".stock").slice(0, 1).show();
	var f = true;
	$("#moreStocks").on('click', function(e){
		if(f){
			e.preventDefault();
			$(".stock:hidden").slideDown();
			f = false;
		}else{
			e.preventDefault();
			$(".stock").slice(2).slideUp();
			f = true;
		}
	})
})