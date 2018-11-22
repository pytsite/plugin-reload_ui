import $ from 'jquery';
import {lang} from '@pytsite/assetman';
import httpApi from '@pytsite/http-api';

$('#pytsite-reload-link').click(function (e) {
    e.preventDefault();

    const link = $(this);
    if (confirm(lang.t('reload_ui@confirm_application_reload'))) {
        reload.reload().then(() => {
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
