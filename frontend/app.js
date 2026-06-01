const btt = document.querySelector("button");
btt.addEventListener("click", async () => {
  const target = document.querySelector("#target").value;
  const port = document.querySelector("#port").value;
  
  const res = await fetch("http://127.0.0.1:3000", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
        },
    body: JSON.stringify({
      "target": target,
      "port": port
    })
  });
    btt.disabled = true;
    const data = await res.json();
    const m = document.querySelector("p");
    if (res.status === 200){
      m.innerText = data.message;
      m.style.color = "dark green";
    }else{
      m.innerText = data.message;
      m.style.color = "red"
    }
    btt.disabled = false;
});
