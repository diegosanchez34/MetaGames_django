$("#formulario_contacto").validate({
    rules:{
        nombre:{
            required:true,
   
        },
        email:{
            required:true,
            email:true}
            ,tipo_solicitud:{
                required:true
            },
        mensaje:{
            required:true,
            minlenght:3,
            maxlenght:120
            
        },
        terminos:{
            required:true
        }
    }
    
})




$("#enviar").click(function(){
    if($("#formulario_contacto").valid()==false){
        return;
    }
    let nombre = $("#nombre").val()
    let email =$("#email").val()
    let tipoSolicitud = $("#tipo_solicitud").val()
    let mensaje = $("#mensaje").val()
    let terminos = $("#temrinos").val()

 //construir un json

 //enviar los datos por post $.post
})

$(document).ready(function(){
    var apiKey = "8bcda3f51amsh6f993b154ffcc77p113c88jsn55755df34e74";
    var apiURL = "https://metacriticapi.p.rapidapi.com/games/top";

    $("#enviar").click(function(){
        $.ajax({
            url: apiURL,
            headers: {
                "X-RapidAPI-Key": apiKey,
                "X-RapidAPI-Host": "metacriticapi.p.rapidapi.com",
                "Authorization": "8bcda3f51amsh6f993b154ffcc77p113c88jsn55755df34e74" // Agrega tu contraseña aquí
            },
            method: "GET",
            success: function(data) {
                $.each(data, function (i, item) {
                    $("#tablajuegos").append(
                        "<tr>" +
                        "<th>" + i + "</th>" +
                        "<th>" + item.title + "</th>" +
                        "<th>" + item.metaScore + "</th>" +
                        "</tr>"
                    );
                });
            },
            error: function(xhr, status, error) {
                console.log(error); // Maneja el error de autenticación de la API
            }
        });
    });
});


const card = document.getElementById('game');
const wordOverlay = card.querySelector('.word-overlay');

card.addEventListener('mouseover', () => {
  wordOverlay.style.transform = 'translateX(0)';
  wordOverlay.style.opacity = '1';
});

card.addEventListener('mouseout', () => {
  wordOverlay.style.transform = 'translateX(-100%)';
  wordOverlay.style.opacity = '0';
});

