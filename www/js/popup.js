  $(document).ready(
	function() {
		$("svg g path").hover(
			function() {
				var txt = $(this).attr("title");
				if(txt!==undefined)
					$(this).closest("svg").before('<div class="popup_mapa" style="position:fixed; background-color:#fff; padding:7px;">'+txt+'</div>');
			},
			function() {
				$(".popup_mapa").remove();
			}
		);

		$("body").mousemove(function(e){
			var x = e.pageX+20;
			var y = e.pageY-$(window).scrollTop()+20;
			$(".popup_mapa").css({'top':y+"px",'left':x+"px"});
		});
	}
);