/*Estoy usando la Api para usar el valor de la UF en cada casa*/
document.addEventListener("DOMContentLoaded", function() {
  function transformarUF() {
      var montoCLP = document.getElementById("montoCLP").innerText;
      var apiKey = "05fea24b031a7d8443d12ea5fa9526902e14db47";
      var url = "https://api.sbif.cl/api-sbifv3/recursos_api/uf/2020/01?apikey=" + apiKey + "&formato=json";

      fetch(url)
          .then(response => response.json())
          .then(data => {
              var valorUF = data.UFs[0].Valor.replace(".", "").replace(",", ".");
              var resultadoUF = (parseFloat(montoCLP) / parseFloat(valorUF)).toFixed(2);
              
              document.getElementById("valorUF").innerText = resultadoUF;
          })
          .catch(error => {
              console.error('Error al obtener datos:', error);
              document.getElementById("resultado").innerText = "Hubo un error al obtener los datos. Por favor, inténtelo de nuevo más tarde.";
          });
  }

  transformarUF();
});

document.addEventListener('DOMContentLoaded', function () {
  // Inicializa Swiper
  var swiper = new Swiper('.swiper', {
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: 1,
    spaceBetween: 10,
    // Más opciones según tus necesidades
  });
});






/*localStorage.setItem("pato", "lucas");

console.log(localStorage.getItem("pato"));*/


document.addEventListener('DOMContentLoaded', function() {
  const propertySelect = document.getElementById('property');
  const properties = [
    { id: 'propiedad1', name: '730 Eyzaguirre' },
    { id: 'propiedad2', name: '921 Varas Mena' },
    { id: 'propiedad3', name: '9423 Av. La Florida' },
    { id: 'propiedad4', name: '1576 Serrano' },
    { id: 'propiedad5', name: '20 El Algarrobal' },
    { id: 'propiedad6', name: '756 Volcán Choshuenco' },
  ];

  properties.forEach(property => {
    const option = document.createElement('option');
    option.value = property.id;
    option.textContent = property.name;
    propertySelect.appendChild(option);
  });
});

  // Validación para el formulario de agendar visita

document.addEventListener('DOMContentLoaded', () => {
  const appointmentForm = document.getElementById('appointmentForm');
  const fullNameInput = document.getElementById('fullName');
  const emailInput = document.getElementById('email');
  const phoneInput = document.getElementById('phone');
  const propertySelect = document.getElementById('property');
  const dateInput = document.getElementById('date');
  const timeInput = document.getElementById('time');
  const termsCheckbox = document.getElementById('terms');
  const warningsParagraph = document.getElementById('warnings');
  const successMessage = document.getElementById('successMessage');

  if (appointmentForm) {
      appointmentForm.addEventListener('submit', e => {
          e.preventDefault();
          let warnings = '';
          let entrar = false;
          const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
          const regexPhone = /^[0-9]{9,15}$/;

          warningsParagraph.innerHTML = '';

          if (fullNameInput.value.trim() === '' || !/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(fullNameInput.value)) {
              warnings += 'El nombre completo es inválido. <br>';
              entrar = true;
          }

          if (!regexEmail.test(emailInput.value)) {
              warnings += 'El email no es válido. Por favor, utiliza el formato nombre@apellido.com <br>';
              entrar = true;
          }

          if (!phoneInput.value || !regexPhone.test(phoneInput.value)) {
              warnings += 'El número de teléfono es inválido. Debe contener entre 9 y 15 dígitos. <br>';
              entrar = true;
          }

          if (!propertySelect.value) {
              warnings += 'Debe seleccionar una propiedad. <br>';
              entrar = true;
          }

          if (!dateInput.value) {
              warnings += 'Debe seleccionar una fecha. <br>';
              entrar = true;
          }

          if (!timeInput.value) {
              warnings += 'Debe seleccionar una hora. <br>';
              entrar = true;
          }

          if (!termsCheckbox.checked) {
              warnings += 'Debe aceptar los términos y condiciones. <br>';
              entrar = true;
          }

          if (entrar) {
              warningsParagraph.innerHTML = warnings;
          } else {
              warningsParagraph.innerHTML = '';
              successMessage.style.display = 'block';
              appointmentForm.reset();
              setTimeout(() => {
                  successMessage.style.display = 'none';
              }, 5000);
          }
      });
  }
});



    document.addEventListener('DOMContentLoaded', () => {
      //* Validación para el formulario de inicio de sesión*/
      const loginForm = document.getElementById('form');
      const emailInput = document.getElementById('email');
      const passwordInput = document.getElementById('password');
      const warningsParagraph = document.getElementById('warnings');

      if (loginForm && emailInput && passwordInput && !document.getElementById('confirm_password')) {
          loginForm.addEventListener('submit', e => {
              e.preventDefault();
              let warnings = '';
              let entrar = false;
              const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
              warningsParagraph.innerHTML = '';

              if (!regexEmail.test(emailInput.value)) {
                  warnings += 'El email no es válido. Por favor, utiliza el formato nombre@apellido.com <br>';
                  entrar = true;
              }

              if (passwordInput.value.length < 8) {
                  warnings += 'La contraseña debe tener más de 8 caracteres <br>';
                  entrar = true;
              }

              if (entrar) {
                  warningsParagraph.innerHTML = warnings;
              } else {
                  warningsParagraph.innerHTML = 'Enviado';
                  loginForm.submit();  
              }
          });
      }

  /* Validación para el formulario de registro*/
  const confirmPasswordInput = document.getElementById('confirm_password');

  if (loginForm && emailInput && passwordInput && confirmPasswordInput) {
      loginForm.addEventListener('submit', e => {
          e.preventDefault();
          let warnings = '';
          let entrar = false;
          const regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
          warningsParagraph.innerHTML = '';

          if (!regexEmail.test(emailInput.value)) {
              warnings += 'El email no es válido. Por favor, utiliza el formato nombre@apellido.com <br>';
              entrar = true;
          }

          if (passwordInput.value.length < 8) {
              warnings += 'La contraseña debe tener más de 8 caracteres <br>';
              entrar = true;
          }

          if (passwordInput.value !== confirmPasswordInput.value) {
              warnings += 'Las contraseñas no coinciden.<br>';
              entrar = true;
          }

          if (entrar) {
              warningsParagraph.innerHTML = warnings;
          } else {
              warningsParagraph.innerHTML = 'Formulario enviado.';
              loginForm.submit();  
          }
      });
  }
});



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
    speed: 600,
    loop: true,
    autoplay: {
      delay: 2000,
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
        slidesPerView: 1,
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
        slidesPerView: 1,
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