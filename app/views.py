# Create your views here.
from django.contrib import auth
from django.template.defaulttags import url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app.models import resources
from django.db import connection


def auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(url('home'))
    else:
        return HttpResponseRedirect(url('invalid'))


def home(request):
    return render(request, 'app/home.html', {
    })


def ssl_create(request):
    return render(request, 'app/ssl_create.html', {
    })

def url_access(request):
    current_url = None
    pre_url = request.GET.get('ParentURL')
    if request.GET.get('URL'):
        current_url = request.GET.get('URL')
    if not current_url:
        return render(request, 'app/url_access.html', {})
    domain_list = resources.objects.raw("select Domain,count(*) as ID from resources where ParentURL = %s and Domain <> '' GROUP BY Domain",[current_url])
    internal_link_list = resources.objects.raw("select ID,URL from resources where ParentURL = %s and Type = 'internal' and ResourceType = 'link'",[current_url])
    internal_resource = resources.objects.raw("select ID,URL,ParentURL,ResourceType,Domain,Type,IsHttps from resources where Type = 'internal' and ParentURL = %s and ResourceType <> 'link'",[current_url])
    path_list = set()
    path_map = {}
    for ir in internal_resource:
        path_map[ir.URL] = ir.URL[:ir.URL.rindex('/')]
        path_list.add(ir.URL[:ir.URL.rindex('/')])
    internal_resource_list = []
    for path in path_list:
        temp_num = 0
        temp_map = {}
        temp_list = []
        for ir in path_map:
            if path_map[ir] == path:
                temp_list.append(ir)
                temp_num += 1
        temp_map['name'] = path
        temp_map['count'] = temp_num
        temp_map['list'] = temp_list
        internal_resource_list.append(temp_map)
    external_resource = resources.objects.raw("select ID,URL,ParentURL,ResourceType,Domain,Type,IsHttps from resources where Type = 'external' and ParentURL = %s and ResourceType <> 'link'",[current_url])
    path_list_ex = set()
    path_map_ex = {}
    for ir in external_resource:
        path_map_ex[ir.URL] = ir.URL[:ir.URL.rindex('/')]
        path_list_ex.add(ir.URL[:ir.URL.rindex('/')])
    external_resource_list = []
    for path in path_list_ex:
        temp_num = 0
        temp_map = {}
        temp_list = []
        for ir in path_map_ex:
            if path_map_ex[ir] == path:
                temp_list.append(ir)
                temp_num += 1
        temp_map['name'] = path
        temp_map['count'] = temp_num
        temp_map['list'] = temp_list
        external_resource_list.append(temp_map)
    cursor = connection.cursor()
    cursor.execute(
        "select count(*) from resources where ParentURL = %s and Type = 'internal'",
        [current_url])
    internal_resource_count = cursor.fetchone()[0]
    cursor.execute(
        "select count(*) from resources where ParentURL = %s and Type = 'external'",
        [current_url])
    external_resource_count = cursor.fetchone()[0]
    cursor.execute(
        "select count(*) from resources where ParentURL = %s and IsHttps='1'",
        [current_url])
    external_https_count = cursor.fetchone()[0]
    cursor.close()
    return render(request, 'app/url_access.html', {'internal_resource_list': internal_resource_list, 'external_resource_list': external_resource_list,
                                                   'internal_resource_count': internal_resource_count, 'external_resource_count':external_resource_count,
                                                   'external_https_count': external_https_count, 'domain_list': domain_list, 'internal_link_list':internal_link_list,
                                                   'current_url': current_url,'pre_url': pre_url
    })

def url_list(request):
    query_sql = "select ID,URL,ParentURL,ResourceType,Domain,Type,IsHttps from resources where 1=1 "
    if request.GET.get('Type'):
        query_sql += 'and Type = "' + request.GET.get('Type')+'" '
    if request.GET.get('URL'):
        if request.GET.get('LikeOrEq') == 'eq':
            query_sql += 'and URL = "' + request.GET.get('URL')+'" '
        else :
            query_sql += 'and URL like "' + request.GET.get('URL')+'%%" '
        # query_sql += 'and URL like %s '
    if request.GET.get('ParentURL'):
        query_sql += 'and ParentURL = "' + request.GET.get('ParentURL')+'" '
    if request.GET.get('ResourceType'):
        query_sql += 'and ResourceType = "' + request.GET.get('ResourceType')+'" '
    if request.GET.get('Domain'):
        query_sql += 'and Domain = "' + request.GET.get('Domain')+'" '
    if request.GET.get('IsHttps'):
        query_sql += 'and IsHttps = "' + request.GET.get('IsHttps')+'" '
    print(query_sql)
    resource = resources.objects.raw(query_sql)
    total_resource = 0
    for res in resource:
        total_resource += 1
    return render(request, 'app/url_list.html', {'resource': resource, 'total_resource':total_resource
    })

