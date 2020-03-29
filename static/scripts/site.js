$(function() {
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
        let str = "static/views/graph" + current_street + "" + current_direction + "" + current_vehicle + ".html";
        console.log(str);
        document.getElementsByTagName("iframe")[0].src = str;
        // update the css
    };


    // adding event listeners
    $('.street-1-button').click(() => {
        current_street = 0;
        update_graph();
        document.getElementsByClassName("street-1-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("street-1-button")[0].style.color = "#272659";
        document.getElementsByClassName("street-2-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("street-2-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("street-3-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("street-3-button")[0].style.color = "#5d739a";
    });
    $('.street-2-button').click(() => {
        current_street = 2;
        update_graph();
        document.getElementsByClassName("street-2-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("street-2-button")[0].style.color = "#272659";
        document.getElementsByClassName("street-1-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("street-1-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("street-3-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("street-3-button")[0].style.color = "#5d739a";
    });
    $('.street-3-button').click(() => {
        current_street = 1;
        update_graph();
        document.getElementsByClassName("street-3-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("street-3-button")[0].style.color = "#272659";
        document.getElementsByClassName("street-2-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("street-2-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("street-1-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("street-1-button")[0].style.color = "#5d739a";
    });

    $('.north-button').click(() => {
        current_direction = 2;
        update_graph();
        document.getElementsByClassName("north-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("north-button")[0].style.color = "#272659";
        document.getElementsByClassName("south-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("south-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("east-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("east-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("west-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("west-button")[0].style.color = "#5d739a";
    });
    $('.south-button').click(() => {
        current_direction = 0;
        update_graph();
        document.getElementsByClassName("south-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("south-button")[0].style.color = "#272659";
        document.getElementsByClassName("north-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("north-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("east-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("east-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("west-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("west-button")[0].style.color = "#5d739a";
    });
    $('.west-button').click(() => {
        current_direction = 1;
        update_graph();
        document.getElementsByClassName("west-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("west-button")[0].style.color = "#272659";
        document.getElementsByClassName("south-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("south-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("east-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("east-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("north-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("north-button")[0].style.color = "#5d739a";
    });
    $('.east-button').click(() => {
        current_direction = 3;
        update_graph();
        document.getElementsByClassName("east-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("east-button")[0].style.color = "#272659";
        document.getElementsByClassName("south-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("south-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("north-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("north-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("west-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("west-button")[0].style.color = "#5d739a";
    });

    $('.general-traffic-button').click(() => {
        current_vehicle = 0;
        update_graph();
        document.getElementsByClassName("general-traffic-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("general-traffic-button")[0].style.color = "#272659";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("articulated-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("articulated-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("buses-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("buses-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("work-vans-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("work-vans-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("bicycles-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("bicycles-button")[0].style.color = "#5d739a";
    });
    $('.single-unit-trucks-button').click(() => {
        current_vehicle = 1;
        update_graph();
        document.getElementsByClassName("single-unit-trucks-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.color = "#272659";
        document.getElementsByClassName("general-traffic-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("general-traffic-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("articulated-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("articulated-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("buses-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("buses-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("work-vans-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("work-vans-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("bicycles-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("bicycles-button")[0].style.color = "#5d739a";
    });
    $('.articulated-trucks-button').click(() => {
        current_vehicle = 2;
        update_graph();
        document.getElementsByClassName("articulated-trucks-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("articulated-trucks-button")[0].style.color = "#272659";
        document.getElementsByClassName("general-traffic-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("general-traffic-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("buses-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("buses-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("work-vans-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("work-vans-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("bicycles-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("bicycles-button")[0].style.color = "#5d739a";
    });
    $('.buses-button').click(() => {
        current_vehicle = 3;
        update_graph();
        document.getElementsByClassName("buses-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("buses-button")[0].style.color = "#272659";
        document.getElementsByClassName("general-traffic-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("general-traffic-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("articulated-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("articulated-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("work-vans-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("work-vans-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("bicycles-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("bicycles-button")[0].style.color = "#5d739a";
    });
    $('.work-vans-button').click(() => {
        current_vehicle = 4;
        update_graph();
        document.getElementsByClassName("work-vans-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("work-vans-button")[0].style.color = "#272659";
        document.getElementsByClassName("general-traffic-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("general-traffic-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("articulated-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("articulated-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("buses-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("buses-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("bicycles-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("bicycles-button")[0].style.color = "#5d739a";
    });
    $('.bicycles-button').click(() => {
        current_vehicle = 5;
        update_graph();
        document.getElementsByClassName("bicycles-button")[0].style.backgroundColor = "#5d739a";
        document.getElementsByClassName("bicycles-button")[0].style.color = "#272659";
        document.getElementsByClassName("general-traffic-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("general-traffic-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("articulated-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("articulated-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("single-unit-trucks-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("work-vans-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("work-vans-button")[0].style.color = "#5d739a";
        document.getElementsByClassName("buses-button")[0].style.backgroundColor = "transparent";
        document.getElementsByClassName("buses-button")[0].style.color = "#5d739a";
    });

});
