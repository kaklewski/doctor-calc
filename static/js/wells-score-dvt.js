const riskSpan = document.getElementById("risk");
let calculatedRisk = "Low";
const recommendationParagraf = document.getElementById("recommendation");
let recommendation = "";

const allCheckboxes = [...document.getElementsByClassName("form-check-input")];

function calculateRisk() {
	let calculatedPoints = document.getElementById("score").innerHTML;

	console.log(calculatedPoints);

	if (calculatedPoints <= 0) {
		calculatedRisk = "Low";
		recommendation =
			"Determine D-dimer. If negative, rule out DVT. If positive, perform CUS of the proximal veins or the entire venous system.";
	} else if (calculatedPoints <= 2) {
		calculatedRisk = "Moderate";
		recommendation =
			"Determine D-dimer. If negative, rule out DVT. If positive, perform CUS of the proximal veins or the entire venous system.";
	} else {
		calculatedRisk = "High";
		recommendation =
			"Perform CUS of the proximal veins or the entire venous system.";
	}
	riskSpan.innerHTML = calculatedRisk;
	recommendationParagraf.innerHTML = recommendation;
}

allCheckboxes.forEach(function (checkbox) {
	checkbox.addEventListener("change", calculateRisk);
});
