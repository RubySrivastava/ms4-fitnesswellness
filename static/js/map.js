function initMap() {
    const myLatLong = {
        lat: 57.655890,
        lng: 12.014910
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