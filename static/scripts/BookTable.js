window.onload= ()=>{
let CheckBoxesLabels= document.querySelectorAll('.labelCheckBox');
CheckBoxesLabels.forEach(label=>{
    label.addEventListener('click', (event)=>{
        console.log(event.target.classList.toggle("active"))
    })
})

}
