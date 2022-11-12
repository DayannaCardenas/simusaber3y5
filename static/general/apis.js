
//obtiene el token
function apisCsrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function apisGetCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = apisGetCookie('csrftoken');

//funcion general para llamar apis
function apisSendToApi(filters,sendFunction,sendErrorFunction){
    var method='';
    var async='';
    if (filters.method!=null){
        method=filters.method;
    }else{
        method='GET';
    }
    if (filters.cache!=null){
        cache=filters.cache;
    }else{
        cache=true;
    }
    if (sendErrorFunction==null){
        errorFunction=apis_failed;
    }else{
        errorFunction=sendErrorFunction;
    }
    if (filters.async!=null){
        async=filters.async;
    }else{
        async=true;
    }
    $.ajax({
        // dataType:'json',
        method: method,
        async: async,
        cache:cache,
        data: JSON.stringify(filters.data),
        url: filters.url,
        contentType:"application/json",
        //headers: filters.headers,
        beforeSend: function(xhr, settings) {
            xhr.url = settings.url;
            if (!apisCsrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken );
            }
        }, 
        success: function(response){ sendFunction(response, {'element':filters.element, 'redirectURL':filters.redirectURL}); }
    }).fail(function(response){errorFunction(response,{'element':filters.element, 'redirectURL':filters.redirectURL, 'data':filters.data})});
}

function apisFailed(response, kwargs){
   
    if(kwargs.element){
        kwargs.element.prop("disabled", false);
        kwargs.element.children('span').addClass('d-none');
    }
    let obj= response.responseJSON;
    if(response.status != 0){
        var m=0;
        for (var key in obj){
            
            if(String(obj[m]).includes('Las credenciales de autenticación no se proveyeron.')){
                window.location.replace(URLAPIS+'/accounts/login/');
            }
            else {
                if(obj[m])
                {
                    let errors=[];
                    let errorLabel=[];
                    var j=0;
                    let x=JSON.stringify(obj[m]).split('"');
                    
                    for (var i = 1; i < x.length; i++) {
                        errorLabel[j]= x[i];
                        i=i+3;
                        j++;
                    }
                    j=0;
                    for (var i = 3; i < x.length; i++) {
                        errors[j]= x[i];
                        i=i+3;
                        j++;
                        
                    }
                    apisShowError(errors,errorLabel,kwargs.data[m]);
                }
                else{
                    let errors=[];
                    let errorLabel=[];
                    var j=0;
                    let x=JSON.stringify(obj).split('"');
                    
                    for (var i = 1; i < x.length; i++) {
                        errorLabel[j]= x[i];
                        i=i+3;
                        j++;
                    }
                    j=0;
                    for (var i = 3; i < x.length; i++) {
                        errors[j]= x[i];
                        i=i+3;
                        j++;
                        
                    }
                    alert(errors)
                }                
            }
            m++;
        }
    }
    else{
        alert("Error por favor revise su conexión con internet");
    } 
}