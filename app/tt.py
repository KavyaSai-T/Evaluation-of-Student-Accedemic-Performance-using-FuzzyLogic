
def stafflogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = SchoolUser.objects.filter(username=username,password=password,user_type='staff')
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("dashboard")
        else:
            messages.success(request, 'Invalid Username or Password')
    return render(request, 'stafflogin.html', {})

def studentlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        post = SchoolUser.objects.filter(username=username,password=password,user_type='student')
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("dashboard")
        else:
            messages.success(request, 'Invalid Username or Password')
    return render(request, 'studentlogin.html', {})
def export_users_xls(request):
    if request.method == 'GET':
        class_id = request.GET.get('cls_id')
        section_id = request.GET.get('sec_id')
        a = int(class_id)
        b = int(section_id)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="marks.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Mark')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Student Register Number',]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        rows = Subject.objects.filter(class_id=a,section_id=b).values_list('subject_name').order_by('subject_id')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(col_num, row_num,  row[col_num] + " " 'Mark', font_style)

        wb.save(response)
        return response