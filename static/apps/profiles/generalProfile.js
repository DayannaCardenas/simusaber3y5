// --------------Incio Pasos Recuperar Contraseña----------------------------------------------
let userpk;
let userUid;
let tokenReset;

$(".js-form_Reset").submit(function(event){
    event.preventDefault();
    $(this).find("button[name=submitReset]").prop("disabled", true);
    $(this).find("button[name=submitReset]").children('span').removeClass('d-none');
    data = {
        "email" : $(this).find("input[name=emailReset]").val(),
    }
    infoToSend = {
        url:URLAPIS+'/profiles/apiSendCodeSMS',
        method:"POST",
        data:data,
        cache: false,
        element: $(this).find("button[name=submitReset]")
    };
    apisSendToApi(infoToSend, saveDataResetEmail, apisFailed);
});

function saveDataResetEmail(response, kwargs){
    $("[name='Paso2']").addClass("active").siblings().removeClass("active");
    kwargs.element.prop('disabled', false);
    kwargs.element.children('span').addClass('d-none');
    userpk= response.usuario;
}

$(".js-form_Verify").submit(function(event){
    event.preventDefault();
    $(this).find("button[name=submitVerify]").prop("disabled", true);
    $(this).find("button[name=submitVerify]").children('span').removeClass('d-none');
    data = {
        "user" : userpk,
        "code": $(this).find("input[name=codeVerify]").val()
    }
    infoToSend = {
        url:URLAPIS+'/profiles/apiValidateCodeSMS',
        method:"POST",
        data:data,
        cache: false,
        element: $(this).find("button[name=submitVerify]")
    };
    apisSendToApi(infoToSend, saveDataResetCode, apisFailed);
});

function saveDataResetCode(response, kwargs){
    $("[name='Paso3']").addClass("active").siblings().removeClass("active");
    kwargs.element.prop('disabled', false);
    kwargs.element.children('span').addClass('d-none');
    userUid = response.uid;
    tokenReset = response.token;
    // alertboostrap('alert-success', response.Mensaje, "alert-boostrap", "alert-generalmodal");
}

$(".js-form_Confirm").submit(function(event){
    event.preventDefault();
    $(this).find("button[name=submitConfirm]").prop("disabled", true);
    $(this).find("button[name=submitConfirm]").children('span').removeClass('d-none');
    data = {
        "uid": userUid,
        "token": tokenReset,
        "new_password1": $(this).find("input[name=new_password1Confirm]").val(),
        "new_password2": $(this).find("input[name=new_password2Confirm]").val()
    }
    infoToSend = {
        url:URLAPIS+'/rest-auth/password/reset/confirm/',
        method:"POST",
        data:data,
        cache: false,
        redirectURL:'/profiles/login/',
        element: $(this).find("button[name=submitConfirm]")
    };
    apisSendToApi(infoToSend, generalRedirectPage, apisFailed);
});

$(".js-btnPassOne").on("click", function(){
    $("[name='Paso1']").addClass("active").siblings().removeClass("active");
    $("[aria-controls='Paso1']").click();
});

$('#reset_password_modal').on('hidden.bs.modal', function () {
    location.reload();
});

$('.js-eye-show').on('click', function(){
    let types='password';
    if($(this).hasClass('fa-eye-slash')){
      types= 'text';
    }
    $(this).toggleClass("fa-eye-slash").toggleClass("fa-eye");
  
    $(this).parents('.input-group').children('input').prop('type', types);
});
// --------------Fin Pasos Recuperar Contraseña----------------------------------------------

//-----------Inicio Seleccionar office dependiendo de ciudad departamento y pais-------------


$('.js-country').on('change',function(){
    $('.js-departament').html("").removeAttr('disabled');
    $('.js-city').html("").attr('disabled',true);
    apiGetDepartament($(this).val());
});


function apiGetDepartament(id){
    infoToSend = {
        url:`${URLAPIS}/locations/apiDepartament?country=${id}`,
        cache: false,
    };
    apisSendToApi(infoToSend,infoDepartament,apisFailed);
}

function infoDepartament(response){
    if(response[0]){
        $('.js-departament').html("").removeAttr('disabled').append('<option value="0" selected> - - - Select Departament - - - -</option>');
        response.forEach(element => {
            const option = document.createElement('OPTION');
            option.text = element.name;
            option.value = element.id;
            $('.js-departament').append(option);
        });
    }else{
        $('.js-departament').html("").attr('disabled',true);
        $('.js-city').html("").attr('disabled',true);
    }
}

$('.js-departament').on('change',function(){
    $('.js-city').removeAttr('disabled');
    apisGetCity($(this).val());
});

function apisGetCity(id){
    infoToSend = {
        url:`${URLAPIS}/locations/apiCity?departament=${id}`,
        cache: false,
    };
    apisSendToApi(infoToSend,infoCity,apisFailed);
}

function infoCity(response){
    print;
    if(response[0]){
        $('.js-city').html("");
        $('.js-city').removeAttr('disabled').append('<option value="0" selected> - - - Select City - - - -</option>');
        response.forEach(element => {
            const option = document.createElement('OPTION');
            option.text = element.name;
            option.value = element.id;
            $('.js-city').append(option);
        });
    }else{
        $('.js-city').html("").attr('disabled',true);
    }
}

$('.js-city').on('change',function(){
    $('.js-city').removeAttr('disabled');
    apisGetOffice($(this).val());
});

function apisGetOffice(id){
    infoToSend = {
        url:`${URLAPIS}/locations/apiOffice?city=${id}`,
        cache: false,
    };
    apisSendToApi(infoToSend,infoOffice,apisFailed);
}

function infoOffice(response){
    if(response[0]){
        console.log(response[0])
        $('.js-office').html("");
        $('.js-office').removeAttr('disabled').append('<option value="0" selected> - - - Select Office - - - -</option>');
        response.forEach(element => {
            const option = document.createElement('OPTION');
            option.text = element.name;
            option.value = element.id;
            $('.js-office').append(option);
        });
    }else{
        $('.js-office').html("").attr('disabled',true);
    }
}

//----------Fin Seleccionar office dependiendo de ciudad departamento y pais--------------
