$(document).ready(function(){
	$(window).scroll(function(){
		if(this.scrollY > 20)
			$(".navbar").addClass("sticky")
		else
			$(".navbar").removeClass("sticky")
	});

	$(window).scroll(function(){
		if(this.scrollY > 50)
			$(".telephone").addClass("tel-active")
		else
			$(".telephone").removeClass("tel-active")
	});

	$('.menu-toggler').click(function(){
		$(this).toggleClass("active");
		$(".navbar-menu").toggleClass("active");
	})
});