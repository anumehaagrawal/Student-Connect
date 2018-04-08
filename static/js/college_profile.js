$(document).ready(function(){
	$('.slider').slider();
	var ethnicity = $('.ethnic-breakup').html().split(';');
	google.charts.load('current', {'packages':['corechart']});
	google.charts.setOnLoadCallback(drawChart);

	function drawChart() {

		var data = google.visualization.arrayToDataTable([
			['Ethnic group', 'Percentage'],
			['American Indian/Alaskan Native', parseFloat(ethnicity[0].trim()) * 100.0],
			['Asian', parseFloat(ethnicity[1].trim()) * 100.0],
			['Black/African-American', parseFloat(ethnicity[2].trim()) * 100.0],
			['Hispanic/Latino', parseFloat(ethnicity[3].trim()) * 100.0],
			['Multi-race (not Hispanic/Latino)', parseFloat(ethnicity[4].trim()) * 100.0],
			['Native Hawaiian/ Pacific Islander', parseFloat(ethnicity[5].trim()) * 100.0],
			['White', parseFloat(ethnicity[6].trim()) * 100.0],
			['Unknown', parseFloat(ethnicity[7].trim()) * 100.0],
		]);

		var options = {
			title: 'Ethnicity'
		};

		var chart = new google.visualization.PieChart(document.getElementById('piechart'));

		chart.draw(data, options);
	}
});