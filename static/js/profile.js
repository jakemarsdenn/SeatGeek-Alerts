const editBtn = document.getElementById("edit-button");
const saveNameBtn = document.getElementById("save-name-button");
const savePasswordBtn = document.getElementById("save-password-button");
const seePasswordBtn = document.getElementById("see-password-button");
const nameField = document.getElementById("name-field");
const passwordField = document.getElementById("password-field");

let editMode = false;


function toggleEdit() {
    editMode = !editMode;
    if (editMode) {
        editBtn.innerHTML = "Cancel";
        nameField.removeAttribute("disabled");
        passwordField.removeAttribute("disabled");
        saveNameBtn.style.display = "block";
        savePasswordBtn.style.display = "block";
        seePasswordBtn.style.display = "block";
    } else {
        editBtn.innerHTML = "Edit";
        nameField.setAttribute("disabled", true);
        passwordField.setAttribute("disabled", true);
        saveNameBtn.style.display = "none";
        savePasswordBtn.style.display = "none";
        seePasswordBtn.style.display = "none";
        passwordField.type = "password";
        seePasswordBtn.innerHTML = "See Password";
    }
}


function seePassword() {
    if (passwordField.type === "password") {
        passwordField.type = "text";
        seePasswordBtn.innerHTML = "Hide Password";
    } else {
        passwordField.type = "password";
        seePasswordBtn.innerHTML = "See Password";
    }
}



