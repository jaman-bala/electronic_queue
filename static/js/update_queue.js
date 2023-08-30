//// update_call_page.js
//
//function updateDisplayQueue() {
//    var xhr = new XMLHttpRequest();
//    xhr.onreadystatechange = function () {
//        if (xhr.readyState === 4 && xhr.status === 200) {
//            document.getElementById("queue-container").innerHTML = xhr.responseText;
//        }
//    };
//    xhr.open("GET", display_queue_url, true);
//    xhr.send();
//}
//
//function updateCallPage() {
//    var xhr = new XMLHttpRequest();
//    xhr.onreadystatechange = function () {
//        if (xhr.readyState === 4 && xhr.status === 200) {
//            document.getElementById("call-container").innerHTML = xhr.responseText;
//            updateDisplayQueue(); // Добавим обновление display_queue
//        }
//    };
//    xhr.open("GET", "{% url 'call_number' %}", true);
//    xhr.send();
//}
//
//document.addEventListener("DOMContentLoaded", function () {
//    setInterval(updateCallPage, 5000);
//    setInterval(updateDisplayQueue, 5000);
//});


function updateDisplayQueue() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var responseData = JSON.parse(xhr.responseText);
            document.getElementById("queue-container").innerHTML = responseData.queueHtml;
            document.getElementById("last-number").innerText = responseData.lastNumber;
        }
    };
    xhr.open("GET", queue_url, true);
    xhr.send();
}
