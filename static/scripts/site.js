$(document).ready(function() {
    // the state
    let current_street = 0;
    let current_direction = 0;
    let current_vehicle = 0;
    
    // add the event listeners
    const update_graph = function(){
        // call the AJAX method with the given params 
    };


    // adding event listeners
    $('.street-1-button').click(() => {
        current_street = 0;
        update_graph();
    });
    $('.street-2-button').click(() => {
        current_street = 2;
        update_graph();
    });
    $('.street-3-button').click(() => {
        current_street = 1;
        update_graph();
    });

    $('north-button').click(() => {
        current_direction = 2;
        update_graph();
    });
    $('south-button').click(() => {
        current_direction = 0;
        update_graph();
    });
    $('west-button').click(() => {
        current_direction = 1;
        update_graph();
    });
    $('east-button').click(() => {
        current_direction = 3;
        update_graph();
    });

    $('general-traffic-button').click(() => {
        current_vehicle = 0;
        update_graph();
    });
    $('single-unit-trucks-button').click(() => {
        current_vehicle = 1;
        update_graph();
    });
    $('articulated-trucks-button').click(() => {
        current_vehicle = 2;
        update_graph();
    });
    $('buses-button').click(() => {
        current_vehicle = 3;
        update_graph();
    });
    $('work-vans-button').click(() => {
        current_vehicle = 4;
        update_graph();
    });
    $('bicycles-button').click(() => {
        current_vehicle = 5;
        update_graph();
    });
    $('pedestrians-button').click(() => {
        current_vehicle = 6;
        update_graph();
    });

});

