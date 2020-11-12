// ??? something useful needs to go in here...
'use strict';

$(document).ready(function() {
    updateTemperature();
  
    $('#temperature-up').click(function() {
        $.post('/temperature', { method: "up"}, function(res){
            var data = JSON.parse(res);
            if (data.status == 200) {
                updateTemperature();
            }
        });
    });
  
    $('#temperature-up').click(function() {
        $.post('/temperature', { method: "down"}, function(res){
            var data = JSON.parse(res);
            if (data.status == 200) {
                updateTemperature();
            }
        });
    });
  
    $('#temperature-up').click(function() {
        $.post('/temperature', { method: "reset"}, function(res){
            var data = JSON.parse(res);
            if (data.status == 200) {
                updateTemperature();
            }
        });
    });
  
    // $('#powersaving-off').click(function() {
    //   thermostat.switchPowerSavingModeOff();
    //   $('#power-saving-status').text('off');
    // });
  
    // $('#powersaving-on').click(function () {
    //   thermostat.switchPowerSavingModeOn();
    //   $('#power-saving-status').text('on');
    //   updateTemperature();
    // });
  
  
  
  
  
    function updateTemperature() {
        $.get('/temperature', function(res) {
            var data = JSON.parse(res)
            if (data.status == 200) {
                var power_saving_mode = data.is_PSM_on ? "True" : "False";
                $('#temperature').text(`Current Temperature: ${thermostat.getCurrentTemperature()} degrees`);
                $('#temperature').attr('class', thermostat.energyUsage());
                $('#power-saving-status').text(power_saving_mode);
            }
        });
    }  
  
  });