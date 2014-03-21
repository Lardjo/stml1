App.ApplicationRoute = Ember.Route.extend({

    model: function () {
        return $.getJSON('/auth').then(function (response) {
            return {user: response.user};
        })
    }
});