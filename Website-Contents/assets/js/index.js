const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://apz34r27q4246kd4rr6ifqvnai0cnhxu.lambda-url.us-east-1.on.aws/");
    let data = await response.json();
    counter.innerHTML = ` Views: ${data}`;
}
updateCounter();