// geting all required elements

const start_btn = document.querySelector(".start_btn button");
const info_box = document.querySelector(".info-box");
const exit_btn = document.querySelector(".buttons .quit");
const continue_btn = document.querySelector(".buttons .restart");
const quiz_box = document.querySelector(".quiz-box");
const option_list = document.querySelector(".optionlist");
const timeCount = document.querySelector(".timer .time-sec");
const timeLine = document.querySelector("header .time_line");
const timeoff = quiz_box.querySelector("header .time-text")



// start Quiz Button Clicked
start_btn.onclick = function(){

    info_box.classList.add("activeInfo");//show info box
}

// if exit button Clicked
exit_btn.onclick = function(){
    info_box.classList.remove("activeInfo");//hide info box
}

// if continue button Clicked
continue_btn.onclick = function(){
    info_box.classList.remove("activeInfo");//hide info box
    quiz_box.classList.add("activeQuiz");//show the quiz
    showQuestions(0);
    queCounter(1);
    startTimer(15);
    startTimerLine(0);
    next_btn.style.display = "none";
    
}

let que_count = 0;
let que_numb =1 ;
let counter ;
let timeValue =15;
let widthValue = 0;
let userScore = 0;


const next_btn = document.querySelector(".next-btn");
const result_box = document.querySelector(".result");
const restart_quiz = document.querySelector(".result .buttons .restart");
const quit_quiz = document.querySelector(".result .buttons .quit");

quit_quiz.onclick = function(){
    window.location.reload();
}

//If nextButoon Clicked
next_btn.onclick = function(){
    if(que_count < questions.length-1){
        que_count ++;
        que_numb ++;
        showQuestions(que_count);
        queCounter(que_numb);
        clearInterval(counter);
        startTimer(timeValue);
        clearInterval(counterLine)
        startTimerLine(widthValue);
        next_btn.style.display = "none";
        timeoff.textContent = "Time Left";
        
    }
    else{
        showResultBox();
        
    }


    };


//getting questions and options from array

function showQuestions(index){
    const que_text = document.querySelector(".que-text");
    
    let que_tag = '<span>'+ questions[index].number +"."+ questions[index].question + '</span>';
    let option_tag = '<div class="option">'+questions[index].options[0]+'<span></span></div>'
                    +'<div class="option">'+questions[index].options[1]+'<span></span></div>'
                    +'<div class="option">'+questions[index].options[2]+'<span></span></div>'
                    +'<div class="option">'+questions[index].options[3]+'<span></span></div>';
    que_text.innerHTML = que_tag;
    option_list.innerHTML = option_tag;
    const option = option_list.querySelectorAll(".option");
    for(let i = 0 ; i < option.length ; i ++){
        option[i].setAttribute("onclick","optionSelected(this)");
     }
    
};

let tickicon ="<div class='icon tick'><i class='fas fa-check'></i></div>"
let crossicon ="<div class='icon cross'><i class='fas fa-cross'></i></div>"

function optionSelected(answer){
    clearInterval(counter);
    clearInterval(counterLine);
    let userAnswer = answer.textContent;
    let correctAns = questions[que_count].ansewer;
    let alloptions = option_list.children.length;

    if(userAnswer == correctAns){
        userScore +=1;
        console.log(userScore)
        answer.classList.add("correct");
        answer.insertAdjacentHTML('beforeend',tickicon);
    }
    else{
        answer.classList.add("incorrect");
        answer.insertAdjacentHTML('beforeend',crossicon);

        //if ansewer is incorrect then automatically selected the correct ansewer
        for(let i = 0 ; i < alloptions ; i ++){
            if( option_list.children[i].textContent == correctAns ){
                option_list.children[i].setAttribute("class","option correct");
                option_list.children[i].insertAdjacentHTML('beforeend',tickicon);
            }
         }
    };
    // once user selected disabled all options....
    for (let i = 0 ; i < alloptions; i++ ){
        option_list.children[i].classList.add("disabled")
    }
    next_btn.style.display = "block";
 

    


};

function showResultBox(){
    info_box.classList.remove('activeInfo');
    quiz_box.classList.remove("activeQuiz");
    result_box.classList.add("activeResult");
    const score = result_box.querySelector(".score-text");
    if (userScore > 3){
        let scoreTag = "<span>and Congrats!,You got only <p>"+ userScore + "</p> out of <p>" + questions.lenght +"</p></span>" ;
        score.innerHTML = scoreTag;  
    }
    else if(userScore > 1){
        let scoreTag = '<span>and sorry,You got only <p>'+ userScore + "</p> out of <p>"+questions.length +"</p></span>";
        score.innerHTML = scoreTag; 
    }
    else{
        let scoreTag = '<span> and sorry, Your got only <p>'+ userScore + "</p> out of <p>"+ questions.length + "<p></span>";
    }
}

function queCounter(index){
    const bottom_ques_counter =  document.querySelector(".total-que");

    let bottom_ques_counter_tag = '<span><p>'+ index  +'</p> of <p>'+ questions.length+'</p>Questions</span>'
    bottom_ques_counter.innerHTML =bottom_ques_counter_tag

}

function startTimer(time){
    counter = setInterval(timer,1000);
    function timer(){
        timeCount.textContent = time;
        time --;
        if (time < 9){
            let addZero = timeCount.textContent;
            timeCount.textContent = "0"+ addZero;
        }
        if(time < 0){
            next_btn.style.display = "block";
            clearInterval(counter);
            timeCount.textContent = "00";
            timeoff.textContent = "Time off";

            let correctAns = questions[que_count].ansewer;
            let alloptions = option_list.children.length;

        

             for (let i = 0 ; i < alloptions; i ++){
                if(option_list.children[i].textContent == correctAns){
                    option_list.children[i].setAttribute("class","option correct");
                    option_list.children[i].insertAdjacentHTML('beforeend',tickIcon);
                }
                
             }

             for (let i = 0 ; i < alloptions; i++ ){
                option_list.children[i].classList.add("disabled")
            }
            
        }
    }

}

function startTimerLine(time){
    counterLine = setInterval(timer,29);
    function timer(){
        time += 1;
        timeLine.style.width = time + "px";

        if (time > 549){
            clearInterval(counterLine)
  
    }}

}