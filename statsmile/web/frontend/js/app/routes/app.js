App.ApplicationRoute = Ember.Route.extend({
    model: function () {
        $.getJSON('/auth').then(function (response) {
            return {user: response.user};
        })
    }
});