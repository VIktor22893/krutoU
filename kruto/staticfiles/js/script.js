$(function () {
    $('.acc_ctrl').on('click', function (e) {
        e.preventDefault();
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
            $(this).next()
                .stop()
                .slideUp(300);
        } else {
            $(this).addClass('active');
            $(this).next()
                .stop()
                .slideDown(300);
        }
    });
});


const burgerMenu = () => {
    const header = document.querySelector('.header.mobile .header__menu');
    header.classList.toggle('active');
}

const catalog_swiper = new Swiper('.swiper.catalog-swiper', {
    direction: 'horizontal',
    slidesPerView: 3,
    spaceBetween: 50,
    loop: true,

    navigation: {
        nextEl: '.catalog-swiper-button-next',
        prevEl: '.catalog-swiper-button-prev',
    },

    breakpoints: {
        320: {
            slidesPerView: 1
        },
        425: {
            slidesPerView: 1
        },
        540: {
            slidesPerView: 2
        },
        768: {
            slidesPerView: 2
        },
    }

});

const trust_swiper = new Swiper('.swiper.trust-swiper', {
    direction: 'horizontal',
    slidesPerView: 5,
    spaceBetween: 25,
    loop: true,

    navigation: {
        nextEl: '.trust-swiper-button-next',
        prevEl: '.trust-swiper-button-prev',
    },
    breakpoints: {
        320: {
            slidesPerView: 2
        },
        425: {
            slidesPerView: 2
        },
        540: {
            slidesPerView: 2
        },
        768: {
            slidesPerView: 3,
        },
        
    }
})


const about_swiper = new Swiper('.swiper.about-swiper', {
    direction: 'horizontal',
    slidesPerView: 5,
    spaceBetween: 25,
    loop: true,

    navigation: {
        nextEl: '.about-swiper-button-next',
        prevEl: '.about-swiper-button-prev',
    },
    breakpoints: {
        320: {
            slidesPerView: 2
        },
        425: {
            slidesPerView: 2
        },
        540: {
            slidesPerView: 2
        },
        768: {
            slidesPerView: 3,
        },
        
    }
})


document.addEventListener('DOMContentLoaded', function() {
    const changeElement = document.querySelector('.change');
    const words = changeElement.getAttribute('data-words').split('/');
    let wordIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function type() {
        const currentWord = words[wordIndex];
        const typeSpeed = isDeleting ? 50 : 50;
        const nextWordDelay = 2000; // Delay before starting to type the next word

        if (!isDeleting && charIndex < currentWord.length) {
            changeElement.textContent += currentWord.charAt(charIndex);
            charIndex++;
            setTimeout(type, typeSpeed);
        } else if (isDeleting && charIndex > 0) {
            changeElement.textContent = currentWord.substring(0, charIndex - 1);
            charIndex--;
            setTimeout(type, typeSpeed);
        } else if (!isDeleting && charIndex === currentWord.length) {
            isDeleting = true;
            setTimeout(type, nextWordDelay);
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            wordIndex = (wordIndex + 1) % words.length;
            setTimeout(type, 500);
        }
    }

    type();
});