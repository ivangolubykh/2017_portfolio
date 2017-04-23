function get_weather() {
    $.ajax({
            type: "GET",
            url: get_weather_url,
            data: '',
            dataType: "json",
            success: function(data){
                document.getElementById('weather_img').src = data.weather_image;
                document.getElementById('weather_temperature').innerHTML = data.weather_temperature;
                document.getElementById('weather_text').innerHTML = data.weather_text;
            }
    });
}
