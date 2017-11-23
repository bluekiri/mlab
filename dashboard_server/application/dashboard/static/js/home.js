function parseTimeLineDatasetFromLogs(logs){
    var dataset_items=  logs.map(function(obj,index){
        return {id: 1, content: logs['data']['model'], start: logs['ts']};
    })

    return new vis.DataSet(dataset_items)
}