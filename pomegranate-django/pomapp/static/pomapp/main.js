    // Function to fetch the latest data from the server
    async function fetchLatestData() {
        try {
            const response = await fetch('/poll');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            
            if (data.error) {
                document.getElementById('latest-data').textContent = `Error: ${data.error}`;
            } else {
                document.getElementById('latest-data').textContent = `Latest Data: ${data.latest_data.join(', ')}`;
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            document.getElementById('latest-data').textContent = 'Error fetching data. Check console for details.';
        }
    }

// Poll the server every 5 seconds
setInterval(fetchLatestData, 5000);

// Fetch data immediately when the page loads
fetchLatestData();