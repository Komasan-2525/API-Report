async function submitRequest() {
    const inputParam = encodeURIComponent(document.getElementById("inputParam").value);

    try {
        
        const response = await fetch(`http://127.0.0.1:8000/api/?name=${inputParam}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        
        const data = await response.json();

        
        const resultBox = document.getElementById("resultBox");
        resultBox.innerHTML = "<p>Result:</p>";

       
        data.forEach(item => {
            resultBox.innerHTML += `<p>${JSON.stringify(item)}</p>`;
        });

    } catch (error) {
        console.error("Error fetching data:", error.message);
        
        const resultBox = document.getElementById("resultBox");
        resultBox.innerHTML = `<p>Error: ${error.message}</p>`;
    }
}
