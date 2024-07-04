// Add current year to the footer

const footerYear = document.querySelector('.footer-year');

function handleCurrentYear() {
	const year = new Date().getFullYear();
	footerYear.innerText = year;
}
handleCurrentYear();

// Calculate scores (Centor score, Wells score etc.)

const inputs = [...document.getElementsByClassName('form-check-input')];
const checkboxes = [...document.querySelectorAll('input[type=checkbox]')];
const radios = [...document.querySelectorAll('input[type=radio]')];
const score = document.getElementById('score');

function countScore() {
	let points = 0;
	// Sum all ticked checkboxes by their HTML values
	for (let i = 0; i < checkboxes.length; i++) {
		if (checkboxes[i].checked === true) {
			points = points + parseInt(checkboxes[i].value);
		}
	}
	// Sum all marked radios by their HTML values
	for (let i = 0; i < radios.length; i++) {
		if (radios[i].checked === true) {
			points = points + parseInt(radios[i].value);
		}
	}
	score.innerHTML = points;
}

// Run the function whenever one of the values is changed
inputs.forEach(function (item) {
	item.addEventListener('change', countScore);
});
