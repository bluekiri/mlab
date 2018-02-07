function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
}

function parseTimeLineDatasetFromLogs(logs){
    var dataset_items=  logs.map(function(obj,index){
        return {id: index, content: obj['data']['model_name'], start: formatDate(obj['ts'].$date)};
    })

    return new vis.DataSet(dataset_items)
}