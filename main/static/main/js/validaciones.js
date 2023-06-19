$(document).ready(function(){

    $("#formulario_contacto").submit(function(){
        $("#error-nombre").hide();
        $("#error-correo").hide();
        $("#error-solicitud").hide();
        $("#error-mensaje").hide();    

        var nombre = $("#nombre").val();
        var correo = $("#correo").val();
        var solicitud = $("#solicitud").val();
        var mensaje = $("#mensaje").val();
        
        if(nombre == ""){
            $("#error-nombre").html("El campo Nombre es obligatorio.");
            $("#error-nombre").show();
            return false;
        }
        else if(correo == ""){
            $("#error-correo").html("El campo Email es obligatorio.");
            $("#error-correo").show();
            return false;
        }
        else if(!validarCorreo(correo)){
            $("#error-correo").html("Por favor, escribe una dirección de correo válida");
            $("#error-correo").show();
            return false;
        }
        else if(solicitud == ""){
            $("#error-solicitud").html("Selecione un tipo de solicitud.");
            $("#error-solicitud").show();
            return false;
        }
        else if(mensaje == ""){
            $("#error-mensaje").html("El campo Mensaje es obligatorio.");
            $("#error-mensaje").show();
            return false;
        }

        event.preventDefault();
      
        $('#miModal').modal('show');
            
    });

    $("#cerrar").click(function() {
        location.reload();
    });

    $("#close").click(function() {
        location.reload();
    });

    function validarCorreo(correo){
        var ejemploCorreo = /\S+@\S+\.\S+/;
        return ejemploCorreo.test(correo);
    }

});


