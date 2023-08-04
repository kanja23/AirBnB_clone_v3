// static/scripts/100-hbnb.js

// Variable to store the list of checked states and cities
const checkedLocations = {};

// Function to update the h4 tag inside the div Locations with the list of States or Cities checked
function updateLocationsTag() {
  const locationsTag = document.querySelector('div.Locations h4');
  const checkedLocationsNames = Object.values(checkedLocations).join(', ');
  locationsTag.textContent = `Locations: ${checkedLocationsNames}`;
}

// Function to handle changes on each input checkbox tag
function handleCheckboxChange(event) {
  const checkbox = event.target;
  const locationId = checkbox.dataset.id;
  const locationName = checkbox.dataset.name;

  if (checkbox.checked) {
    // If the checkbox is checked, store the State or City ID in the variable
    checkedLocations[locationId] = locationName;
  } else {
    // If the checkbox is unchecked, remove the State or City ID from the variable
    delete checkedLocations[locationId];
  }

  // Update the h4 tag with the list of States or Cities checked
  updateLocationsTag();
}

// Function to handle the button click event
function handleSearchButtonClick() {
  // Get the list of checked amenities
  const amenities = [];
  const checkboxes = document.querySelectorAll('input[type="checkbox"][data-type="amenity"]:checked');
  checkboxes.forEach((checkbox) => {
    amenities.push(checkbox.dataset.id);
  });

  // Make a POST request to places_search with the list of amenities, states, and cities
  const apiUrl = 'http://0.0.0.0:5001/api/v1/places_search';
  fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      amenities: amenities,
      states: Object.keys(checkedLocations).map(id => ({ id: id, name: checkedLocations[id] })),
      cities: [],
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the data received from the API (e.g., display results on the page)
      console.log('Search results:', data);
    })
    .catch((error) => {
      console.error('Error searching places:', error);
    });
}

// Call the handleCheckboxChange function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  // Listen to changes on each input checkbox tag
  const checkboxes = document.querySelectorAll('input[type="checkbox"][data-type="location"]');
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', handleCheckboxChange);
  });

  const searchButton = document.getElementById('search-button');
  searchButton.addEventListener('click', handleSearchButtonClick);

  // You can add other functions and event listeners related to 100-hbnb.html here if needed.
  // For example, handling other interactions, updating the content dynamically, etc.
});
