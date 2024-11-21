<script>
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropMenu() {
    document.getElementById("dropContent").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
    var dropContent = document.getElementById("dropContent");
      if (dropContent.classList.contains('show')) {
        dropContent.classList.remove('show');
      }
  }
}
</script>