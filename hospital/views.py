from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from .models import *
import datetime
import uuid
from alipay import AliPay


# Create your views here.
class ChooseLoginView(View):
    '''选择身份登录'''

    def get(self, request):
        return render(request, 'chooselogin.html')


class PatientLoginView(View):
    '''患者登录'''

    def get(self, request):
        return render(request, 'patientlogin.html')

    def post(self, request):
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')

        patient_list = Patient.objects.filter(phone=phone, password=password)
        if patient_list:
            request.session['patient'] = patient_list[0]

            return HttpResponseRedirect("/patientcenter/")

        return HttpResponse("登录有问题")


class DoctorLoginView(View):
    '''医生登录'''

    def get(self, request):
        return render(request, 'doctorlogin.html')

    def post(self, request):
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')

        doctor_list = Doctor.objects.filter(phone=phone, password=password)
        if doctor_list:
            request.session['doctor'] = doctor_list[0]

            return HttpResponse("进入医生界面")

        return HttpResponse("登录有问题")


class PatientRegisterView(View):
    '''患者注册'''

    def get(self, request):
        return render(request, 'patientregister.html')

    def post(self, request):
        # 只能注册患者账号 医生账号只能由管理员添加
        phone = request.POST.get('phone', '')

        patientlist = Patient.objects.filter(phone=phone)
        if patientlist:
            return render(request, 'patientregister.html', {"err": 1, "tips": "*该号码已经被注册"})
        else:
            password = request.POST.get('password', '')
            name = request.POST.get('name', '')
            sex = request.POST.get('sex', '')
            age = request.POST.get('age', '')

            patient = Patient.objects.create(phone=phone, password=password, name=name, sex=sex, age=age)

            if patient:
                return HttpResponseRedirect("/patientlogin/")

            return HttpResponseRedirect("/patientregister/")


class PatientCenterView(View):
    '''患者界面'''

    def get(self, request):
        patient = request.session.get('patient', '')

        return render(request, 'patientcenter.html', {'patient_name': patient.name})


class ChooseDepartmentView(View):
    '''选择科室'''

    def get(self, request):
        parentid_department_list = [o.id for o in Department.objects.filter(parentid=0)]

        all_department_list = dict()
        for id in parentid_department_list:
            all_department_list[Department.objects.filter(id=id)[0].name] = Department.objects.filter(parentid=id)

        # print(all_department_list)

        return render(request, 'choosedepartment.html', {'all_department_list': all_department_list})


class ChooseDoctorAndTimeView(View):
    '''选择医生和时间'''

    def get(self, request, department_id):
        department_id = int(department_id)

        department_name = Department.objects.get(id=department_id).name  # 科室名字

        doctor_list = Doctor.objects.filter(department_id=department_id)  # 当前科室里的医生

        doctor_time_number_list = []  # 此医生及其的可预约时间和人数列表
        for doctor in doctor_list:
            doctor_id = doctor.id
            doctor_time_number_list.append([doctor, TimeNumber.objects.get(doctor_id=doctor_id)])

        tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        return render(request, 'choosedoctorandtime.html',
                      {'department_name': department_name, 'doctor_time_number_list': doctor_time_number_list,
                       'department_id': department_id, 'tomorrow': tomorrow})


