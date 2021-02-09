
document.addEventListener("scroll",function(){
    if(window.scrollY > 20){
        document.querySelector(".navbar").classList.add("sticky");
        document.querySelector(".navbar .logo a span").classList.add("sticky");
           }else{
        document.querySelector(".navbar").classList.remove("sticky");
        document.querySelector(".navbar .logo a span").classList.remove("sticky");
           };
   if(window.scrollY > 500){
      document.querySelector(".scroll-up-button").classList.add("show");
   }
   else{
      document.querySelector(".scroll-up-button").classList.remove("show");
   }
})

document.querySelector(".scroll-up-button").addEventListener("click",function(){
   alert("hi");
})

const menuButton = document.querySelector(".navbar .menu-btn")
menuButton.addEventListener("click",function(){
   document.querySelector(".navbar .menu").classList.toggle("active")
   document.querySelector(".menu-btn i").classList.toggle("active")
})

