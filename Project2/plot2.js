function buildPlot() {
    Plotly.d3.json(`/gun_sales`, function(error, response) {
        console.log(response)
        var handgun = response.handgun
        var long_gun = response.long_gun
        var other = response.other
        var year = response.year
        var state = response.state

        // var trace1 = {
        //     type: "scatter",
        //     mode: "lines",
        //     x: year,
        //     y: handgun,
        //     line: {
        //         color: "#17BECF"
        //     }
        // };

        // var data1 = [trace1];

        var layout = {
            title: "Gun Sales by State",
            xaxis: {
                autorange: true,
                type: "linear"
            },
            yaxis: {
                autorange: true,
                type: "linear"
            }
        };

        Plotly.newPlot("plot", data1, layout);

    });
}

buildPlot()