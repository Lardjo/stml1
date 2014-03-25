Ember.Handlebars.helper('date', function(date) {
    return moment(date['$date']).format('MMMM D, YYYY');
});

Ember.Handlebars.helper('date-full', function(date){
    return moment.unix(date).utc().format('MMM D, YYYY');
});

Ember.Handlebars.helper('parse_duration', function(date) {
    return moment.unix(date).utc().format('H:mm:ss');
});

Ember.Handlebars.helper('last-update', function(date) {
    return moment.utc(date['$date']).format('LLL');
});

Ember.Handlebars.helper('match', function(value) {
    return value + 1;
});

Ember.Handlebars.helper('badge-label', function(value) {
    if (value['badge'] == 1) {
        return new Handlebars.SafeString('<span class="label label-primary">Staff</span>');
    } else if (value['badge'] == 2) {
        return new Handlebars.SafeString('<span class="label label-info"><span class="glyphicon glyphicon-ok"></span> Verified</span>');
    } else {
        return 'Unknown';
    }
});