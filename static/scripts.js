document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the form submission
    document.getElementById('data-collection-form').addEventListener('submit', async function (event) {
        event.preventDefault();

        // Get input values
        const instructionInput = document.getElementById('instruction-input').value;
        const inputInput = document.getElementById('input-input').value;
        const outputInput = document.getElementById('output-input').value;

        // Create a new FormData object and append input values to it
        const formData = new FormData();
        formData.append('instruction', instructionInput);
        formData.append('input', inputInput);
        formData.append('output', outputInput);

        // Send a POST request to submit the data
        const response = await fetch('/submit-data', {
            method: 'POST',
            body: formData
        });

        // Check if the response is successful
        if (response.ok) {
            const jsonResponse = await response.json();
            alert(jsonResponse.message);
        } else {
            alert('Error submitting data.');
        }

        // Clear the input fields
        document.getElementById('instruction-input').value = '';
        document.getElementById('input-input').value = '';
        document.getElementById('output-input').value = '';
    });

    // Initialize the page
    init();
});

function init() {
    // Function to resize the textarea dynamically
    function textAreaResize(e) {
        var obj = e.target;
        obj.style.height = "1px";
        obj.style.height = (12 + obj.scrollHeight) + "px";
    }
    
    // Add event listeners to the textareas for resizing
    document.querySelectorAll('textarea').forEach(i => i.addEventListener('keydown', textAreaResize));
    document.querySelectorAll('textarea').forEach(i => i.addEventListener('keyup', textAreaResize));
}

// Functions to open different pages
function openIntroduction() {
    window.location.href = "/introduction";
}

function openInitialTask() {
    window.location.href = "/initial-task";
}

function openClosedQA() {
    window.location.href = "/init-closed-qa";
}

function openOpenQA() {
    window.location.href = "/init-open-qa";
}

function openExtract() {
    window.location.href = "/init-extract";
}

function openCompletion() {
    window.location.href = "/init-completion";
}

function openSummarization() {
    window.location.href = "/init-summarization";
}

function openTranslation() {
    window.location.href = "/init-translation";
}

function openRewrite() {
    window.location.href = "/init-rewrite";
}

function openClassification() {
    window.location.href = "/init-classification";
}

function openSentimentAnalysis() {
    window.location.href = "/init-sentiment-analysis";
}

function openGeneration() {
    window.location.href = "/init-generation";
}

function openBrainstorming() {
    window.location.href = "/init-brainstorming";
}

function openFurtherTasks() {
    window.location.href = "/init-further-tasks";
}

function openMakePrompt() {
    window.location.href = "/make-prompt";
}

function openMakeCompletion() {
    window.location.href = "/make-completion";
}

function openDashboard() {
    window.location.href = "/dashboard";
}

