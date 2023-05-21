// Takes in a number and returns the sum of a list of number up to that number which are multipels of 3 or 5.
// Example: 10 --> 23
function solution(number){
 let result = 0
  for(let i = 0; i < number; i++){
    if (i % 3 === 0 || i % 5 === 0){
      result += i
    }
  }
  return result
}
