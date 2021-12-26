function Signup(URL){
    let username=document.getElementById("username").value;
    let email=document.getElementById("email").value;
    let password=document.getElementById("password").value;
    let re_password=document.getElementById("re_password").value;

    let data={
        username:username,
        email:email,
        password:password,
        re_password:re_password
    }


    if(username=="" && email=="" && password=="" && re_password ==""){
        alert("please enter all fields")
        }
else{
    if(password==re_password){
        SubmitData(data,URL,path='/')
    }
    else{
        alert("password dosent match")
    }
}
    }



function Login(URL){
    let username=document.getElementById("login_username").value;
    let password=document.getElementById("login_password").value;

    let data={
        username:username,
        password:password
}
if(username=="" &&  password==""){
    alert("please enter all fields")
}
else{
    SubmitData(data,URL,path='/user/'+username)

}

}




