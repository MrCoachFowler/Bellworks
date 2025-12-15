//Create a function following this contract:
//Name: usernameMaker
//Purpose: Create a username for someone based on their email address
//Input: email address string <first_name>.<last_name>@<email_domain>.<top_level_domain>
//Output: username following the requirements:
//First three characters of first name, last three characters of last name and the email domain
//ex: hank.hawk@tvusd.org --> hanawktvusd
function usernameMaker(email)
{
    let nameSeperatorIndex = email.indexOf(".");
    let atSignIndex = email.indexOf("@");
    let domainSeperatorIndex = email.indexOf(".", atSignIndex);
    
    let firstName = email.substring(0, nameSeperatorIndex);
    let lastName = email.substring(nameSeperatorIndex + 1, atSignIndex);
    let domain = email.substring(atSignIndex + 1, domainSeperatorIndex);

    let answer = firstName.substring(0, 3);
    answer += lastName.substring(lastName.length - 4);
    answer += domain;

    return answer;
}


//Create a program that:

//generates a username for the following three emails and prints it
let email1 = "roger.dodger@gmail.com";
let email2 = "mac.miller@soundcloud.com";
let email3 = "keanu.reeves@matrix.org";

console.log(usernameMaker(email1))
console.log(usernameMaker(email2))
console.log(usernameMaker(email3))

//Challenge: Once done, add some defense so it will inform the user when the first or last name isn't long enough