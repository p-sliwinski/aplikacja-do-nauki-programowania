const fs = require("fs");

const data = fs.readFileSync("data/js_lessons.json", "utf-8");
const lessons = JSON.parse(data);

console.log("Lekcje JavaScript:");
lessons.forEach(l => {
  console.log(l.id + ". " + l.title);
});