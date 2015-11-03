var link = window.location.href.split("/");

$(document).ready(function(){
    //We are at a page
    var current_page = link[3];
    var button_links = document.getElementsByClassName("button");
    
    for(var i=0; i<button_links.length; i++){
      if (button_links[i].parentElement.href.split("/")[3] == current_page) {
        if (current_page == " ") {
          //homepage
          $("a#home li div div").addClass("current-page");
        }
        $("a#" + current_page + " li div div").addClass("current-page");
      }
    }
    
  });