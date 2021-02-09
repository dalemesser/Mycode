const slidepage = document.querySelector(".slidepage");
const firstnxtbtn = document.querySelector(".next-2");
const secprevbtn = document.querySelector(".prev-1");
const secnxtbtn = document.querySelector(".next-3");
const thridprevbtn = document.querySelector(".prev-2");
const thirdnxtbtn = document.querySelector(".next-4");
const forthprevbtn = document.querySelector(".prev-3");
const submit = document.querySelector(".submit");
const progresstext = document.querySelectorAll(".step p");
const progresscheck = document.querySelectorAll(".step .check");
const bullet = document.querySelectorAll(".step .bullet");

let max = 4;
let current = 1;

firstnxtbtn.addEventListener("click", function () {
  slidepage.style.marginLeft = "-25%";
  bullet[current - 1].classList.add("active");
  progresscheck[current - 1].classList.add("active");
  progresstext[current - 1].classList.add("active");
  current += 1;
});

secprevbtn.addEventListener("click", function () {
  slidepage.style.marginLeft = "0";
  bullet[current - 2].classList.remove("active");
  progresscheck[current - 2].classList.remove("active");
  progresstext[current - 2].classList.remove("active");
  current -= 1;
});

secnxtbtn.addEventListener("click", function () {
  slidepage.style.marginLeft = "-50%";
  bullet[current - 1].classList.add("active");
  progresscheck[current - 1].classList.add("active");
  progresstext[current - 1].classList.add("active");
  current += 1;
});

thridprevbtn.addEventListener("click", function () {
  slidepage.style.marginLeft = "-25%";
  bullet[current - 2].classList.remove("active");
  progresscheck[current - 2].classList.remove("active");
  progresstext[current - 2].classList.remove("active");
  current -= 1;
});

thirdnxtbtn.addEventListener("click", function () {
  slidepage.style.marginLeft = "-75%";
  bullet[current - 1].classList.add("active");
  progresscheck[current - 1].classList.add("active");
  progresstext[current - 1].classList.add("active");
  current += 1;
});

forthprevbtn.addEventListener("click", function () {
  slidepage.style.marginLeft = "-50%";
  bullet[current - 2].classList.remove("active");
  progresscheck[current - 2].classList.remove("active");
  progresstext[current - 2].classList.remove("active");
  current -= 1;
});

submit.addEventListener("click", function () {
  bullet[current - 1].classList.add("active");
  progresscheck[current - 1].classList.add("active");
  progresstext[current - 1].classList.add("active");
  current += 1;
  setTimeout(function () {
    alert("You're Successfully Signup");
  }, 800);
});
