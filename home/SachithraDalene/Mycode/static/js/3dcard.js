const card = document.querySelector('.card');
const container = document.querySelector(".container");
const title = document.querySelector(".titile")

//Moving Animation Event
container.addEventListener("mousemove",function(e){
    let xAxis = (window.innerWidth/2 - e.pageX)/20;
    let yAxis = (window.innerHeight/2 - e.pageY)/70;
    card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`
    console.log(e.pageX,e.pageY);

});

//Animate In
container.addEventListener('mouseenter',function(e){
    card.style.transition = "none";
    title.style.transform = "translateZ(150px)"
})


//Animate Out
container.addEventListener("mouseleave",function(e){
    card.style.transition = "all 0.5s ease"
    card.style.transform = `rotateY(0deg) rotateX(0deg)`;
    title.style.transform = "translateZ(0px)"
});
