const mapKedah = L.map("map", {
    minZoom: 5,
    maxZoom: 18,
    maxBounds: [[1.0, 99.0], [6.5, 104.5]],
    maxBoundsViscosity: 1.0
}).setView([6.12, 100.37], 9)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(mapKedah);

const mapSelangor = L.map("map2", {
    minZoom: 5,
    maxZoom: 18,
    maxBounds: [[1.0, 99.0], [6.5, 104.5]],
    maxBoundsViscosity: 1.0
}).setView([3.07, 101.51], 9)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(mapSelangor);

fetch('/hospitals')
    .then(response => response.json())
    .then(function(hospitals) {
        hospitals.forEach(function(h) {
            L.marker([h.lat, h.lng])
            .addTo(mapKedah)
            L.marker([h.lat, h.lng])
            .addTo(mapSelangor)
            .bindPopup('<b>' + h.name + '</b></br>' + h.type);
        });
    });