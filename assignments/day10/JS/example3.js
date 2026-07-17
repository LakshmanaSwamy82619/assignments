let marks = [85, 42, 76, 91, 38, 67, 55, 29, 80, 40];

let pass = 0
let fail = 0
let highest = marks[0]
let lowest = marks[0]

for(let i = 0; i < marks.length; i++) {

    if(marks[i] >= 50) {
        if(marks[i] > 90) {
            console.log("Student " + (i + 1) + ": " + marks[i] + " - Topper");
            // highest=marks[i];
        } 
        else {
            console.log("Student " + (i + 1) + ": " + marks[i] + " - Pass");
        }
        pass++;
    } 
    else {
        console.log("Student " + (i + 1) + ": " + marks[i] + " - Fail");
        fail++;
    }
    if(marks[i] > highest) {
        highest = marks[i];
    }

    if(marks[i] < lowest) {
        lowest = marks[i];
    }
}

console.log("Total Passed: " + pass);
console.log("Total Failed: " + fail);
console.log("Highest Score: " + highest)
console.log("Lowest Score: " + lowest)