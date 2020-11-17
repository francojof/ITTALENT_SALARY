
var form = $("#formulario");


function submitForm() {
  
    
    $("#formulario").submit();
 }

 $(function(){
    $('formulario').on('submit', function(e){
    });
})

function validar(){
    var nombre,email,rentaLiquida;

    expresion=/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    expresionNombre= /^[a-zA-ZñÑ-áéíóúÄËÏÖÜÁÉÍÓÚ ]+$/i;
    nombre = document.getElementById("id_nombre").value;
    email  = document.getElementById("id_email").value;
  

    if (email ==="" && nombre ==="")
    {
        Swal.fire({
            title:"Alerta",
            text:"debes completar todos los campos antes de continuar",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,

        });
        return false;
    }

    else if (nombre ==="")
    {
        Swal.fire({
            title:"Alerta",
            text:"debes ingresar un nombre",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,

        });
        return false;
    }
    else if (nombre.length>50)
    {
        Swal.fire({
            title:"Alerta",
            text:"el nombre ingresado es muy largo",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,

        });
        return false;
    }
    else if (email.length>100)
    {
        Swal.fire({
            title:"Alerta",
            text:"el correo ingresado es muy largo",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,

        });
        return false;
    }
    else if (email ==="")
    {
        Swal.fire({
            title:"Alerta",
            text:"debes ingresar un email",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,

        });
        return false;
    }
    else if (!expresion.test(email) && !expresionNombre.test(nombre) )
    {
        Swal.fire({
            title:"Alerta",
            text:"datos ingresados invalidos",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,
        });
        return false;
    }

    else if (!expresion.test(email))
    {
        Swal.fire({
            title:"Alerta",
            text:"correo invalido",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,
        });
        return false;
    }
    else if (!expresionNombre.test(nombre))
    {
        Swal.fire({
            title:"Alerta",
            text:"su nombre no es valido",
            icon:"warning",
            confirmButtonText:"Aceptar",
            timer: 5000,
            timerProgressBar: true,
            allowOutssideClick: true,
            allowEscapeKey: true,
            allowEnterkey: true,
        });
        return false;

    }
    
}

function numbersonly(e){
    var unicode=e.charCode? e.charCode : e.keyCode
    if (unicode!=8){ 
        if (unicode<48||unicode>57) 
            return false 
    }
}


$(function(){
    
	form.children("#wizard").steps({
        headerTag: "h4",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        
        
        onStepChanging: function (event, currentIndex, newIndex) { 
            if ( newIndex === 1 ) {
                $('.wizard > .steps ul').addClass('step-2');

                
            } else {
                $('.wizard > .steps ul').removeClass('step-2');
            }
            if ( newIndex === 2 ) {
                $('.wizard > .steps ul').addClass('step-3');
                form.find('a[href="#finish"]').remove();
                $('#formulario .actions li:last-child').append('<a href="#finish" role="menuitem" type="submit" id="botonEnviar" onclick="submitForm()"  >Enviar</a> ')
  
            } else {
                $('.wizard > .steps ul').removeClass('step-3');
            }

            return true; 
        
        },
        labels: {
            finish: "Enviar",
            next: "Siguente",
            previous: "Atrás"
        },

        onFinished: function (event, currentIndex)
        {
           form.submit();
        }
        
    });
    
    $('.forward').click(function(){
    	$("#wizard").steps('next');
    });
    $('.backward').click(function(){
        $("#wizard").steps('previous');
    });
    
})












