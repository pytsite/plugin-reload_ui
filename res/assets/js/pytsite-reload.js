define(['http-api'], function (httpApi) {
    return {
        reload: function () {
            return httpApi.post('reload');
        }
    }
});
