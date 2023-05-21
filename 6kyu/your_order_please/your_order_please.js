// Function takes in a string of words with numbers and sorts the words based on the number within each word.
// Example: "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
function order(words){
  if(!words){ return ""}
  const word_list = words.split(" ")
  let new_string = ""
  word_list.forEach( (word, i) => {
    new_string += `${word_list.filter(word => word.includes(String(i + 1)))} `
  })
  return new_string.trim()
}
