function addMlabInfo() {
    $.get( "/dashboard/info", function(data) {
    var data = JSON.parse(data);
    var container = $(".tab-container");

    container.append("<strong class=\"setting-header\">Dashboard</strong>");
    container.append("<p class=\"setting-content\">Title: "+data["dashboard_title"]+"</p>")
    container.append("<p class=\"setting-content\">Port: "+data["dashboard_port"]+"</p>")

    container.append("<strong class=\"setting-header\">Zookeeper</strong>");
    container.append("<p class=\"setting-content\">Host: "+data["zookeper"]+"</p>")
    container.append("<p class=\"setting-content\">Directory: "+data["zookeper_directory"]+"</p>")

    container.append("<strong class=\"setting-header\">Mongo</strong>");
    container.append("<p class=\"setting-content\">Uri: "+data["mongo"]+"</p>")
    container.append("<p class=\"setting-content\">Database: "+data["mongo_database"]+"</p>")
    });
}

