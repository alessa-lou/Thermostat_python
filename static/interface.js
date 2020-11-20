'use strict';

$(document).ready(function() {
    updateTemperature();
  
    $('#temperature-up').on('click', function() {
        $.post('/temperature', { method: "up"}, function(res){
            console.log(res)
            // var data = JSON.parse(res);
            // console.log(data)
            if (res.status == 200) {
                updateTemperature();
            }
        });
    });
  
    $('#temperature-down').on('click', function() {
        $.post('/temperature', { method: "down"}, function(res){
            // var data = JSON.parse(res);
            if (res.status == 200) {
                updateTemperature();
            }
        });
    });
  
    $('#temperature-reset').on('click', function() {
        $.post('/temperature', { method: "reset"}, function(res){
            // var data = JSON.parse(res);
            if (res.status == 200) {
                updateTemperature();
            }
        });
    });
  
    $('#power-saving-on').on('click', function() {
        $.post('/power-saving-mode', { method: 'on' }, function(res) {
          // var data = JSON.parse(res)
          if (res.status === 200) {
            updateTemperature();
          }
        });
      });
    
      $('#power-saving-off').on('click', function() {
        $.post('/power-saving-mode', function(res) {
          // var data = JSON.parse(res)
          if (res.status === 200) {
            console.log("Hello are we in the right bit?")
            updateTemperature();
          }
        });
      })
  
    function updateTemperature() {
        $.get('/temperature', function(res) {
          console.log(res)
          var data = JSON.parse(res)
          console.log(data.temperature)
            if (data.status == 200) {
                var power_saving_mode = data.power_save_mode_on ? "on" : "off";
                console.log(data.status)
                console.log(power_saving_mode)
                $('#temperature').text(data.temperature);
                $('#temperature').attr('class', data.energy_usage + '-usage');
                $('#power-saving-status').text(power_saving_mode);
            }
        });
    }  
  
  });