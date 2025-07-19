// static/js/script.js

document.addEventListener('DOMContentLoaded', () => {

    // Get all necessary elements from the DOM
    const imageUpload = document.getElementById('imageUpload');
    const imagePreviewContainer = document.getElementById('image-preview-container');
    const imagePreview = document.getElementById('image-preview');
    const btnPreview = document.getElementById('btn-preview');
    const btnPredict = document.getElementById('btn-predict');
    const resultContainer = document.getElementById('result-container');
    const resultText = document.getElementById('result-text');
    const loadingSpinner = document.getElementById('loading-spinner');

    // --- Event Listener for Image Preview ---
    if (btnPreview) {
        btnPreview.addEventListener('click', () => {
            const files = imageUpload.files;
            if (files.length > 0) {
                const file = files[0];
                const reader = new FileReader();

                reader.onload = function(e) {
                    imagePreview.setAttribute('src', e.target.result);
                    imagePreviewContainer.style.display = 'block';
                }
                reader.readAsDataURL(file);
            } else {
                alert('Please select an image file first.');
            }
        });
    }

    // --- Event Listener for Prediction ---
    if (btnPredict) {
        btnPredict.addEventListener('click', async () => {
            const files = imageUpload.files;
            if (files.length === 0) {
                alert('Please select an image file to predict.');
                return;
            }

            // Prepare for prediction
            resultContainer.style.display = 'block';
            loadingSpinner.style.display = 'inline-block';
            resultText.style.display = 'none';
            resultText.classList.remove('error'); // Clear previous errors

            // Create FormData object to send file to backend
            const formData = new FormData();
            formData.append('file', files[0]);

            try {
                // Fetch API to call our backend endpoint
                const response = await fetch('/api/predict', {
                    method: 'POST',
                    body: formData,
                });

                const data = await response.json();

                // Hide spinner and display result
                loadingSpinner.style.display = 'none';
                resultText.style.display = 'block';

                if (response.ok) {
                    // Success! Display prediction and confidence
                    resultText.innerHTML = `
                        Predicted Rice Type: <span class="prediction">${data.prediction}</span>
                        <span class="confidence">Confidence: ${data.confidence}</span>
                    `;
                } else {
                    // Error from backend
                    resultText.classList.add('error');
                    resultText.innerText = `Error: ${data.error || 'An unknown error occurred.'}`;
                }

            } catch (error) {
                // Network or other fetch-related error
                console.error('Fetch Error:', error);
                loadingSpinner.style.display = 'none';
                resultText.style.display = 'block';
                resultText.classList.add('error');
                resultText.innerText = 'An error occurred while communicating with the server.';
            }
        });
    }
});