$(document).ready(function() {
    // the state
    let current_street = 0;
    let current_direction = 0;
    let current_vehicle = 0;
    console.log("hi there!");


    // add the event listeners
    const update_graph = function() {
        console.log("entered update graph");
        // call the AJAX method with the given params
        //$.get(window.location.host + "/update_graph" + "?intersection=" + current_street + "&direction=" + current_direction + "&traffic=" + current_vehicle);
        document.getElementByTagName("iframe")[0].src = "static/views/graph" + current_street + "" + current_direction + "" + current_vehicle + ".html";
        // update the css
    };


    // adding event listeners
    document.getElementByClassName("street-1-button").addEventListener("click", function(){
      current_street = 0;
      console.log("got here");
      update_graph();
    });
    $('.street-1-button').click(() => {
        current_street = 0;
        console.log("entered stb1");
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

});
