const riskSpan = document.getElementById("risk");
let calculatedRisk = "";
const recommendationParagraf = document.getElementById("recommendation");
let recommendation = "";

const allCheckboxes = [...document.getElementsByClassName("form-check-input")];

function calculateRisk() {
	let calculatedPoints = document.getElementById("score").innerHTML;

	console.log(calculatedPoints);

	if (calculatedPoints <= 1) {
		calculatedRisk = "Low";
		recommendation =
			"Symptomatic treatment. Bacteriological diagnosis is unnecessary.";
	} else if (calculatedPoints <= 3) {
		calculatedRisk = "Moderate";
		recommendation =
			"Perform a rapid test for the presence of PBHA antigen. If unavailable, order a throat swab culture test. Treatment decision based on outcome.";
	} else {
		calculatedRisk = "High";
		recommendation =
			"a) If symptoms are severe, prescribe an antibiotic.<br>b) If symptoms are mild, do a PBHA rapid test. If unavailable, order a throat swab culture test. Treatment decision based on outcome.";
	}
	riskSpan.innerHTML = calculatedRisk;
	recommendationParagraf.innerHTML = recommendation;
}

allCheckboxes.forEach(function (checkbox) {
	checkbox.addEventListener("change", calculateRisk);
});