# 支付宝公钥
alipay_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsvqQkhIIoFS+k+krQYuHBsemR0zQ0BFQcUdbPUwuiFAuqVI9ZgrUbZ3cBisJ5rngayPB1cergvg+sKaoCjGCbiOZAib1tE/tG/UvSUzo/rTgjf/FpIGwEbQp27Owd5M5mJyxB0tZ0NRfxnNtjvpJxf6Tqo7cfUWXHlH+KNnh1eVvpHzQftolQaNmes3vJtJiWkXol5cGWPLzJJkJyIQEqJVPvV9/L15pZeDZCCtgok/j/KU4ujsNUoZhYQU4pmJhu610Pi3vO4qiJT/2zvro85yjNYC/MigeShHdiCxc/+UTfDuDqM+X+F3gFcasvSdyD2ImPpTR4oTvL9MgmuskSQIDAQAB
-----END PUBLIC KEY-----"""

# 应用私钥
my_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAsDmN53ZqOcZNsmkHrFFwpy/YcpFwkRbhjgXZ8wBhbjBOprAJrt4k8whU0P0inNALGgI+Afk+AkggA+yIQJeGTfbWqQdg7k+X44PPgFUXvhm4sSOs1/cqJ/9ETG9oJ6qc9IZOw0aba2rDSiBEkv4KUdJHouYEHcLtMutWaLYJQTWuDsQDy1dWG/Qo5ynzRcxs5SZIGhkFA24azEM+vjjIpFcgjDjkbpkydiC5VpB1tymFvGE7Xvq08LkTyVjpPK3P/N9a/IiyMdBLqC5CTEodoGBAcxryN2r9wgThdYd7jrq6eNGG0ACXRGNaA/ncrjPx9MGd56VL5BQuKUFHxtPZAwIDAQABAoIBAC8jxjTjdTjtNf2CoP3UbzkZ0GGdTCpTn5R5NjsNoAJ0w6VNM9nmLKYiVWXuQOMHt+CGNwYaIR9FIeNK04vLvK6AWB2xDpnRCsVejhQ7LvW4NbKU43iF8m3ul9uGdasetYunncwYyBxs276pcQ6NDD+k62rE8tbvPLpBP8UU5NbfTNU4iXnx6kaqYj+qn3Ps37ZSPsFegoPfBUWU/E+qLQgkeAJoIc01hodcaJ1DFMF79h7/t/2x4rLXhRVMG8dqKejog89JOjIJfPkI/SD8PzJ2qmim6McgyHEl3YBVeQ6MWK4/JsEX+Zj6liMYw4IS9jwTNZ3tjNnI8W5B5oNnwPkCgYEA/EYGQ/cuV/r4L3+6HaGyoppEn6uNd9OKEY7cbTY/mQyI6pRuJIV1yWX1E7WoLNFcIXOvqJk2YxqyQOPUw9SvqhctWrqbIDGA/dJMpCfII8QG29LgIphrwN2e7eX+YYae3e8CccPDfFNNjgU+6XRCVc3PIHIFXtgYejn7HHIPSC8CgYEAstPzX/g1X1/W2vxi5RFtKY7FI0LDKQlCQCqarJsjvhxY0UT+klSnO5tKlyl9q49USF06NgKWxKHCqNQuE6CJB5S7Ulecy7UNVDHSDIKd3VESE0jBQHhhGMuZLs0K4oMLCSuNCL+uQGI9IoVLrurRyUJk0bNRle/RTt3N7xcrc20CgYAIf9N2Nr24+RujfgonNWtvTwNA3ebGQrpEHSwQAePipCl4vcd4M4bkYir/nv8rg2I3Pk6Mv5y1ehDHXuWsM143vNAqXl8blo9h/dPXM//qNJCGl3Q1tizrMoxIN5d6ca6oi4TpkE7lwWi7gDG+a8xQV77CuRS1PVKVy55KNw2MwQKBgE1THJ9YwitVU6ApFdIa8OrRUyjmC2FJIZ6BTZRpGNFxjG4guTso448AnQYz6KUwOq93sF3+TJcFoxhBdxMBjX77ruvx+liTFwpa6IqESCKUlY5FHVr1Mnb4QmpcOuKq6zCx5i/sQjqQwAKXRJyD6OZvkQyjzxlYM1c4zX0etakZAoGBALOkXbGnzo6o+6M1LH5VJAkN0mr/SqkJOpIfN315Ec42/Cuz/fQ3CAD1s0AhvZBXDyw8s835XIzv5UjhVzhcr3hk88YORDgXL8xmmXvYSUS0TSOSs5C1VBTbB1jl4/dhEp/T8L2jr/zoL+HvIi5fBHdsCPAp2whjPARRPGXi6n0B
-----END RSA PRIVATE KEY-----"""

# 创建AliPay对象
alipay = AliPay(
    appid='2021000119657952',
    app_notify_url='http://127.0.0.1:8000/checkpay/',
    app_private_key_string=my_private_key,
    alipay_public_key_string=alipay_public_key,
    sign_type='RSA2',
    debug=True
)


