
document.addEventListener('input', function (e) {
    var input = e.target;
    if (input.tagName.toLowerCase() === 'input' && input.type === 'text') {
      var maxLength = parseInt(input.getAttribute('maxlength'), 10);
      var currentLength = input.value.length;
  
      if (currentLength === maxLength) {
        var nextInput = input.nextElementSibling;
        if (nextInput) {
          nextInput.focus();
        }
      } else if (currentLength === 0) {
        var previousInput = input.previousElementSibling;
        if (previousInput) {
          previousInput.focus();
        }
      }
    }
  });
  
  document.addEventListener('keydown', function (e) {
    var input = e.target;
    if (e.key === 'Backspace' && input.tagName.toLowerCase() === 'input' && input.type === 'text') {
      var currentLength = input.value.length;
  
      if (currentLength === 0) {
        var previousInput = input.previousElementSibling;
        if (previousInput) {
          previousInput.focus();
        }
      }
    }
  });8