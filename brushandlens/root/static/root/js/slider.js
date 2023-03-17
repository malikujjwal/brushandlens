let icon = document.querySelector('ion-icon');
icon.onclick = function(){
  icon.classList.toggle('active');
}

// share button 
let shareButtons = document.querySelectorAll(".share-btn");
if (shareButtons) {
    [].forEach.call(shareButtons, function(button) {
    button.addEventListener("click", function(event) {
        var width = 650,
        height = 450;
        event.preventDefault();
        currentURL = window.location.href
        href = "https://www.addtoany.com/share_save?linkurl=" + currentURL.replaceAll("%", "/");
        console.log(href);
        window.open(href, 'Share Dialog', 'menubar=no,toolbar=no,resizable=yes,scrollbars=yes,width='+width+',height='+height+',top='+(screen.height/2-height/2)+',left='+(screen.width/2-width/2));
    });
    });
}

//create slides in slider
$(document).ready(function() {
    var price = [];
    $(".carousel-item input").each(function() {
        price.push($(this).val());
    });

    $("#carousel-inner-div img").click(function(){this.requestFullscreen()});

    var basePrice = price[$('.carousel-item.active').index()];
    var materialPrice = 0;
    var borderPrice = 0;
    var sizePrice = 0;

    function updatePrice(updatedPrice){
        $("#cartValue").val("Add to Cart   USD " + updatedPrice);
    }

    $('#carouselExampleCaptions').on('slid.bs.carousel', function () {
        var totalItems = $('.nav-img-item').length;
        var currentIndex = $('.carousel-item.active').index();
        console.log(price[currentIndex]);
        basePrice = price[currentIndex];
        console.log(totalItems);
        console.log(currentIndex);
        updatePrice(+sizePrice + +borderPrice + +basePrice + +materialPrice);
    })

    $('input[name=material]').change(function() {
        materialPrice = $('input[name=material]:checked').val();

        if (materialPrice == "10"){
            $('#carousel-inner-div img').addClass('carousel-frame');
            if (borderPrice == "5"){
                $('#carousel-inner-div img').removeClass('carousel-border');
                $('#carousel-inner-div img').addClass('carousel-border-wframe');
            }

        }
        else if (materialPrice == "0" && borderPrice == "5") {
            $('#carousel-inner-div img').removeClass('carousel-frame');
            $('#carousel-inner-div img').removeClass('carousel-border-wframe');
            $('#carousel-inner-div img').addClass('carousel-border');
        }
        else{
            $('#carousel-inner-div img').removeClass('carousel-frame');
        }

        updatePrice(+sizePrice + +borderPrice + +basePrice + +materialPrice);
    });

    $('input[name=size]').change(function() {
        sizePrice = $('input[name=size]:checked').val();
        updatePrice(+sizePrice + +borderPrice + +basePrice + +materialPrice);
    });

    $('input[name=border]').change(function() {
        borderPrice = $('input[name=border]:checked').val();
        if (borderPrice == "5" && materialPrice == "10"){
            $('#carousel-inner-div img').addClass('carousel-border-wframe');
        }
        else if (materialPrice == "0" && borderPrice == "5") {
            $('#carousel-inner-div img').removeClass('carousel-border-wframe');
            $('#carousel-inner-div img').addClass('carousel-border');
        }
        else{
            $('#carousel-inner-div img').removeClass('carousel-border-wframe');
            $('#carousel-inner-div img').removeClass('carousel-border');
        }
        updatePrice(+sizePrice + +borderPrice + +basePrice + +materialPrice);
    });

    $('#cartValue').click(function() {
        alert("Item added to cart!");
    });

});