
function CreateLiElement(text_type){

    let text_warning="text-warning";
    let text_success="text-success";
    let text_danger="text-danger";
    let text=""

    if (text_type == "warning"){
        text=text_warning
    }
    else if (text_type == "danger"){
        text=text_danger
    }
    else if (text_type == "success"){
        text=text_success
    }else{
        text=""
    }


    let element=document.createElement("li");
    element.setAttribute("class","list-group-item"+" "+text);
    return element;

}


function AppendElements(list,ul,text_type){

    for(let i in list){

        li=CreateLiElement(text_type)
        li.innerHTML=list[i];
        ul.appendChild(li);
    }
}



function ResetUI(){
    document.getElementById("alert-board").innerHTML="";
    document.getElementById("indicator_board").innerHTML="";
    document.getElementById("stored").innerHTML="";
    document.getElementById("links").innerHTML="";
    document.getElementById("differences").innerHTML="";

}




function OutputResponse(response_obj){
    
    ResetUI();
    success="<div class='alert alert-success' role='alert'><p id='alert'></p></div>"+
    "</div>";
    warning="<div class='alert alert-warning' role='alert'><p id='alert'></p></div>"+
    "</div>";
    alert_type=""
    
    console.log(response_obj)
    
    let message=response_obj.response.message;
    let links=response_obj.response.links;
    let differences=response_obj.response.differences;
    let stored=response_obj.response.stored;

    if (links.length > 0){

        alert_type=success;    

        if (differences.length==0){

            differences.push("No differences detected");
        }
        
    }else{
        alert_type=warning
    }
    document.getElementById("alert-board").innerHTML=alert_type;
    document.getElementById("alert").innerHTML=message;

    links_ul_element=document.getElementById("links");
    stored_ul_element=document.getElementById("stored");
    differences_ul_element=document.getElementById("differences");

    AppendElements(links,links_ul_element,"success");
    AppendElements(stored,stored_ul_element,"");
    AppendElements(differences,differences_ul_element,"danger");

    


}

//+++++++++++++++++++++HTTP REQUEST +++++++++++++++++++++
function HttpRequest(message_content){

    let response="";
    const xhttp=new XMLHttpRequest();

    xhttp.onload=function(){
        if (this.readyState==4 && this.status==200){
            response=this.responseText;
            response=JSON.parse(response);
            OutputResponse(response);
            
        }else{
            console.log("bad response");
        }
       
    }


    xhttp.open("GET","/url/?target_url="+message_content,true);
    xhttp.send();    
    

    
}


function fetchurl(){
    
    ResetUI()
    warning="<div class='alert alert-warning' role='alert'><p id='alert'></p></div>"+
    "</div>";
    indicator="<div id='indicator'></div>";

    document.getElementById("indicator_board").innerHTML=indicator;
    document.getElementById("alert-board").innerHTML=warning;
    document.getElementById("alert").innerHTML="Fetching url";

    let element=document.getElementById("search_url");
    let value=element.value;
    HttpRequest(value);


}


function clear(){

   let browser=document.getElementById("search_url");
   browser.value="";
   browser.innerHTML="";

}


document.getElementById("search_button").addEventListener("click",fetchurl);
document.getElementById("search_clear").addEventListener("click",clear);