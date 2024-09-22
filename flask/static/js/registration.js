function myformvalfn(form) {
    var firstname, lastname, email, phnumber, pwd, cnfpwd, age, passoutyear, qualification, address;

    let haserror = false;

    // Getting values from the textboxes
    firstname = form.txtfirstname.value;
    lastname = form.txtlastname.value;
    email = form.txtemail.value;
    phnumber = form.txtphnum.value;
    pwd = form.txtpwd.value;
    cnfpwd = form.cnftxtpwd.value;
    age = form.txtage.value;
    passoutyear = form.txtpassoutyear.value;
    qualification = form.txtqualification.value;
    address = form.txtaddress.value;

    // Resetting styles and error messages
    form.txtfirstname.style.border = '1px solid black';
    form.txtlastname.style.border = '1px solid black';
    form.txtemail.style.border = '1px solid black';
    form.txtphnum.style.border = '1px solid black';
    form.txtpwd.style.border = '1px solid black';
    form.cnftxtpwd.style.border = '1px solid black';
    form.txtage.style.border = '1px solid black';
    form.txtpassoutyear.style.border = '1px solid black';
    form.txtqualification.style.border = '1px solid black';
    form.txtaddress.style.border = '1px solid black';

    document.getElementById("firstnameerror").textContent = "";
    document.getElementById("lastnameerror").textContent = "";
    document.getElementById("emailerror").textContent = "";
    document.getElementById("phonenumbererror").textContent = "";
    document.getElementById("passworderror").textContent = "";
    document.getElementById("cnfpassworderror").textContent = "";
    document.getElementById("ageerror").textContent = "";
    document.getElementById("passoutyearerror").textContent = "";
    document.getElementById("qualificationerror").textContent = "";
    document.getElementById("addresserror").textContent = "";

    // Validations
    if (firstname.length === 0) {
        document.getElementById("firstnameerror").textContent = "Enter First name";
        haserror = true;
        form.txtfirstname.style.border = '1px solid red';
    }

    if (lastname.length === 0) {
        document.getElementById("lastnameerror").textContent = "Enter Last name";
        haserror = true;
        form.txtlastname.style.border = '1px solid red';
    }

    if (email.length === 0) {
        document.getElementById("emailerror").textContent = "Enter Email";
        haserror = true;
        form.txtemail.style.border = '1px solid red';
    }

    if (phnumber.length === 0) {
        document.getElementById("phonenumbererror").textContent = "Enter Phone number";
        haserror = true;
        form.txtphnum.style.border = '1px solid red';
    }

    if (!/^\d{10}$/.test(phnumber)) {
        document.getElementById("phonenumbererror").textContent = "10 digits are required";
        haserror = true;
        form.txtphnum.style.border = '1px solid red';
    }

    if (pwd.length === 0) {
        document.getElementById("passworderror").textContent = "Enter Password";
        haserror = true;
        form.txtpwd.style.border = '1px solid red';
    }

    if (cnfpwd.length === 0 || cnfpwd !== pwd) {
        document.getElementById("cnfpassworderror").textContent = "Passwords do not match";
        haserror = true;
        form.cnftxtpwd.style.border = '1px solid red';
    }

    if (age.length === 0 || isNaN(age) || age < 1 || age > 120) {
        document.getElementById("ageerror").textContent = "Enter a valid Age";
        haserror = true;
        form.txtage.style.border = '1px solid red';
    }

    if (passoutyear.length === 0 || isNaN(passoutyear) || passoutyear < 1900 || passoutyear > 2099) {
        document.getElementById("passoutyearerror").textContent = "Enter a valid Year of Passout";
        haserror = true;
        form.txtpassoutyear.style.border = '1px solid red';
    }

    if (qualification.length === 0) {
        document.getElementById("qualificationerror").textContent = "Enter Qualification";
        haserror = true;
        form.txtqualification.style.border = '1px solid red';
    }

    if (address.length === 0) {
        document.getElementById("addresserror").textContent = "Enter Address";
        haserror = true;
        form.txtaddress.style.border = '1px solid red';
    }

    return !haserror;
}

// Event listener to reset error messages and field borders when the reset button is clicked
document.getElementById("resetButton").addEventListener("click", function() {
    // Clear error messages
    document.getElementById("firstnameerror").textContent = "";
    document.getElementById("lastnameerror").textContent = "";
    document.getElementById("emailerror").textContent = "";
    document.getElementById("phonenumbererror").textContent = "";
    document.getElementById("passworderror").textContent = "";
    document.getElementById("cnfpassworderror").textContent = "";
    document.getElementById("ageerror").textContent = "";
    document.getElementById("passoutyearerror").textContent = "";
    document.getElementById("qualificationerror").textContent = "";
    document.getElementById("addresserror").textContent = "";

    // Reset input field borders
    document.getElementById("txtfirstname").style.border = '1px solid black';
    document.getElementById("txtlastname").style.border = '1px solid black';
    document.getElementById("txtemail").style.border = '1px solid black';
    document.getElementById("txtphnum").style.border = '1px solid black';
    document.getElementById("txtpwd").style.border = '1px solid black';
    document.getElementById("cnftxtpwd").style.border = '1px solid black';
    document.getElementById("txtage").style.border = '1px solid black';
    document.getElementById("txtpassoutyear").style.border = '1px solid black';
    document.getElementById("txtqualification").style.border = '1px solid black';
    document.getElementById("txtaddress").style.border = '1px solid black';
});
