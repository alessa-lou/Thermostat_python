'use strict';

$(document).ready(function() {
    updateTemperature();
  
    $('#temperature-up').on('click', function() {
        $.post('/temperature', { method: "up"}, function(res){
            // var data = JSON.parse(res);
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
  
    $('#temperature-reser').on('click', function() {
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
            updateTemperature();
          }
        });
      })
  
    function updateTemperature() {
        $.get('/temperature', function(res) {
            if (res.status == 200) {
                var power_saving_mode = res.is_PSM_on ? "on" : "off";
                console.log("helloooooo?!?!?!?!")
                $('#temperature').text(res.temperature);
                $('#temperature').attr('class', res.energy_usage() + '-usage');
                $('#power-saving-status').text(power_saving_mode);
            }
        });
    }  
  
  });