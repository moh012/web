// popup messege

document.addEventListener("DOMContentLoaded", function() {
  var popup = document.getElementById("login-popup");
  var closeButton = document.getElementById("close-button");

  // إظهار واجهة المنبثقة
  function showPopup() {
    popup.style.display = "flex";
  }

  // إخفاء واجهة المنبثقة
  function hidePopup() {
    popup.style.display = "none";
  }

  // ربط زر الإغلاق بدالة إخفاء واجهة المنبثقة
  closeButton.addEventListener("click", hidePopup);

  // إخفاء واجهة المنبثقة عند النقر خارج الحدود
  window.addEventListener("click", function(event) {
    if (event.target === popup) {
      hidePopup();
    }
  });
});

// end popup messege

/* هذا الكود  وظيفته عندما يضغط المستخدم على الصورة تفتح في نفس الصفحه وعندما يضغط خارج اطار الصورة 
 يغلق الصورة ويضل في نفس الصفحة 
*/
const imageLinks = document.querySelectorAll('.image-link');

imageLinks.forEach(function(imageLink) {
  imageLink.addEventListener('click', function(event) {
    event.preventDefault();
    const imageSource = imageLink.getAttribute('href');
    const imageOverlay = document.createElement('div');
    imageOverlay.classList.add('image-overlay');
    const image = document.createElement('img');
    image.setAttribute('src', imageSource);
    imageOverlay.appendChild(image);

    const closeButton = document.createElement('span');
    closeButton.innerHTML = '&times;';
    closeButton.classList.add('close-btn');
    imageOverlay.appendChild(closeButton);

    document.body.appendChild(imageOverlay);

    closeButton.addEventListener('click', function() {
      document.body.removeChild(imageOverlay);
    });

    imageOverlay.addEventListener('click', function(event) {
      if (event.target === imageOverlay) {
        document.body.removeChild(imageOverlay);
      }
    });
  });
});


/* نهاية الكود  */

