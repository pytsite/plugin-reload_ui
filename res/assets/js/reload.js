require(['jquery', 'pytsite-reload', 'lang'], function ($, reload, lang) {
    $('#pytsite-reload-link').click(function (e) {
        e.preventDefault();

        var link = $(this);
        if (confirm(lang.t('plugins.reload_ui@confirm_application_reload'))) {
            reload.reload().done(function () {
                link.parent().text(lang.t('plugins.reload_ui@app_is_reloading'));
                setTimeout(function () {
                    location.reload();
                }, 3000)
            });
        }
    });
});
