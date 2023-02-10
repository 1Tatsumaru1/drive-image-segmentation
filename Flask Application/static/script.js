const img_submit = document.getElementById('img_submit')
const img_form = document.getElementById('img_form')
const cover = document.getElementById('cover')

if (img_submit !== null) {
    img_submit.addEventListener('click', (e) => {
        e.preventDefault()
        cover.style.display = 'flex'
        img_form.submit()
    })
}
