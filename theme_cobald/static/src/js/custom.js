$(document).on('click', '#header_show_menu', function(){
    $('#oe_main_menu_navbar').hide();
});

$(document).on('click', '#close_model', function(){
    $('#oe_main_menu_navbar').show();
});

document.querySelectorAll(".carousel_merken .carousel").forEach((carousel) => {
  // **********************************************
  // INITIALISATIONS
  // **********************************************
  // Nombre de slides
  const itemsCount = carousel.querySelectorAll(".carousel-item").length;

  // **********************************************
  // AJOUT DES ELEMENTS DE NAVIGATION
  // **********************************************

  // Ajout de la navigation
  if (!carousel.classList.contains("carousel-no-navigation")) {
    addNavigation();
  }

  function addNavigation() {
    const navigation = document.createElement("div");
    navigation.setAttribute("class", "carousel-navigation");

    for (let i = 0; i < itemsCount; i++) {
      const btn = document.createElement("a");
      btn.setAttribute("href", "#");
      btn.setAttribute("class", "carousel-navigation-btn");
      navigation.append(btn);
      btn.onclick = function (e) {
        e.preventDefault();
        showSlide(i);
      };
    }

    carousel.append(navigation);
  }

  // Ajout des Flèches
  if (!carousel.classList.contains("carousel-no-arrows")) {
    addArrows();
  }

  function addArrows() {
    const arrowLeft = document.createElement("a");
    arrowLeft.setAttribute("class", "carousel-arrow carousel-arrow-left");
    arrowLeft.innerText = "❮";
    carousel.append(arrowLeft);
    arrowLeft.onclick = function (e) {
      e.preventDefault();
      showSlide(activeItem - 1);
    };

    const arrowRight = document.createElement("a");
    arrowRight.setAttribute("class", "carousel-arrow carousel-arrow-right");
    arrowRight.innerText = "❯";
    carousel.append(arrowRight);
    arrowRight.onclick = function (e) {
      e.preventDefault();
      showSlide(activeItem + 1);
    };
  }

  // **********************************************
  // DEPLACEMENT DES SLIDES
  // **********************************************

  let previousItem, activeItem, nextItem;
  showSlide(1);

  function showSlide(index) {
    if (index >= itemsCount) {
      activeItem = 0;
    } else if (index < 0) {
      activeItem = itemsCount - 1;
    } else {
      activeItem = index;
    }
    nextItem = activeItem + 1 >= itemsCount ? 0 : activeItem + 1;
    previousItem = activeItem - 1 < 0 ? itemsCount - 1 : activeItem - 1;
    removeClasses();
    addClasses();
  }

  function removeClasses() {
    carousel.querySelectorAll(".carousel-item").forEach((slide) => {
      slide.classList.remove("previous", "active", "next");
    });
    carousel.querySelectorAll(".carousel-navigation-btn").forEach((btn) => {
      btn.classList.remove("active");
    });
  }

  function addClasses() {
    carousel.querySelectorAll(".carousel-item")[activeItem].classList.add("active");
    carousel.querySelectorAll(".carousel-item")[previousItem].classList.add("previous");
    carousel.querySelectorAll(".carousel-item")[nextItem].classList.add("next");
    carousel.querySelectorAll(".carousel-navigation-btn")[activeItem].classList.add("active");
  }
});