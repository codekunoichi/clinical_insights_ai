const form = document.getElementById('visitForm');
const spinner = document.getElementById('spinner');
const spinnerContainer = document.getElementById('spinner-container');
const spinnerText = document.getElementById('spinner-text');

// List of messages to rotate through
const messages = [
    "Talking to the OpenAI models...",
    "Thinking...",
    "Generating content..."
];
let messageIndex = 0;

// Function to rotate messages
function rotateMessages() {
    messageIndex = (messageIndex + 1) % messages.length;
    spinnerText.innerHTML = messages[messageIndex];
}

// Set an interval to change the message every 2 seconds
let messageInterval;

form.addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Show the spinner and rotating text
    spinnerContainer.style.display = 'flex';

    // Start rotating the messages
    messageInterval = setInterval(rotateMessages, 2000);

    // Simulate form submission for demo (remove this in production)
    setTimeout(() => {
        form.submit(); // Actually submit the form after the delay
    }, 500);  // Submit the form after a short delay (500ms)
});

// When the page is reloaded after the response is received, hide the spinner container
window.addEventListener('load', function() {
    spinnerContainer.style.display = 'none'; // Hide spinner on page load
});