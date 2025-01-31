
function initializeAuthorDiv(divID) {

    var authorDiv = document.getElementById(divID);
    authorDiv.classList.add("author_box");

    var authorContainerDiv = document.getElementById("author_box_container");

    var label1 = document.createElement("label");
    var input1 = document.createElement("input");

    var label2 = document.createElement("label");
    var input2 = document.createElement("input");

    var label3 = document.createElement("label");
    var input3 = document.createElement("input");

    var addButton = document.createElement("button");
    addButton.classList.add("addAuthor");
    addButton.innerText = "Add Author";
    addButton.addEventListener('click', function (){
        addAuthor(divID);
    });

    label1.innerText = "First Name (Required):";
    label1.setAttribute("for", "fname1");

    input1.setAttribute("type", "text");
    input1.setAttribute("id", "fname1");
    input1.setAttribute("name", "fname1");

    label2.innerText = "Last Name (Required):";
    label2.setAttribute("for", "lname1");

    input2.setAttribute("type", "text");
    input2.setAttribute("id", "lname1");
    input2.setAttribute("name", "lname1");

    label3.innerText = "Email (Required):";
    label3.setAttribute("for", "email1");

    input3.setAttribute("type", "text");
    input3.setAttribute("id", "email1");
    input3.setAttribute("name", "email1");

    authorDiv.appendChild(label1);
    authorDiv.appendChild(input1);
    authorDiv.appendChild(label2);
    authorDiv.appendChild(input2);
    authorDiv.appendChild(label3);
    authorDiv.appendChild(input3);
    authorContainerDiv.appendChild(addButton);

}

function addAuthor(divElementID){
    var arrayLength = getDivElements(divElementID);
    var authorDiv = document.getElementById(divElementID);

    var lineBreak = document.createElement("br");

    var label1 = document.createElement("label");
    var input1 = document.createElement("input");

    var label2 = document.createElement("label");
    var input2 = document.createElement("input");

    var label3 = document.createElement("label");
    var input3 = document.createElement("input");

    var autindex = arrayLength + 1;

    label1.innerText = "First Name:";
    label1.setAttribute("for", "fname" + autindex);

    input1.setAttribute("type", "text");
    input1.setAttribute("id", "fname" + autindex);
    input1.setAttribute("name", "fname" + autindex);

    label2.innerText = "Last Name:";
    label2.setAttribute("for", "lname" + autindex);

    input2.setAttribute("type", "text");
    input2.setAttribute("id", "lname" + autindex);
    input2.setAttribute("name", "lname" + autindex);

    label3.innerText = "Email:";
    label3.setAttribute("for", "email" + autindex);

    input3.setAttribute("type", "text");
    input3.setAttribute("id", "email" + autindex);
    input3.setAttribute("name", "email" + autindex);

    var div_box = document.createElement("div");
    var div_label = document.createElement("label");
    div_label.innerText = "AuDiv:";
    div_label.setAttribute("for", "AuDiv" + autindex);
    div_box.classList.add('child')

    input3.setAttribute("type", "div");
    input3.setAttribute("id", "AuDiv" + autindex);
    input3.setAttribute("name", "AuDiv" + autindex);

    authorDiv.appendChild(div_box)
    div_box.appendChild(lineBreak);
    div_box.appendChild(label1);
    div_box.appendChild(lineBreak);
    div_box.appendChild(input1);
    div_box.appendChild(lineBreak);
    div_box.appendChild(label2);
    div_box.appendChild(lineBreak);
    div_box.appendChild(input2);
    div_box.appendChild(lineBreak);
    div_box.appendChild(label3);
    div_box.appendChild(lineBreak);
    div_box.appendChild(input3);

}
