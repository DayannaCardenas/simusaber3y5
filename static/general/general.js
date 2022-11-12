function generalRedirectPage(response, kwargs){
    console.log(kwargs);
    if(kwargs.redirectURL){
        window.location.replace(URLAPIS+kwargs.redirectURL);
    }
    
}


