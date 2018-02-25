var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $searchButton = document.querySelector("#search");

$searchButton.addEventListener("click", handleSearchButtonClick);

var filteredUFOData = dataSet;

// render the filtered dataSet to the tbody
function renderTable() {
    $tbody.innerHTML = "";
    for (var i=0; i<filteredUFOData.length; i++) {
    
        // Get current UFO Data and fields
        var UFOdata = filteredUFOData[i];
        var fields = Object.keys(UFOdata);

        // Create new row in tbody for each data point
        var $row = $tbody.insertRow(i);
        for (var j = 0; j < fields.length; j++) {

            // for every field in data, create new cell and set value to current data point
            var field = fields[j];
            var $cell = $row.insertCell(j);
            $cell.innerText = UFOdata[field];
        }
        
    }
}

function handleSearchButtonClick() {
    // Format search field by trimming value whitespace and changing to lowercase string
    var filterDatetime = $datetimeInput.value;
    
    // set filtered UFO Data to an array of all data that match the datetime filter
    filteredUFOData = dataSet.filter(function(UFOdata) {
        var UFOdatetime = UFOdata.datetime;
    
        // if true, add datetime to filtered UFO Data
        return UFOdatetime === filterDatetime;
    });
renderTable();
}

