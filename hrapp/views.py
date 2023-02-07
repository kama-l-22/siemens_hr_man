from .models import *
from django.core.exceptions import *
from django.shortcuts import render,redirect
from django.db.models import Q

# Create your views here.

try : 

 def login(request): #login fucntion function to check the user.....

    if 'loginsubmit' in request.POST:

        print('login')
        empcode = request.POST.get('empcode')
        pword = request.POST.get('pword')

        a = employee.objects.filter(Emp_code=empcode)
        b = manager.objects.filter(Emp_code=empcode)
        c = hr.objects.filter(Emp_code=empcode)
        d = qdmin.objects.filter(Emp_code=empcode)

        print(a,b,c,d)

        if str(a) != '<QuerySet []>': #checking in employee
            for i in a:
                print('emp')
                empid = i.id
                request.session['empid'] = empid
                if i.password == pword:
                    return redirect('emp')
                else:
                    return render(request,'login.html',{'error':"password doesn't match"})
                
        elif str(b) != '<QuerySet []>':  #checking in manager
            for i in b:
                print('manager')
                manid = i.id
                request.session['manid'] = manid
                
                if i.password == pword:
                    return redirect('man')
                else:
                    return render(request,'login.html',{'error':"password doesn't match"})
                
        elif str(c) != '<QuerySet []>': #checking in hr
            for i in c:
                print('hr')
                hrid = i.id
                request.session['hrid'] = hrid
                if i.password == pword:
                    return redirect('hr_f')
                else:
                    return render(request,'login.html',{'error':"password doesn't match"})
                
                
        elif str(d) != '<QuerySet []>': #checking in admin
            for i in d:
                print('admin')
                admid = i.id
                request.session['admid'] = admid
                
                if i.password == pword:
                    return redirect('adminn')
                else:
                    return render(request,'login.html',{'error':"password doesn't match"})
                
                
        else: # no user found
            print('no user found..')
            return render(request,'login.html',{'error':'no user found'})

    return render(request,'login.html')


 def home(request): #home page which has no use.. now
    return render(request,'home.html')











 def man(request): #working on the manager functions.. .. ... 
    manid = request.session['manid']
    print(manid)
    user = manager.objects.get(id = manid)
    print(user)


    if 'getre' in request.POST: #getreport
        print('get report')
        kocha = report.objects.all()
        return render(request,'home.html',{ 'role':'man','object':user,'function':'gtr','kocha':kocha})

    elif 'evemp' in request.POST: #scoring Employee
        print('scoring employee')
        empo = employee.objects.all()
        return render(request,'home.html',{ 'role':'man','object':user,'function':'escore','empo':empo})

    elif 'ess' in request.POST: # submiting the score
        empo = employee.objects.all()
        print('ep score change is on process')
        emid = request.POST.get('eempid')
        scro = request.POST.get('es')
        loko = employee.objects.get(Emp_code = emid)
        print(loko)
        loko.employee_score = scro
        loko.save()
        return render(request,'home.html',{ 'role':'man','object':user,'function':'escore','empo':empo,'message':'employee grade has been changed'})

    elif 'editper' in request.POST: #editing the personal data
        print('edit personal data')
        return render(request,'home.html',{ 'role':'man','object':user,'function':'eper'})

    elif 'eman' in request.POST: #submiting the personaldata
        emcode = request.POST.get('emcode')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pht = request.POST.get('pht')
        jdt = request.POST.get('jdt')
        phn = request.POST.get('phn')
        print(emcode,fname,lname,email,pht,jdt,phn)
        user.first_name = fname
        user.last_name =lname
        user.email = email

        user.phone = phn
        user.save()
        return render(request,'home.html',{ 'role':'man','object':user,'function':'eper','message':'changes are saved'})

    elif 'cemp' in request.POST: #chaging the project of employee
        emp_o = employee.objects.all()
        print('changing the employee project')
        return render(request,'home.html',{ 'role':'man','object':user,'function':'cempr','emp_o':emp_o})

    elif 'cwps' in request.POST: #submiting the chnage for the submit in employe project
        emp_o = employee.objects.all()
        cheid = request.POST.get('chemid')
        print(cheid)
        cwpc = request.POST.get('cwpc')
        print(cwpc)
        joko = employee.objects.get(Emp_code = cheid)
        print(joko)
        joko.c_w_p = cwpc
        joko.save()
        return render(request,'home.html',{ 'role':'man','object':user,'function':'cempr','emp_o':emp_o,'message':"employee's current working project has been changed."})

    elif 'manview' in request.POST: #view page for manager
        print('view')
        allo = employee.objects.all()
        return render(request,'home.html',{ 'role':'man','object':user,'function':'mview','allo':allo})

    elif 'searchm' in request.POST: #the using of search function in the manager page..
        print('view')
        sear = request.POST.get('semo')
        allo = employee.objects.filter(Q(first_name__startswith = sear)| Q(Emp_code__contains = sear))
        return render(request,'home.html',{ 'role':'man','object':user,'function':'mview','allo':allo})

    elif 'logout' in request.POST: #for logout from manager
        return redirect('login')
    else:
        print('view')
        allo = employee.objects.all()
        return render(request,'home.html',{ 'role':'man','object':user,'function':'mview','allo':allo})

    return render(request,'home.html',{ 'role':'man','object':user})














 def hr_f(request):
    hrid = request.session['hrid']
    print(hrid)
    user = hr.objects.get(id = hrid)
    print(user)
    if 'gleave' in request.POST:
        print('give leave')
        leok = requestleave.objects.all()
        return render(request,'home.html',{'role':'hr','object':user,'function':'leave','leok':leok})
    elif 'chuchu' in request.POST:
        leok = requestleave.objects.all()
        eidl = request.POST.get('eidl')
        rfl = request.POST.get('rfl')
        dtl= request.POST.get('dtl')
        apby = request.POST.get('apby')
        print(eidl,rfl,dtl,apby)
        crl = approvedleave.objects.create(
            empidforleave = eidl,
            dateofleave = str(dtl),
            reasonofleave = rfl,
            approved_by = apby
        )
        crl.save()

        deko = requestleave.objects.get(empidforleave = eidl)
        deko.delete()
        return render(request,'home.html',{'role':'hr','object':user,'function':'leave','leok':leok})
    elif 'chucha' in request.POST:
        print('deapptoving the leave')
        leok = requestleave.objects.all()
        eidl = request.POST.get('eidl')
        rfl = request.POST.get('rfl')
        dtl= request.POST.get('dtl')
        apby = request.POST.get('apby')
        print(eidl,rfl,dtl,apby)

        deko = requestleave.objects.get(empidforleave = eidl)
        deko.delete()
        return render(request,'home.html',{'role':'hr','object':user,'function':'leave','leok':leok})
    elif 'adem' in request.POST:
        print('adding a new employee')
        mano = manager.objects.all()
        return render(request,'home.html',{'role':'hr','object':user,'function':'adde','mano':mano})

    elif 'subforadde' in request.POST:
        print('adding new employee data submit')
        Emp_code_ = request.POST.get('Emp_code')
        first_name_ = request.POST.get('first_name')
        last_name_ = request.POST.get('last_name')
        password_ = request.POST.get('password')
        email_ = request.POST.get('email')
        photo_ = request.POST.get('photo')
        employee_score_ = request.POST.get('employee_score')
        joined_date_ = request.POST.get('joined_date')
        phone_ = request.POST.get('phone')
        address_ = request.POST.get('address')
        skills_ = request.POST.get('skills')
        c_w_p_ = request.POST.get('c_w_p')
        man_ager_ = request.POST.get('m_under')
        request_by_ = request.POST.get('request_by')
        print(Emp_code_,first_name_,last_name_,password_,email_,photo_,employee_score_,
        joined_date_,phone_,address_,skills_,c_w_p_,man_ager_,request_by_)


        sho = employee.objects.filter(Emp_code = Emp_code_)
        print(sho)
        man_ager_ob = manager.objects.get(Emp_code = man_ager_)
        if str(sho) == '<QuerySet []>':
            savo = request_employee.objects.create(
            Emp_code = Emp_code_,
            first_name =first_name_,
            last_name = last_name_,
            password =password_,
            email = email_,
            photo = photo_,
            employee_score = employee_score_,
            joined_date = joined_date_,
            phone = phone_,
            address = address_,
            skills = skills_,
            c_w_p = c_w_p_,
            manager = man_ager_ob,
            request_by = request_by_
        )

            savo.save()
        
        else:
            print('user exits')
    elif 'viewhr' in request.POST:
        print('hr view function is called')
        emlo = employee.objects.all()
        return render(request,'home.html',{ 'role':'hr','object':user,'function':'hrview','allo':emlo})
    elif 'searchhr'in request.POST:
        sear = request.POST.get('semo')
        allo = employee.objects.filter(Q(first_name__startswith = sear)| Q(Emp_code__contains = sear))
        return render(request,'home.html',{ 'role':'hr','object':user,'function':'hrview','allo':allo})
    elif 'editemhr' in request.POST:
       
        Emp_code__ = request.POST.get('Emp_code')
        first_name__ = request.POST.get('first_name')
        last_name__ = request.POST.get('last_name')
        email__ = request.POST.get('email')
        joined_date__ = request.POST.get('joined_date')
        phone__ = request.POST.get('phone')
        address__ = request.POST.get('address')
        skills__ = request.POST.get('skills')
        c_w_p__ = request.POST.get('c_w_p')
        print(Emp_code__,first_name__,last_name__,email__,
        joined_date__,phone__,address__,skills__,c_w_p__)
        allo = employee.objects.filter(Emp_code =  Emp_code__)
        editko = employee.objects.get(Emp_code = Emp_code__)
        editko.first_name = first_name__
        editko.last_name = last_name__
        editko.email = email__
        editko.phone = phone__
        editko.address = address__
        editko.skills = skills__
        editko.save()

        return render(request,'home.html',{ 'role':'hr','object':user,'function':'hrview','allo':allo})

    elif 'logout' in request.POST: #for logout from manager
        return redirect('login')
    else:
        print('give leave')
        leok = requestleave.objects.all()
        return render(request,'home.html',{'role':'hr','object':user,'function':'leave','leok':leok})

    return render(request,'home.html',{'role':'hr','object':user})

    










 def emp(request):
    empid = request.session['empid']
    print(empid)
    user = employee.objects.get(id = empid)
    print(user)


    if 'ask_leave' in request.POST:
        print('akleave')
        return render(request,'home.html',{'role':'emp','object':user,'function':'askleave'})

    elif 'leavesubmit' in request.POST:
        empidfor_leave = request.POST.get('empid')
        dateof_leave = request.POST.get('date')
        reasonof_leave = request.POST.get('reason')
        in_person_charge = request.POST.get('inper')
        print(empidfor_leave,dateof_leave,reasonof_leave,in_person_charge)

        leave = requestleave.objects.create(
            empidforleave =empidfor_leave,
            dateofleave = dateof_leave,
            reasonofleave = reasonof_leave,
            inperson_charge = in_person_charge,
        )
        leave.save()

        return render(request,'home.html',{'role':'emp','object':user,'function':'askleave','message':'leave request has sent'})

        
    elif 'subre' in request.POST:
        print('subre')
        return render(request,'home.html',{'role':'emp','object':user,'function':'submit_report'})

    elif 'reportsub' in request.POST:
        print('geting the report and saving')
        
        if 'reportsub' in request.POST:
            eid_sub = request.POST.get("empid")
            sub_date = request.POST.get("date")
            subfile = request.POST.get("file")
            complition =request.POST.get("comstatus")
            proname =request.POST.get("pname")
            print(eid_sub,sub_date,subfile,complition,proname)
            submit = report.objects.create(
                empid_for_report =eid_sub,
                doucment_overview =subfile,
                submit_date =sub_date,
                compliction_status =complition,
                project_name =proname,
            )
            return render(request,'home.html',{'role':'emp','object':user,'function':'submit_report','message':'report has been sent to manager'})
        return render(request,'home.html',{'role':'emp','object':user,'function':'submit_report'})



    elif 'edit' in request.POST:
        print('edit')
        return render(request,'home.html',{'role':'emp','object':user,'function':'edit_personal'})

    elif 'epd' in request.POST:
        print('editing started...')
        empcode = request.POST.get('empcode')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email= request.POST.get('email')
        img = request.POST.get('img')
        phn = request.POST.get('phn')
        adrs = request.POST.get('adrs')
        skills = request.POST.get('skills')
        print(empcode,fname,lname,email,img,phn,adrs,skills)
        
        edit = employee.objects.get(Emp_code = empcode)
        print('okokok',edit)
        edit.first_name = fname
        edit.last_name = lname
        edit.email = email
        edit.photo = img
        edit.address = adrs
        edit.skills = skills
        edit.phone = phn
        edit.save()
        print('saved')
        return render(request,'home.html',{'role':'emp','object':user,'function':'edit_personal','message':'changes are saved'})


    elif 'viwescr' in request.POST:
        print('viwe scrore')
        return render(request,'home.html',{'role':'emp','object':user,'function':'view_score'})
    elif 'logout' in request.POST: 
        return redirect('login')
    else:
        print('akleave')
        return render(request,'home.html',{'role':'emp','object':user,'function':'askleave'})

    return render(request,'home.html', {'role':'emp','object':user})
    

 def adminn(request):
    admid = request.session['admid']
    print(admid)
    user = qdmin.objects.get(id = admid)
    print(user)
    if 'viewall' in request.POST:
        print('workin on view all admin')
        vemp = employee.objects.all()
        vhr = hr.objects.all()
        vman = manager.objects.all()
        return render(request,'home.html', {'role':'admin','object':user,'function' :'viewall','e':vemp,'m':vman,'h':vhr})
    elif 'searchvi' in request.POST:
        print('searching in admin page')
        sear = request.POST.get('searchina')
        vemp = employee.objects.filter(Q(first_name__startswith = sear)| Q(Emp_code__contains = sear))
        vhr = hr.objects.filter(Q(first_name__startswith = sear)| Q(Emp_code__contains = sear))
        vman = manager.objects.filter(Q(first_name__startswith = sear)| Q(Emp_code__contains = sear))
        nai = []
        for i in vemp:
            nai.append(i)
        for i in vhr:
            nai.append(i)
        for i in vman:
            nai.append(i)

            
        print(nai)
        return render(request,'home.html', {'role':'admin','object':user,'function' :'viewall','heo':nai})
    
    elif 'editrole' in request.POST:
        emo = request.POST.get('no')

        a = employee.objects.filter(Emp_code=emo)
        b = manager.objects.filter(Emp_code=emo)
        c = hr.objects.filter(Emp_code=emo)

        print(a,b,c,)
        

        if str(a) != '<QuerySet []>': #checking in employee
            for i in a:
                Emp_code_  = request.POST.get('no')
                first_name_ = request.POST.get('nfn')
                last_name_ = request.POST.get('nln')
                email_  = request.POST.get('ne')
                phone_ = request.POST.get('np')
                #print(Emp_code_,first_name,last_name,email,phone)
                emoo = employee.objects.get(Emp_code = Emp_code_)
                emoo.first_name = first_name_
                emoo.last_name = last_name_
                emoo.email = email_
                emoo.phone = phone_
                emoo.save()
                return redirect('adminn')
        elif str(b) != '<QuerySet []>':  #checking in manager
            for i in b:
                print('manager')
                Emp_code_  = request.POST.get('no')
                first_name_ = request.POST.get('nfn')
                last_name_ = request.POST.get('nln')
                email_  = request.POST.get('ne')
                phone_ = request.POST.get('np')
                #print(Emp_code_,first_name,last_name,email,phone)
                emoo = manager.objects.get(Emp_code = Emp_code_)
                emoo.first_name = first_name_
                emoo.last_name = last_name_
                emoo.email = email_
                emoo.phone = phone_
                emoo.save()
                return redirect('adminn')
        elif str(c) != '<QuerySet []>': #checking in hr
            for i in c:
                print('hr')
                Emp_code_  = request.POST.get('no')
                first_name_ = request.POST.get('nfn')
                last_name_ = request.POST.get('nln')
                email_  = request.POST.get('ne')
                phone_ = request.POST.get('np')
                #print(Emp_code_,first_name,last_name,email,phone)
                emoo = hr.objects.get(Emp_code = Emp_code_)
                emoo.first_name = first_name_
                emoo.last_name = last_name_
                emoo.email = email_
                emoo.phone = phone_
                emoo.save()
                return redirect('adminn')
        
    elif 'addemp' in request.POST:
        print('addemp')
        iop = manager.objects.all()
        return render(request,'home.html', {'role':'admin','object':user,'function':'addemp','iop':iop})

    elif 'addemo' in request.POST:
        print('adding new employee')
        iop = manager.objects.all()
        aEmp_code  = request.POST.get('Emp_code')
        afirst_name = request.POST.get('first_name')
        alast_name = request.POST.get('last_name')
        apassword = request.POST.get('password')
        aemail = request.POST.get('email')
        aphoto  = request.POST.get('photo')
        aemployee_score = request.POST.get('employee_score')
        ajoined_date  = request.POST.get('joined_date')
        aphone  = request.POST.get('phone')
        aaddress = request.POST.get('address')
        askills = request.POST.get('skills')
        ac_w_p = request.POST.get('c_w_p')
        manid = request.POST.get('manager')
        yui = manager.objects.get(id = manid)
        ayu = [aEmp_code,afirst_name,alast_name,apassword,aemail,aphoto,
        aemployee_score,ajoined_date,aphone,aaddress,askills,ac_w_p]
        print(ayu)

     
        hut = employee.objects.filter(Emp_code = aEmp_code)
        print(hut)
        if str(hut) == '<QuerySet []>':
            sd = employee.objects.create(
            Emp_code = aEmp_code,
            first_name =afirst_name,
            last_name = alast_name,
            password = apassword,
            email = aemail,
            employee_score = aemployee_score,
            joined_date  = ajoined_date,
            phone  = aphone,
            address = aaddress,
            skills = askills,
            c_w_p = ac_w_p,
            manager = yui
            )
            sd.save()
        else: 
            print('userexits')
        return render(request,'home.html', {'role':'admin','object':user,'function':'addemp','iop':iop})
    elif 'addhr' in request.POST:
        print('addhr')
        return render(request,'home.html', {'role':'admin','object':user,'function':'addhr'})
    elif 'addhro' in request.POST:
        print('adding the hr.. ')
   
        hEmp_code  = request.POST.get('Emp_codeh')
        hfirst_name = request.POST.get('first_nameh')
        hlast_name = request.POST.get('last_nameh')
        hpassword = request.POST.get('passwordh')
        hemail = request.POST.get('emailh')
        hjoined_date  = request.POST.get('joined_dateh')
        hphone  = request.POST.get('phoneh')
        

     
        hut = hr.objects.filter(Emp_code = hEmp_code)
        print(hut)
        if str(hut) == '<QuerySet []>':
            sd = hr.objects.create(
            Emp_code = hEmp_code,
            first_name =hfirst_name,
            last_name = hlast_name,
            password = hpassword,
            email = hemail,
            joined_date  = hjoined_date,
            phone  = hphone,
        )
            sd.save()
        else: 
            print('userexits')
        return render(request,'home.html', {'role':'admin','object':user,'function':'addhr'})

    elif 'addman' in request.POST:
        print('addman')
        return render(request,'home.html', {'role':'admin','object':user,'function':'addman'})

    elif 'addmano' in request.POST:
        print('adding the man.. ')
   
        hEmp_code  = request.POST.get('Emp_codeh')
        hfirst_name = request.POST.get('first_nameh')
        hlast_name = request.POST.get('last_nameh')
        hpassword = request.POST.get('passwordh')
        hemail = request.POST.get('emailh')
        hjoined_date  = request.POST.get('joined_dateh')
        hphone  = request.POST.get('phoneh')
        

     
        hut = manager.objects.filter(Emp_code = hEmp_code)
        print(hut)
        if str(hut) == '<QuerySet []>':
            sd = manager.objects.create(
            Emp_code = hEmp_code,
            first_name =hfirst_name,
            last_name = hlast_name,
            password = hpassword,
            email = hemail,
            joined_date  = hjoined_date,
            phone  = hphone,
        )
            sd.save()
        else: 
            print('userexits')
    
        return render(request,'home.html', {'role':'admin','object':user,'function':'addhr'})
    
    elif 'nreq' in request.POST:
        print('new user requests')
        monu = manager.objects.all()
        puo = request_employee.objects.all()
        uuo = req_hr.objects.all()
        guo = req_man.objects.all()

        return render(request,'home.html',{'role':'admin','object':user,'function': 'nreqo','puo':puo,'monu':monu,'uuo':uuo,'guo':guo})
    elif 'apreq' in request.POST:
        print('approving the employee request')

        rEmp_code = request.POST.get('Emp_code')
        rfirst_name =  request.POST.get('first_name')
        rlast_name = request.POST.get('last_name')
        rpassword = request.POST.get('password')
        remail = request.POST.get('email')
        remployee_score = request.POST.get('employee_score')
        rjoined_date = request.POST.get('joined_date')
        rphone = request.POST.get('phone')
        raddress = request.POST.get('address')
        rskills = request.POST.get('skills')
        rc_w_p = request.POST.get('c_w_p')
        rmanager = request.POST.get('manager')
        pochi = manager.objects.get(id = rmanager)

        poda = employee.objects.create(
            Emp_code = rEmp_code,
            first_name = rfirst_name,
            last_name = rlast_name,
            password = rpassword,
            email = remail,
            employee_score = remployee_score,
            joined_date = rjoined_date,
            phone = rphone,
            address = raddress,
            skills = rskills,
            c_w_p = rc_w_p,
            manager = pochi
        )
        poda.save()

        koi = request_employee.objects.get(Emp_code = rEmp_code)
        print(koi)
        koi.delete()


    elif 'raddhr' in request.POST:
        print('approving the hr')
        rEmp_code = request.POST.get('Emp_code')
        rfirst_name =  request.POST.get('first_name')
        rlast_name = request.POST.get('last_name')
        rpassword = request.POST.get('password')
        remail = request.POST.get('email')
        rjoined_date = request.POST.get('joined_date')
        rphone = request.POST.get('phone')

        poda = hr.objects.create(
            Emp_code = rEmp_code,
            first_name = rfirst_name,
            last_name = rlast_name,
            password = rpassword,
            email = remail,
            joined_date = rjoined_date,
            phone = rphone,
        )
        poda.save()

        koi = req_hr.objects.get(Emp_code = rEmp_code)
        print(koi)
        koi.delete()
    elif 'raddman' in request.POST:
        print("approving the manager")
        gEmp_code = request.POST.get('Emp_code')
        gfirst_name =  request.POST.get('first_name')
        glast_name = request.POST.get('last_name')
        gpassword = request.POST.get('password')
        gemail = request.POST.get('email')
        gjoined_date = request.POST.get('joined_date')
        gphone = request.POST.get('phone')

        poda = manager.objects.create(
            Emp_code = gEmp_code,
            first_name = gfirst_name,
            last_name = glast_name,
            password = gpassword,
            email = gemail,
            joined_date = gjoined_date,
            phone = gphone,
        )
        poda.save()

        koi = req_man.objects.get(Emp_code = gEmp_code)
        print(koi)
        koi.delete()

    elif 'logout' in request.POST:
        return redirect('login')
    else:
        print('workin on view all admin')
        vemp = employee.objects.all()
        vhr = hr.objects.all()
        vman = manager.objects.all()
        return render(request,'home.html', {'role':'admin','object':user,'function' :'viewall','e':vemp,'m':vman,'h':vhr})
        

    return render(request,'home.html', {'role':'admin','object':user,})

 def hrreg(request):
    if 'reghr' in request.POST:
        epc = request.POST.get('epc')
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        pho = request.POST.get('pho')
        e = request.POST.get('e')
        p =request.POST.get('p')
        rp = request.POST.get('conp')
        print(fn,ln,pho,e,p,rp)
        if p == rp:
            ghy = req_hr.objects.create(
            Emp_code = epc,
            first_name = fn,
            last_name = ln,
            password = p,
            email =e,
            phone =pho,
            req_by = 'own'

        )

            ghy.save()

            return render(request,'login.html',{'error':'your request has sent'})

    return render(request,'hrreg.html')

 def manreg(request):
    if 'regman' in request.POST:
        epc = request.POST.get('epc')
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        pho = request.POST.get('pho')
        e = request.POST.get('e')
        p =request.POST.get('p')
        rp = request.POST.get('conp')
        print(fn,ln,pho,e,p,rp)
        if p == rp:
            ghy = req_man.objects.create(
            Emp_code = epc,
            first_name = fn,
            last_name = ln,
            password = p,
            email =e,
            phone =pho,
            req_by = 'own'

        )

            ghy.save()

            return render(request,'login.html',{'error':'your request has sent'})
    return render(request,'manreg.html')

except:
    print('some external erron')
    def hello(request):
        return render(request,'login.html',{'error':'some external error occured'})