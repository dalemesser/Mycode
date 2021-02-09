document.addEventListener("scroll",function(){
    if(window.scrollY > 20){
        document.querySelector(".navbar").classList.add("sticky");
        document.querySelector(".navbar .logo a span").classList.add("sticky");
           }else{
        document.querySelector(".navbar").classList.remove("sticky");
        document.querySelector(".navbar .logo a span").classList.remove("sticky");
           };
})

const menuButton = document.querySelector(".navbar .menu-btn")
menuButton.addEventListener("click",function(){
   document.querySelector(".navbar .menu").classList.toggle("active")
   document.querySelector(".menu-btn i").classList.toggle("active")
})

