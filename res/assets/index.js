const $ = require('jquery');
const httpApi = require('@pytsite/http-api');

$('#pytsite-reload-link').click(function (e) {
    e.preventDefault();

    const link = $(this);
    if (confirm(lang.t('reload_ui@confirm_application_reload'))) {
        reload.reload().done(function () {
            link.parent().text(lang.t('reload_ui@app_is_reloading'));
            setTimeout(function () {
                location.reload();
            }, 3000)
        });
    }
});

function reload() {
    return httpApi.post('reload');
}

export {reload}
