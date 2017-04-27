'use strict';

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

function arcana() {
    /* Загадки для посетителей */
    function arcana_template(arcana_data_element) {
        var user_answer = prompt(arcana_data_element[0]);
        if (user_answer) {
            if (user_answer.toLowerCase() == arcana_data_element[1].toLowerCase()) {
                alert("Поздравляю! Вы угадали. Можете попробовать еще загадку.");
            }
            else {
                alert("Вы не угадали. Можете попробовать еще загадку.");
            }
        }
    }

    /* генерация случайного числа для выбоа номера загадки */
    function getRandomInt(max) {
        return Math.floor(Math.random() * max);
    }

    var arcana_data = []
    /* Добавляю загадку и правильный ответ в список загадок:*/
    arcana_data.push(['С какой птицы нужно ощипать перья, чтобы получились сразу и утро, и день, и вечер, и ночь?','с утки'])
    arcana_data.push(['Под каким деревом сидит волк, когда идет дождь?','под мокрым'])
    arcana_data.push(['На теле – два уха, а головы нет.','кастрюля'])
    arcana_data.push(['Что достанет зубами затылок?','расчёска'])
    arcana_data.push(['Он программы пишет-пишет,\nЗа компьютером сидит,\nВсе эмоции здесь лишни –\nЛишь исходный код твердит.','программист'])
    arcana_data.push(['Что нельзя съесть на завтрак?','обед и ужин'])
    arcana_data.push(['Что поднять земли легко, но трудно кинуть далеко?','пух'])

    /* вызываю случайную загадку: */
    arcana_template(arcana_data[getRandomInt(arcana_data.length)])
}