def https_show(request):
    cursor = connection.cursor()
    cursor.execute("select count(*) from (select DISTINCT Domain from resources where Type = 'external') temp_res")
    exter_domain_count = cursor.fetchone()[0]
    cursor.execute("select count(*) from resources where Type = 'internal' and ResourceType = 'link'")
    internal_link_count = cursor.fetchone()[0]
    cursor.execute("select count(*) from resources where Type = 'internal' and ResourceType <> 'link'")
    internal_resource_count = cursor.fetchone()[0]
    cursor.execute("select count(*) from resources where Type = 'external' and ResourceType = 'link'")
    external_link_count = cursor.fetchone()[0]
    cursor.execute("select count(*) from resources where Type = 'external' and ResourceType <> 'link'")
    external_resource_count = cursor.fetchone()[0]
    cursor.execute("select count(*) from resources where IsHttps = '1'")
    external_https_count = cursor.fetchone()[0]
    cursor.close()
    return render(request, 'app/https_show.html', {'exter_domain_count':exter_domain_count,'internal_link_count':internal_link_count,
                                                   'internal_resource_count':internal_resource_count, 'external_link_count':external_link_count,
                                                   'external_resource_count':external_resource_count, 'external_https_count':external_https_count
    })

def https_detail(request):
    cursor = connection.cursor()
    query_sql = "select ID,URL,ParentURL,ResourceType,Domain,Type,IsHttps from resources where 1=1 "
    if request.GET.get('Type'):
        query_sql += 'and Type = ' + request.GET.get('Type')
    if request.GET.get('ResourceType'):
        query_sql += 'and ResourceType = ' + request.GET.get('ResourceType')
    if request.GET.get('Domain'):
        query_sql += 'and Domain = "' + request.GET.get('Domain')+'"'
    if request.GET.get('IsHttps'):
        query_sql += 'and IsHttps = ' + request.GET.get('IsHttps')
    print(query_sql)
    Resource = resources.objects.raw(query_sql)
    cursor.execute("select count(*) from resources where Type = 'internal' and ResourceType = 'link' and Domain = %s",
                   [request.GET.get('Domain')])
    internal_link_count = cursor.fetchone()[0]
    cursor.close()
    cursor = connection.cursor()
    cursor.execute("select count(*) from resources where Type = 'internal' and ResourceType <> 'link' and Domain = %s",
                   [request.GET.get('Domain')])
    internal_resource_count = cursor.fetchone()[0]
    cursor.close()
    cursor = connection.cursor()
    cursor.execute(
        "select count(*) from resources where Type = 'external' and ResourceType = 'link' and Domain = %s",
        [request.GET.get('Domain')])
    external_link_count = cursor.fetchone()[0]
    cursor.close()
    cursor = connection.cursor()
    cursor.execute(
        "select count(*) from resources where Type = 'external' and ResourceType <> 'link' and Domain = %s",
        [request.GET.get('Domain')])
    external_resource_count = cursor.fetchone()[0]
    cursor.close()
    cursor = connection.cursor()
    cursor.execute(
        "select count(*) from resources where IsHttps = '1' and Domain = %s",
        [request.GET.get('Domain')])
    external_https_count = cursor.fetchone()[0]
    cursor.close()
    return render(request, 'app/https_detail.html', {'Resource': Resource, 'internal_link_count': internal_link_count, 'external_link_count': external_link_count,
    'internal_resource_count': internal_resource_count,
    'external_resource_count': external_resource_count,
    'external_https_count':external_https_count,'domainName':request.GET.get('Domain')
    })


def ssl_create_file(request):
    return render(request, 'app/ssl_create_file.html', {
    })


def ssl_create_dns(request):
    return render(request, 'app/ssl_create_dns.html', {
    })


@login_required
def need_login(request):
    return HttpResponse('OK')


def test(request):
    return render(request, 'app/test.html', {
        'title': 'Test Page',
        'description': 'Test Page for some demo.',
    })
