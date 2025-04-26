const [N, ingredients] = require("fs")
  .readFileSync(0, "utf-8")
  .trim()
  .split("\n")

const cheeseSet = new Set()

const items = ingredients.split(" ")
for (const item of items) {
  if (item.endsWith("Cheese")) {
    cheeseSet.add(item)
  }
}

if (cheeseSet.size >= 4) {
  console.log("yummy")
} else {
  console.log("sad")
}
