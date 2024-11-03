async function analyzeText() {
    const text = document.getElementById('inputText').value;
    const response = await fetch('/analyze/text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text }),
    });
    const data = await response.json();
    document.getElementById('resultText').innerText = 'Predicted Emotion: ' + data.emotion;
}

async function analyzeImage() {
    const fileInput = document.getElementById('imageInput');
    if (fileInput.files.length === 0) {
        alert("Please select an image file.");
        return;
    }
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    const response = await fetch('/analyze/image', {
        method: 'POST',
        body: formData,
    });
    const data = await response.json();
    document.getElementById('resultImage').innerText = 'Predicted Emotion: ' + data.emotion;
}
