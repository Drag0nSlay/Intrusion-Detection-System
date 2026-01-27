const API = "http://localhost:5000/alerts";

const map = L.map("map").setView([20, 0], 2);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

const ctx = document.getElementById("severityChart");
const severityChart = new Chart(ctx, {
    type: "doughnut",
    data: {
        labels: ["Low", "Medium", "High"],
        datasets: [{
            data: [0, 0, 0]
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: { color: "#e5e7eb" }
            }
        }
    }
});

const MITRE_MAP = {
    "NMAP Scan Detected": ["T1046", "Discovery"],
    "Brute Force Login": ["T1110", "Credential Access"],
    "ICMP PING detected": ["T1018", "Discovery"],
    "ARP Spoofing": ["T1557", "Man-in-the-Middle"]
};

async function loadAlerts() {
    const res = await fetch(API);
    const alerts = await res.json();

    const tbody = document.getElementById("alerts-table");
    const mitreBody = document.getElementById("mitre-body");

    tbody.innerHTML = "";
    mitreBody.innerHTML = "";

    let low = 0, medium = 0, high = 0;

    alerts.forEach(a => {
        let sevClass = "sev-low";
        if (a.alert.severity >= 3) {
            sevClass = "sev-high";
            high++;
        } else if (a.alert.severity === 2) {
            sevClass = "sev-medium";
            medium++;
        } else {
            low++;
        }

        tbody.innerHTML += `
            <tr>
                <td>${a.timestamp}</td>
                <td>${a.src_ip}</td>
                <td>${a.dest_ip}</td>
                <td>${a.proto}</td>
                <td>${a.alert.signature}</td>
                <td class="${sevClass}">${a.alert.severity}</td>
            </tr>
        `;

        const lat = (Math.random() * 140) - 70;
        const lon = (Math.random() * 360) - 180;
        L.circleMarker([lat, lon], { radius: 5 }).addTo(map);

        if (MITRE_MAP[a.alert.signature]) {
            const [tech, tactic] = MITRE_MAP[a.alert.signature];
            mitreBody.innerHTML += `
                <tr>
                    <td>${a.alert.signature}</td>
                    <td>${tech}</td>
                    <td>${tactic}</td>
                </tr>
            `;
        }
    });

    severityChart.data.datasets[0].data = [low, medium, high];
    severityChart.update();

    document.getElementById("total-alerts").innerText = alerts.length;
    document.getElementById("critical-alerts").innerText = high;
}

loadAlerts();
setInterval(loadAlerts, 5000);
