async function submitRequest() {
    const inputParam = encodeURIComponent(document.getElementById("inputParam").value);

    try {
        // Make API request
        const response = await fetch(`http://127.0.0.1:8000/api/?name=${inputParam}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse the JSON response
        const data = await response.json();

        // Display the result in a more readable way
        const resultBox = document.getElementById("resultBox");
        resultBox.innerHTML = "<p>Result:</p>";

        // Iterate over the data and create HTML elements
        data.forEach(item => {
            resultBox.innerHTML += `<p>${JSON.stringify(item)}</p>`;
        });

    } catch (error) {
        console.error("Error fetching data:", error.message);
        // Handle the error, e.g., display an error message in the result box
        const resultBox = document.getElementById("resultBox");
        resultBox.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}
