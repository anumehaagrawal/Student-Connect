$(document).ready(function() {
	for (var i = 0; i < parseInt($('.colleges-length').html()); i++) {
		$('#indicatorContainer' + i.toString()).radialIndicator({
			barColor: '#4caf50',
			minValue: 800,
			maxValue: 1600,
			radius: 30,
			barWidth: 3,
			initValue: parseInt($('#college-score-' + i.toString()).html()),
		});
		var interests = $('#college-specialisation-' + i.toString()).html().split(';');
		for (var int = 0; int < interests.length; int++) {
			$('#colSpec' + i.toString()).append('<div class="chip">' + $.trim(interests[int]) + '</div>');
		}
	}
});