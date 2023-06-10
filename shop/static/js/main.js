setTimeout(function() {
    var messages = document.getElementsByClassName('message');
    for (var i = 0; i < messages.length; i++) {
        messages[i].style.display = 'none';
    }}, 5000);





 var dropdownButton = document.getElementById("dropdown-button");
    var dropdownList = document.getElementById("dropdown-list");
    var dropdownContainer = document.getElementById("dropdown-container");

    dropdownContainer.addEventListener("mouseenter", function() {
      dropdownList.style.display = "block";
    });

    dropdownContainer.addEventListener("mouseleave", function() {
      dropdownList.style.display = "none";
    });




function scrollToBlock(blockId) {
  var block = document.getElementById(blockId);
  block.scrollIntoView({ behavior: 'smooth' });
}

