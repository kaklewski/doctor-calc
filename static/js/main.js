// Add current year to the footer

const footerYear = document.querySelector(".footer-year");

function handleCurrentYear() {
	const year = new Date().getFullYear();
	footerYear.innerText = year;
}
handleCurrentYear();

// Scores calculation

const inputs = [...document.getElementsByClassName("form-check-input")];
const checkboxes = [...document.querySelectorAll("input[type=checkbox]")];
const radios = [...document.querySelectorAll("input[type=radio]")];
const score = document.getElementById("score");

function countScore() {

	let points = 0;

	for (let i = 0; i < checkboxes.length; i++) {
		if (checkboxes[i].checked === true) {
			points = points + parseInt(checkboxes[i].value);
		}
	}

	for (let i = 0; i < radios.length; i++) {
		if (radios[i].checked === true) {
			points = points + parseInt(radios[i].value);
		}
	}

	score.innerHTML = points;

}

inputs.forEach(function (item) {
	item.addEventListener("change", countScore);
});
