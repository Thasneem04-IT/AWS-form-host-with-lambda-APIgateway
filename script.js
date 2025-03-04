document.getElementById("dataForm").addEventListener("submit", async function(event) {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  const response = await fetch("https://9jmnls5e5g.execute-api.ap-south-1.amazonaws.com/prod/submit-form", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email })
  });

  const result = await response.json();
  alert(result.message || "Form submitted successfully!");
});
