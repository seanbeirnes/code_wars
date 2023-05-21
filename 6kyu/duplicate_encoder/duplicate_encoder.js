// Converts a string to a new string where each charachter in the new string is "(" if it appears only once, or ")" if that character appears more than once.
// Example: "Success"  -->  ")())())"
function duplicateEncode(word){
    dict = {}
    for(let i = 0; i < word.length; i++){
      const char = word[i].toLowerCase()
      if(!dict[char]){
        dict[char] = 1
      }else{
        dict[char] += 1
      }
    }
    let new_str = ""
    for(let i = 0; i < word.length; i++){
      const char = word[i].toLowerCase()
      if(dict[char] > 1){
        new_str += ")"
      }else{
        new_str += "("
      }
    }
  return new_str
}
