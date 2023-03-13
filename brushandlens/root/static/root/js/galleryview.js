$('#artist_button').on("click", function () {
    console.log('sadas');
});

$('#theme_button').on("click", function () {
    console.log('2eqwdwf');
});

function GalleryViewer(numRows, goatsPerRow) {
    const GOATS_PER_PAGE = numRows * goatsPerRow;

    this.updateCards = (goats) => {
        $('#cards').empty();

        for (let row = 0; row < numRows; row++) {
            const deck = $('<div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center"> </div>');

            for (let col = 0; col < goatsPerRow; col++) {
                const index = row * goatsPerRow + col;
                if (index < goats.length) {
                    const goat = goats[row * goatsPerRow + col];

                    const card = $(`
                        <div class="col mb-5">
                            <div class="card h-100">
                                <!-- Product image-->
                                <img class="card-img-top" src="/static/root/images/${goat.image}" alt="..." />
                                <!-- Product details-->
                                <div class="card-body p-4">
                                    <div class="text-center">
                                        <!-- Product name-->
                                        <h5 class="fw-bolder">Fancy Product</h5>
                                        <!-- Product price-->
                                        $40.00 - $80.00
                                    </div>
                                </div>
                                <!-- Product actions-->
                                <div id = "adopt-button" class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                    <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="#">View options</a></div>
                                </div>
                            </div>
                        </div>`);

                    $(card).find('.adopt-button').on('click', _ => {
                        this.adopt(goat);
                    });

                    $(deck).append(card);
                } else {

             

                }
            }

            $('#cards').append(deck);
        }
    }

    const createPageLink = (text, toPage, active, disabled) => {
        const link = $(`
            <li class="page-item">
                <a class="page-link">${text}</a>
            </li>
        `);
        $(link).find('.page-link').on('click', _ => {
            this.currentPage = toPage;
            this.load();
        });
        if (active)
            link.addClass('active');
        if (disabled)
            link.addClass('disabled');
        return link;
    }

    this.currentPage = 1;

    this.updatePagination = (total) => {
        let pages = Math.ceil(total / GOATS_PER_PAGE);
        $('#paginator').empty().append(
            createPageLink('Previous', this.currentPage - 1, false, this.currentPage == 1)
        );
        for (let page = 1; page <= pages; page++)
            $('#paginator').append(
                createPageLink(page, page, page == this.currentPage, false)
            );
        $('#paginator').append(
            createPageLink('Next', this.currentPage + 1, false, this.currentPage == pages)
        );
    }

    this.update = (data) => {
        this.updateCards(data.goats);
        this.updatePagination(data.total);
    }

    this.load = () => {
        $.get('/api/get_artists', {
            n: GOATS_PER_PAGE,
            offset: (this.currentPage - 1) * GOATS_PER_PAGE
        }, (data) => {
            this.update(data);
        });
    }

    this.adopt = (goat) => {
        $.post('/api/update_goat', {
            uid: goat.uid,
            adopted: (goat.adopted == 1 ? 0 : 1),
            n: GOATS_PER_PAGE,
            offset: (this.currentPage - 1) * GOATS_PER_PAGE
        }, (data) => {
            this.update(data);
        });
    }
}
