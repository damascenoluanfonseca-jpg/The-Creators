const destinationList = document.getElementById('destination-list');
const loadButton = document.getElementById('load-data');

const sampleDestinations = [
  {
    name: 'Paris',
    country: 'France',
    description: 'Historic neighborhoods, art museums, and classic city walks.'
  },
  {
    name: 'Tokyo',
    country: 'Japan',
    description: 'A dense blend of culture, technology, and food experiences.'
  },
  {
    name: 'Lisbon',
    country: 'Portugal',
    description: 'Coastal city with warm weather, design, and scenic viewpoints.'
  }
];

function renderDestinations(items) {
  if (!destinationList) return;

  destinationList.innerHTML = items
    .map(
      (item) => `
        <article class="card">
          <h3>${item.name}</h3>
          <p><strong>${item.country}</strong></p>
          <p>${item.description}</p>
        </article>
      `
    )
    .join('');
}

if (loadButton) {
  loadButton.addEventListener('click', () => {
    renderDestinations(sampleDestinations);
  });
}

renderDestinations(sampleDestinations);
