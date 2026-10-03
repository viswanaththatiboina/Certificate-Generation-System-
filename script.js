const form = document.getElementById("certificateForm");
const result = document.getElementById("result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  result.textContent = "Agent is generating your certificate...";

  const payload = Object.fromEntries(new FormData(form).entries());

  try {
    const response = await fetch("/api/generate", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (!response.ok) {
      result.textContent = data.error || "Generation failed.";
      return;
    }

    const id = data.certificate.certificate_id;
    result.innerHTML =
      `Certificate generated successfully: <strong>${id}</strong><br>` +
      `<a class="download" href="/certificate/${id}">View Certificate</a>`;
  } catch (error) {
    result.textContent = "Server error. Please try again.";
  }
});
