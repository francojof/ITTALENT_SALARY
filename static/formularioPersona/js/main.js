//VARIABLE FORMULARIO COMPLETO
var form = $("#formulario");

/* const spinnerBox = document.getElementById("spinner-box")
const dataBox    = document.getElementById("data-box")
console.log(spinnerBox)
console.log(dataBox) */
//CODIGO ICONO CARGA FORMULARIO
/* var spinner = $('#loader');
var formData = form.serializeArray();
formData = objectifyForm(formData);
$(function() {
  submitForm.submit(function(e) {
    e.preventDefault();
    spinner.show();
    $.ajax({
      url: 'formulario/',
      data: formData,
      method: 'post',
      dataType: 'JSON'
    }).done(function(resp) {
      spinner.hide();
      alert(resp.status);
    });
  });
}); */

function submitForm() {
    /* $('body').append('<div id="loading">Loading...</div>') */
    
    $("#formulario").submit();
 }

 $(function(){
    $('formulario').on('submit', function(e){
        alert("tranquilo mi rey");
    });
})

function validar(){
    var nombre,email,rentaLiquida;
    /* console.log( $( this ).serialize() ); */
    /* expresion= /\w+@\w+\.+[a-z]/; */
    expresion=/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    expresionNombre= /^[a-zA-ZñÑ-áéíóúÄËÏÖÜÁÉÍÓÚ ]+$/i;
    nombre = document.getElementById("id_nombre").value;
    email  = document.getElementById("id_email").value;
    empresa = document.getElementById("tamano_empresa").value;
    pais = document.getElementById("pais").value;
    edad = document.getElementById("edad").value;
    estudios = document.getElementById("estudios").value;
    genero = document.getElementById("genero").value;
    ingles_hablado = document.getElementById("ingles_hablado").value;
    ingles_escrito = document.getElementById("ingles_escrito").value;
    actividad = document.getElementById("actividad").value;
    contrato = document.getElementById("contrato").value;
    cargo = document.getElementById("cargo").value;
    experiencia = document.getElementById("experiencia").value;
    rentas_brutas = document.getElementById("rentas_brutas").value;
    duracionTrabajo = document.getElementById("duracionTrabajo").value;

}



//VALIDAR NUMERO EN RENTA
function numbersonly(e){
    var unicode=e.charCode? e.charCode : e.keyCode
    if (unicode!=8){ //if the key isn't the backspace key (which we should allow)
        if (unicode<48||unicode>57) //if not a number
            return false //disable key press
    }
}



// JQUERY STEPS
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
