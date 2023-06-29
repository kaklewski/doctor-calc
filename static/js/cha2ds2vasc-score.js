const riskSpan = document.getElementById("risk");
let calculatedRisk = "";
const recommendationParagraf = document.getElementById("recommendation");
let recommendation = "";

const allCheckboxes = [...document.getElementsByClassName("form-check-input")];

function calculateRisk() {
	let calculatedPoints = document.getElementById("score").innerHTML;

	console.log(calculatedPoints);

	if (calculatedPoints <= 0) {
		calculatedRisk = "Low";
		recommendation = "No anticoagulant or antiplatelet therapy needed.";
	} else if (calculatedPoints == 1) {
		calculatedRisk = "Moderate";
		recommendation = "Consider oral anticoagulation (NOAC preferred).";
	} else {
		calculatedRisk = "High";
		recommendation = "Order oral anticoagulation (NOAC preferred)";
	}
	riskSpan.innerHTML = calculatedRisk;
	recommendationParagraf.innerHTML = recommendation;
}

allCheckboxes.forEach(function (checkbox) {
	checkbox.addEventListener("change", calculateRisk);
});
