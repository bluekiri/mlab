function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = '' + d.getFullYear(),
        hours = '' + d.getHours(),
        minutes = '' + d.getMinutes(),
        seconds = '' + d.getSeconds();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    if (hours.length < 2) hours = '0' + hours;
    if (minutes.length < 2) minutes= '0' + minutes;
    if (seconds.length < 2) seconds= '0' + seconds;


    return [year, month, day].join('-')+'T'+hours+":"+minutes+":"+seconds+".000Z";
}

function parseTimeLineDatasetFromLogs(logs){
    var dataset_items=  logs.map(function(obj,index){
        return {id: index, content: obj['data']['model_name'], start: formatDate(obj['ts'].$date)};
    })

    return new vis.DataSet(dataset_items)
}