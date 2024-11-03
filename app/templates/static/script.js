const form = document.getElementById('visitForm');
const spinner = document.getElementById('spinner');
const spinnerContainer = document.getElementById('spinner-container');
const spinnerText = document.getElementById('spinner-text');

let messageIndex = 0;
let selectedModel = 'OpenAI'; // Default model

// Function to set selected AI model based on radio button
function setSelectedModel() {
    const modelTypeRadio = document.querySelector('input[name="model_type"]:checked');
    selectedModel = modelTypeRadio ? modelTypeRadio.value : 'OpenAI';
    console.log("Selected AI model: " + selectedModel);
}

// Function to rotate messages
function rotateMessages() {
    const spinnerText = document.getElementById('spinner-text');
    
    // Update messages array after setting the selected model
    const messages = [
        `Talking to the ${selectedModel} models...`,
        "Thinking...",
        "Generating content..."
    ];

    messageIndex = (messageIndex + 1) % messages.length;
    spinnerText.innerHTML = messages[messageIndex];
}

// Call this function when form is submitted or spinner is shown
function showSpinner() {
    setSelectedModel();  // Capture the selected model
    rotateMessages();    // Start rotating messages with updated model
    setInterval(rotateMessages, 1000);  // Rotate every 1 seconds
}

// Set an interval to change the message every 2 seconds
let messageInterval;

form.addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    setSelectedModel();
    // Show the spinner and rotating text
    spinnerContainer.style.display = 'flex';
    spinner.style.display = 'block';  // Ensure spinner itself is visible

    // Start rotating the messages
    messageInterval = setInterval(rotateMessages, 1000);

    // Simulate form submission for demo (remove this in production)
    setTimeout(() => {
        form.submit(); // Actually submit the form after the delay

    }, 100);  // Submit the form after a short delay (500ms)
});

// When the page is reloaded after the response is received, hide the spinner container
window.addEventListener('load', onsubmit, function() {
    spinnerContainer.style.display = 'none'; // Hide spinner on page load
    scrollToGeneration();
});

function resetForm() {
    form.reset(); 
}

function resetResponsePanels() {
    // Clear the content of the Visit Note and Generated Output panels
    document.getElementById('visit-note-panel').innerHTML = '<p>No visit note entered yet.</p>';
    document.getElementById('generated-output-panel').innerHTML = '<p>Generated output will appear here after submission.</p>';
}

function scrollToGeneration() {
    document.getElementById("generated-output-panel").scrollIntoView({ 
        behavior: "smooth",
        block: "start"
    })
}

// Add this to the form's onsubmit event
form.onsubmit = function() {
    resetResponsePanels(); // Clear the lower panels when submit is clicked
};


function fillVisitNote() {
    const visitNoteSelect = document.getElementById('visit_note_select');
    const visitNoteTextarea = document.getElementById('visit_note');
    const adherenceResponseTextarea = document.getElementById('adherence_response');
    const selectedNoteId = visitNoteSelect.value;

    // Fetch the visit note and medication adherence responses if available
    if (selectedNoteId) {
        fetch(`/get_visit_note?note_id=${selectedNoteId}`)
            .then(response => response.json())
            .then(data => {
                visitNoteTextarea.value = data.visit_note || '';
                adherenceResponseTextarea.value = data.adherence_response || '';  // Fill the additional textarea
            })
            .catch(error => console.error('Error fetching visit note:', error));
    }
}