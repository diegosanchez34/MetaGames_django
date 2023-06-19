$(document).ready(function(){
    var apiKey = "8bcda3f51amsh6f993b154ffcc77p113c88jsn55755df34e74";
    var apiURL = "https://metacriticapi.p.rapidapi.com/games/top";

    $("#traer").click(function(){
        $.ajax({
            url: apiURL,
            headers:
            {
                "X-RapidAPI-Key": apiKey,
                "X-RapidAPI-Host": "metacriticapi.p.rapidapi.com",
                "Authorization": "8bcda3f51amsh6f993b154ffcc77p113c88jsn55755df34e74" 
            },
            method: "GET",
            success: function(data) {
                $.each(data, function (i, item) {
                    $("#tablajuegos").append(
                        "<tr>" +
                        "<td> " + (i+1) + " </td> " +
                        "<td> <img src = '" + item.thumbnailUrl + "'></td>" +
                        "<td>" + item.title + "</td>" +
                        "<td>" + item.metaScore + "</td>" +
                        "<td>" + item.userScore + "</td>" +
                        "</tr>"
                    );
                });
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        });
    });
});
