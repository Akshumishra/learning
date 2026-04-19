function checkGrade(totalMarks, examType) {
  if (examType === "Final-exam") {
    return totalMarks >= 90;
  } else {
    return totalMarks >= 89 && totalMarks <= 100;
  }
}

console.log(checkGrade(95, "Final-exam"));
console.log(checkGrade(88, "Regular"));