class ConfirmRegistrationView(View):
    '''确认挂号信息'''

    def get(self, request, department_id, doctor_id, consultation_hours):
        department_id = int(department_id)
        doctor_id = int(doctor_id)

        patient = request.session.get('patient', '')
        doctor = Doctor.objects.get(id=doctor_id)
        department = Department.objects.get(id=department_id)

        patient_name = patient.name
        doctor_name = doctor.name
        registration_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        consultation_hours = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d") + " " + consultation_hours
        # doctor_id
        patient_id = patient.id
        address = department.address
        registration_price = doctor.registration_price
        # print(patient_name,doctor_name,registration_time,consultation_hours,doctor_id,patient_id,address)

        return render(request, 'confirmregistration.html', {'patient_name': patient_name, 'doctor_name': doctor_name,
                                                            'registration_time': registration_time,
                                                            'consultation_hours': consultation_hours,
                                                            'doctor_id': doctor_id, 'patient_id': patient_id,
                                                            'address': address,
                                                            'registration_price': registration_price})

    def post(self, request):
        patient_name = request.POST.get('patient_name', '')
        doctor_name = request.POST.get('doctor_name', '')
        registration_time = request.POST.get('registration_time', '')
        consultation_hours = request.POST.get('consultation_hours', '')
        illness = request.POST.get('illness', '')
        doctor_id = request.POST.get('doctor_id', '')
        patient_id = request.POST.get('patient_id', '')
        address = request.POST.get('address', '')
        out_trade_num = uuid.uuid4().hex
        payway = 'alipay'
        status = '待支付'
        isdelete = 1

        register = Register.objects.create(patient_name=patient_name, doctor_name=doctor_name,
                                           registration_time=registration_time,
                                           consultation_hours=consultation_hours, illness=illness, doctor_id=doctor_id,
                                           patient_id=patient_id, address=address, isdelete=isdelete,
                                           out_trade_num=out_trade_num,
                                           payway=payway, status=status)

        registration_price = request.POST.get('registration_price', '')

        params = alipay.api_alipay_trade_page_pay(
            subject='医院挂号',
            out_trade_no=register.out_trade_num,
            total_amount=registration_price,
            return_url='http://127.0.0.1:8000/checkpay/'
        )

        url = 'https://openapi.alipaydev.com/gateway.do' + '?' + params

        return HttpResponseRedirect(url)


class CheckPayView(View):
    def get(self, request):
        params = request.GET.dict()
        sign = params.pop('sign')

        if alipay.verify(params, sign):
            out_trade_no = params.get('out_trade_no', '')
            register = Register.objects.get(out_trade_num=out_trade_no)
            register.status = '已支付'
            register.isdelete = 0
            register.save()

            doctor_time_number = TimeNumber.objects.get(doctor_id=register.doctor_id)
            consultation_hours_time = str(register.consultation_hours)[11:]
            print('--------------------------------------------------')
            print(consultation_hours_time)
            if consultation_hours_time == '08:00:00':
                doctor_time_number.eight -= 1
            elif consultation_hours_time == '09:00:00':
                doctor_time_number.nine -= 1
            elif consultation_hours_time == '10:00:00':
                doctor_time_number.ten -= 1
            elif consultation_hours_time == '11:00:00':
                doctor_time_number.eleven -= 1
            elif consultation_hours_time == '14:00:00':
                doctor_time_number.fourteen -= 1
            elif consultation_hours_time == '15:00:00':
                doctor_time_number.fifteen -= 1
            elif consultation_hours_time == '16:00:00':
                doctor_time_number.sixteen -= 1
            elif consultation_hours_time == '17:00:00':
                doctor_time_number.seventeen -= 1
            doctor_time_number.save()

            return HttpResponseRedirect('/patientshowregistration/')

        out_trade_no = params.get('out_trade_no', '')
        register = Register.objects.get(out_trade_num=out_trade_no)
        register.isdelete = 1
        register.save()

        return HttpResponseRedirect('/choosedepartment/')


class PatientShowRegistrationView(View):
    '''患者展示挂号信息'''

    def get(self, request):
        patient = request.session.get('patient')
        register_list = patient.register_set.order_by('consultation_hours').filter(isdelete=False, status='已支付').all()

        return render(request, 'patientshowregistration.html', {'register_list': register_list})


class GuideView(View):
    def get(self, request):
        return render(request, 'guide.html')


class TrafficView(View):
    def get(self, request):
        return render(request, 'traffic.html')
