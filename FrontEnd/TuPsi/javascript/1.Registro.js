const form = document.getElementById('contacto') || document.getElementById('registro')
form.addEventListener('submit', async function getFormData(e) {
    e.preventDefault(); 
    const form = document.getElementById(e.target.id),
        formData = new FormData(form)
        for (const pair of formData.entries()) {
            console.log(`${pair[0]}, ${pair[1]}`);
            }
}
)