// from data.js
var tableData = data;
var tablebody =  d3.select("tbody")

function ufoTable(data){
tablebody.html("") 
data.forEach((datarow)=>{
    var row = tablebody.append("tr")
    Object.values(datarow).forEach((value)=>{
        var cell = row.append("td")
        cell.text(value)
    })   
})
}
ufoTable(tableData)

function filterTable(){
d3.event.preventDefault()
var date = d3.select("#datetime").property("value")
var filterData = tableData
if (date){
    filterData = filterData.filter(row=>row.datetime===date)
}
ufoTable(filterData)
}
d3.selectAll("#filter-btn").on("click", filterTable)