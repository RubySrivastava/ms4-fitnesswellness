function initMap() {
    const myLatLong = {
        lat: 57.659012,
        lng: 11.990340
    }; /*Möndal*/
    
    /*Select Location*/
    /*Display Map & Marker on map*/
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: myLatLong,
    });
    new google.maps.Marker({
        position: myLatLong,
        map,
    });
}