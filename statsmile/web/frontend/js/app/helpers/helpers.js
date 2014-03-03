Ember.Handlebars.helper('format-duration', function(date){
    return moment.unix(date).utc().format('H:m:s');
});