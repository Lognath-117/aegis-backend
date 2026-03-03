fetch("http://127.0.0.1:5000/predict", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({ text: "Aliens landed in India yesterday" })
})
.then(res => res.json())
.then(data => console.log(data));