//Create a function following this contract:
//Name:pCounter
//Purpose: Count all the p tags in an html body
//Input: a page of html data
//Output: the number of p tags in the html

//Create a function following this contract:
//Name:pTagReader
//Purpose: Return a list of all the strings in a p tag in the html body
//Input: a page of html data
//Output: a list of each string in the p tag on the page


let htmlBody1 = `<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Frogs</title>
    </head>
    <body>
    <h1>All About Frogs</h1>

    <p>Frogs are amphibians that live both in water and on land.</p>
    <p>They have strong legs that help them jump great distances.</p>
    <p>Frogs play an important role in ecosystems by controlling insect populations.</p>
    <p>Some frog species are brightly colored to warn predators of their toxicity.</p>

    </body>
    </html>`

let htmlBody2 = `<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Dragons</title>
    <style>
        body {
        font-family: Arial, sans-serif;
        margin: 20px;
        }
        .fire-dragons {
        background-color: #ffebe6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        }
        .ice-dragons {
        background-color: #e6f2ff;
        padding: 15px;
        border-radius: 8px;
        }
    </style>
    </head>
    <body>
    <h1>Dragons of Myth and Legend</h1>

    <div class="fire-dragons">
        <h2>Fire Dragons</h2>
        <p>Fire dragons are often described as powerful beings that breathe flames and guard treasures.</p>
        <p>They are feared in many stories but also respected for their immense strength and wisdom.</p>
    </div>`

let htmlBody3 = `<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>The Color Purple</title>
    <style>
        body {
        font-family: Georgia, serif;
        margin: 20px;
        background-color: #f7f3fa;
        }
        .history {
        background-color: #e0c3f7;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        }
        .symbolism {
        background-color: #d1b3ff;
        padding: 15px;
        border-radius: 8px;
        }
    </style>
    </head>
    <body>
    <h1>The Color Purple</h1>

    <div class="history">
        <h2>History</h2>
        <p>Purple dye was once so rare and expensive that it was worn only by royalty and the wealthy elite.</p>
        <p>It was traditionally made from sea snails, a long and labor-intensive process that made it highly valued.</p>
    </div>

    <div class="symbolism">
        <h2>Symbolism</h2>
        <p>Today, purple is often associated with creativity, imagination, and spiritual depth.</p>
        <p>It can represent both luxury and mystery, making it a favorite color in art and design.</p>
    </div>

    </body>
    </html>`


//Verify your outputs

console.log(pCounter(htmlBody1)) //4
console.log(pTagReader(htmlBody1)) //['Frogs are amphibians that live both in water and on land.', 'They have strong legs that help them jump great distances.', 'Frogs play an important role in ecosystems by controlling insect populations.', 'Some frog species are brightly colored to warn predators of their toxicity.']

console.log(pCounter(htmlBody2)) //2
console.log(pTagReader(htmlBody2)) //['Fire dragons are often described as powerful beings that breathe flames and guard treasures.', 'They are feared in many stories but also respected for their immense strength and wisdom.']

console.log(pCounter(htmlBody3)) //4
console.log(pTagReader(htmlBody3)) //['Purple dye was once so rare and expensive that it was worn only by royalty and the wealthy elite.', 'It was traditionally made from sea snails, a long and labor-intensive process that made it highly valued.', 'Today, purple is often associated with creativity, imagination, and spiritual depth.', 'It can represent both luxury and mystery, making it a favorite color in art and design.']