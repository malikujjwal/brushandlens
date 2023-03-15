window.onload = function () {
    let urlPath = window.location.pathname;
    if (urlPath.startsWith('/accounts')) {
        let button = document.getElementById('dropdownMenuButton1');
        button.classList.add('active');
    }
}