
// Function to count visitors time spend time on post
// Store in seconds in database
let initialSpendTime = 0;

// Check visitorID is not null then perform fetch operation and increment
if (visitorID != null) {

    setInterval(() => {
        // Increase initial spend time on every interval with 5
        initialSpendTime += 5;

        const data = {
            visitorID: visitorID,
            spendTime: initialSpendTime,
        };
        // Send data on every 5 second to store on database of visitor

        // Send post request to server and update visitors time spend duration
        fetch("/api/v1/timeSpendsDuration", {
            method: "POST",
            headers: { 'X-CSRFToken': csrfToken, "Content-Type": "application/json" },
            body: JSON.stringify(data),
            keepalive: true
        });
    }, 5000);
};

