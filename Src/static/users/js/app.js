document.addEventListener("DOMContentLoaded", function() {

});

// Create a "close" button and append it to each list item
var myNodelist = document.getElementsByTagName("li");
var i;
for (i = 0; i < myNodelist.length; i++) {
  var span = document.createElement("span");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  myNodelist[i].appendChild(span);
}

// Click on a close button to hide the current list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
      div.remove();
  }
}

// Create a new list item when clicking on the "Add" button
document.querySelector('.btn').addEventListener('click', newElement);
function newElement(e) {
    var li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between";
    var inputValue = document.getElementById("new_task").value;

    //saving into local storage
    const task = document.getElementById("new_task").value;
    let tasks;
    if(localStorage.getItem('tasks') === null) {
      tasks = [];
    } else {
      tasks = JSON.parse(localStorage.getItem('tasks'));

    }

    var flag = true;
    tasks.forEach(myfunc);
    function myfunc(item) {
        if (item == task) {
            alert("already exist!")
            flag = false;
        } 
    };

    
    if (flag) {
        tasks.push(task);
        localStorage.setItem('tasks', JSON.stringify(tasks));
        var t = document.createTextNode(inputValue);
        li.appendChild(t);
        if (inputValue === '') {
            alert("You must write something!");
        } else {
            document.querySelector('ul.list-group').appendChild(li);
        }
        document.getElementById("new_task").value = "";
        
        
        var span = document.createElement("SPAN");
        var txt = document.createTextNode("\u00D7");
        span.className = "close";
        span.appendChild(txt);
        li.appendChild(span);
    }
    console.log(e)
    e.preventDefault();
    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
          var div = this.parentElement;
            div.remove();
        }
    }
    
}
//remove all tasks by clicking the buttom
document.querySelector('.clear-tasks').addEventListener('click', onClick_qq);
function onClick_qq(e){

    console.log(' َAll tasks has been removed by Clicking the buttom');
    var ul = document.querySelector('ul.list-group')
    ul.remove()
    e.preventDefault();
}

function onload_func() {
    var taskss = JSON.parse(localStorage.getItem('tasks'));
    console.log(taskss);
    
    function myfunc(item) {
        
        console.log(item);
        var li = document.createElement("li");
        li.className = "list-group-item d-flex justify-content-between";
        var inputValue = item;

        var t = document.createTextNode(inputValue);
        li.appendChild(t);
        document.querySelector('ul.list-group').appendChild(li);
        var span = document.createElement("SPAN");
        var txt = document.createTextNode("\u00D7");
        span.className = "close";
        span.appendChild(txt);
        li.appendChild(span);
        
        for (i = 0; i < close.length; i++) {
            close[i].onclick = function() {
              var div = this.parentElement;
                div.remove();
            }
        }

    };
    taskss.forEach(myfunc);
}
//localStorage.clear();

