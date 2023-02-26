function copyToClipboard(text) {
    var input = document.createElement('textarea');
    input.value = text;
    document.body.appendChild(input);
    input.select();
    document.execCommand('copy');
    document.body.removeChild(input);
}

var copyBtn = document.getElementById('copy-btn');
var result = document.getElementById('result');
copyBtn.addEventListener('click', function() {
    copyToClipboard(result.textContent);
});

var preloader = document.getElementById('preloader');
function myFunction() { 
    preloader.style.display = 'none';
}
  