/**
* Template Name: EstateAgency
* Updated: Sep 18 2023 with Bootstrap v5.3.2
* Template URL: https://bootstrapmade.com/real-estate-agency-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Toggle .navbar-reduce
   */
  let selectHNavbar = select('.navbar-default')
  if (selectHNavbar) {
    onscroll(document, () => {
      if (window.scrollY > 100) {
        selectHNavbar.classList.add('navbar-reduce')
        selectHNavbar.classList.remove('navbar-trans')
      } else {
        selectHNavbar.classList.remove('navbar-reduce')
        selectHNavbar.classList.add('navbar-trans')
      }
    })
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Search window open/close
   */
  let body = select('body');
  on('click', '.navbar-toggle-box', function(e) {
    e.preventDefault()
    body.classList.add('box-collapse-open')
    body.classList.remove('box-collapse-closed')
  })

  on('click', '.close-box-collapse', function(e) {
    e.preventDefault()
    body.classList.remove('box-collapse-open')
    body.classList.add('box-collapse-closed')
  })

  /**
   * Intro Carousel
   */
  new Swiper('.intro-carousel', {
    speed: 900,
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });
 /**
   * Property carousel
   */
  new Swiper('#property-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.propery-carousel-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 3,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });
  

  /**
   * News carousel
   */
  new Swiper('#news-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.news-carousel-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 3,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * Property carousel
   */
  new Swiper('#property-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.propery-carousel-pagination1',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 3,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * Testimonial carousel
   */
  new Swiper('#testimonial-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.testimonial-carousel-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Property Single carousel
   */
  new Swiper('#property-single-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.property-single-carousel-pagination',
      type: 'bullets',
      clickable: true
    }
  });

})()

// start login pages js

// (function ($) {
//   "use strict";

  
//   /*==================================================================
//   [ Validate ]*/
//   var input = $('.validate-inputA .input100A');

//   $('.validate-formA').on('submit',function(){
//       var check = true;

//       for(var i=0; i<input.length; i++) {
//           if(validate(input[i]) == false){
//               showValidate(input[i]);
//               check=false;
//           }
//       }

//       return check;
//   });


  

//   $('.validate-formA .input100A').each(function(){
//       $(this).focus(function(){
//          hideValidate(this);
//       });
//   });

//   function validate (input) {
//       if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
//           if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
//               return false;
//           }
//       }
//       else {
//           if($(input).val().trim() == ''){
//               return false;
//           }
//       }
//   }

//   function showValidate(input) {
//       var thisAlert = $(input).parent();

//       $(thisAlert).addClass('alert-validate');
//   }

//   function hideValidate(input) {
//       var thisAlert = $(input).parent();

//       $(thisAlert).removeClass('alert-validate');
//   }
  
  
  

// })(jQuery);









// // page 2

// document.addEventListener('input', function (e) {
//   var input = e.target;
//   if (input.tagName.toLowerCase() === 'input' && input.type === 'text') {
//     var maxLength = parseInt(input.getAttribute('maxlength'), 10);
//     var currentLength = input.value.length;

//     if (currentLength === maxLength) {
//       var nextInput = input.nextElementSibling;
//       if (nextInput) {
//         nextInput.focus();
//       }
//     } else if (currentLength === 0) {
//       var previousInput = input.previousElementSibling;
//       if (previousInput) {
//         previousInput.focus();
//       }
//     }
//   }
// });

// document.addEventListener('keydown', function (e) {
//   var input = e.target;
//   if (e.key === 'Backspace' && input.tagName.toLowerCase() === 'input' && input.type === 'text') {
//     var currentLength = input.value.length;

//     if (currentLength === 0) {
//       var previousInput = input.previousElementSibling;
//       if (previousInput) {
//         previousInput.focus();
//       }
//     }
//   }
// });



// // page3

// (function ($) {
//   "use strict";

  
//   /*==================================================================
//   [ Validate ]*/
//   var input = $('.validate-input .input100');

//   $('.validate-form').on('submit',function(){
//       var check = true;

//       for(var i=0; i<input.length; i++) {
//           if(validate(input[i]) == false){
//               showValidate(input[i]);
//               check=false;
//           }
//       }

//       return check;
//   });


//   $('.validate-form .input100').each(function(){
//       $(this).focus(function(){
//          hideValidate(this);
//       });
//   });

//   function validate (input) {
//       if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
//           if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
//               return false;
//           }
//       }
//       else {
//           if($(input).val().trim() == ''){
//               return false;
//           }
//       }
//   }

//   function showValidate(input) {
//       var thisAlert = $(input).parent();

//       $(thisAlert).addClass('alert-validate');
//   }

//   function hideValidate(input) {
//       var thisAlert = $(input).parent();

//       $(thisAlert).removeClass('alert-validate');
//   }
  
  

// })(jQuery);






// // page4

// (function ($) {
//   "use strict";

  
//   /*==================================================================
//   [ Validate ]*/
//   var input = $('.validate-input .input100');

//   $('.validate-form').on('submit',function(){
//       var check = true;

//       for(var i=0; i<input.length; i++) {
//           if(validate(input[i]) == false){
//               showValidate(input[i]);
//               check=false;
//           }
//       }

//       return check;
//   });


//   $('.validate-form .input100').each(function(){
//       $(this).focus(function(){
//          hideValidate(this);
//       });
//   });

//   function validate (input) {
//       if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
//           if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
//               return false;
//           }
//       }
//       else {
//           if($(input).val().trim() == ''){
//               return false;
//           }
//       }
//   }

//   function showValidate(input) {
//       var thisAlert = $(input).parent();

//       $(thisAlert).addClass('alert-validate');
//   }

//   function hideValidate(input) {
//       var thisAlert = $(input).parent();

//       $(thisAlert).removeClass('alert-validate');
//   }
  
  

// })(jQuery);
// end login pages js

