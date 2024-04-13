const editButton = document.getElementById("editButton");
const name = document.getElementById("name");
const nameForm = document.getElementById("nameForm");
const email = document.getElementById("email");
const emailForm = document.getElementById("emailForm");
let editMode = false;

function toggleEdit() {
    editMode = !editMode;
    if (editMode) {
        editButton.innerHTML = "Save";
        name.style.display = "none";
        nameForm.style.display = "block";
        email.style.display = "none";
        emailForm.style.display = "block";
    } else {
        editButton.innerHTML = "Edit";
        name.style.display = "block";
        nameForm.style.display = "none";
        email.style.display = "block";
        emailForm.style.display = "none";
    }
}


const pwdButton = document.getElementById("pwdButton");
const pwdForm = document.getElementById("pwdForm");
let changeMode = false;

function changePassword() {
    changeMode = !changeMode;
    if (changeMode) {
        pwdButton.innerHTML = "Save Password";
        pwdForm.style.display = "block";
    } else {
        pwdButton.innerHTML = "Change Password";
        pwdForm.style.display = "none";
    }
}


const pwdField = document.getElementById("pwdForm").getElementsByClassName("password")[0];
const seePwdButton = document.getElementById("seePwdButton");

function seePassword() {
    if (pwdField.type === "password") {
        pwdField.type = "text";
        seePwdButton.innerHTML = "Hide Password";
    } else {
        pwdField.type = "password";
        seePwdButton.innerHTML = "See Password";
    }
}