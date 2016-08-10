// load EFFECTIVE_TLD_NAMES_JSON
$.getJSON(SETTINGS.EFFECTIVE_TLD_NAMES_JSON_URL, function (data) {
    SETTINGS.EFFECTIVE_TLD_NAMES_JSON = data;
});

$('#ssl_create').submit(function () {
    var domains_list = SETTINGS.EFFECTIVE_TLD_NAMES_JSON;
    // todo multi domain check and not same top domain validate
    var domains_input = $(this).find('input[name="domains"]');
    var a = document.createElement('a');
    a.href = 'https://' + domains_input.val();
    var domain = a.hostname;
    var domain_suffix = get_domain_suffix(domain);
    while (domain_suffix) {
        if (domains_list.indexOf(domain_suffix) != -1) break;
        domain_suffix = get_domain_suffix(domain_suffix);
    }
    if (!domain_suffix) {
        toast_error('no such domains suffix of ' + domain);
        return false;
    }
    var domain_name = domain.substr(0, domain.length - domain_suffix.length - 1);

    if (domain_name.indexOf('.') == -1) domains_input.val(domain + ',' + 'www.' + domain)
});

function get_domain_suffix(domains) {
    var index = domains.indexOf('.');
    if (index == -1) return '';
    return domains.substr(index + 1);
}

function toast_error(msg) {
    //todo pretty toast error ui
    alert(msg);
}
