document.getElementById("startBtn").addEventListener("click", function () {

    document.getElementById("result").innerHTML =
    "<h3>Opening Camera...</h3>";

    fetch("/detect")
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = `
            <h2>Detected Emotion: ${data.emotion}</h2>
            <h2>Response: ${data.response}</h2>
        `;
    });
});