//tutorial https://www.youtube.com/watch?v=RsPWEmfOQdU&ab_channel=WEBCIFAR

const sections = document.querySelectorAll('section')
const navLi = document.querySelectorAll('nav ul li')

window.addEventListener('scroll', ()=> {
    let current = '';
    console.log(pageYoffset);

    sections.forEach( section => {
        const sectionTop = section.offsetTop;
        // console.log(sectionTop)
        const sectionHeight = section.clientHeight;

    })
})



