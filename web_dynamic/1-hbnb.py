$(document).ready(function () {
    // Variable to store the selected amenity IDs
    const selectedAmenities = {};

    // Function to update the h4 tag with the list of amenities checked
    function updateAmenitiesHeader() {
        const amenitiesHeader = $('#amenities-header');
        const amenityNames = Object.values(selectedAmenities).join(', ');
        amenitiesHeader.text(amenityNames);
    }

    // Listen for changes on each input checkbox tag
    $('li input[type="checkbox"]').on('change', function() {
        const amenityId = $(this).data('id');
        const amenityName = $(this).data('name');

        // If the checkbox is checked, store the Amenity ID in the variable
        if ($(this).is(':checked')) {
            selectedAmenities[amenityId] = amenityName;
        } else {
            // If the checkbox is unchecked, remove the Amenity ID from the variable
            delete selectedAmenities[amenityId];
        }

        // Update the h4 tag with the list of Amenities checked
        updateAmenitiesHeader();
    });
});
