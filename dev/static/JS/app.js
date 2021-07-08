//changeActive(param) - changes current button to inactive
//                      and will eventually update the form

function changeActive(param) {
    const currActive = document.getElementById('active')
    currActive.id = 'inactive'
    currActive.classList.remove('active')
    param.id = 'active'
    param.classList.add('active')
}