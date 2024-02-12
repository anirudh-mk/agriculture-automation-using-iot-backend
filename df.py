# from django.db import models
#
#
# class Role(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#
#
# class Department(models.Model):
#     department_id = models.AutoField(primary_key=True)
#     department_name = models.CharField(max_length=255)
#
#
# class Staff(models.Model):
#     staff_id = models.AutoField(primary_key=True)
#     staff_name = models.CharField(max_length=255)
#     phno = models.CharField(max_length=15)
#     address = models.TextField()
#     dob = models.DateField()
#     qualification = models.CharField(max_length=255)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     doj = models.DateField()
#     status = models.CharField(max_length=50)
#     email = models.EmailField()
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     gender = models.CharField(max_length=10)
#     blood_group = models.CharField(max_length=5)
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#
#
# class StaffRoleLink(models.Model):
#     id = models.AutoField(primary_key=True)
#     staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_role_link_staff')
#     role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='staff_role_link_role')
#
#     class Meta:
#         db_table = 'staff_role_link'
#
#
# class LoginDetails(models.Model):
#     Logindetails_id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     logged_in = models.DateTimeField()
#     logged_out = models.DateTimeField()
#
#
# class Receptionist(models.Model):
#     register_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     blood_group = models.CharField(max_length=5)
#     contact = models.CharField(max_length=15)
#     address = models.TextField()
#     gender = models.CharField(max_length=10)
#     dob = models.DateField()
#     email = models.EmailField()
#     dov = models.DateField()
#     weight = models.DecimalField(max_digits=5, decimal_places=2)
#     height = models.DecimalField(max_digits=5, decimal_places=2)
#     age = models.IntegerField()
#
#
# class Doctor(models.Model):
#     doctor_id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     doctor_name = models.CharField(max_length=255)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     const_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     duty_time = models.CharField(max_length=50)
#
#
# class BookAppointment(models.Model):
#     appointment_id = models.AutoField(primary_key=True)
#     token_no = models.CharField(max_length=10)
#     register_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
#     doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     apnt_date = models.DateField()
#
#
# class RepBill(models.Model):
#     recbill_id = models.AutoField(primary_key=True)
#     register_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
#     reg_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     appointment_id = models.ForeignKey(BookAppointment, on_delete=models.CASCADE)
#     doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     # first_name = models.CharField(max_length=255)
#     # last_name = models.CharField(max_length=255)
#     data_and_time = models.DateTimeField()
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#
#
# class Medicine(models.Model):
#     med_id = models.AutoField(primary_key=True)
#     generic_name = models.CharField(max_length=255)
#     med_name = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
#     exp_date = models.DateField()
#
#
# class LabTest(models.Model):
#     test_id = models.AutoField(primary_key=True)
#     test_name = models.CharField(max_length=255)
#     low_range = models.DecimalField(max_digits=10, decimal_places=2)
#     high_range = models.DecimalField(max_digits=10, decimal_places=2)
#     normal_range = models.DecimalField(max_digits=10, decimal_places=2)
#     price = models.DecimalField(max_digits=10, decimal_places=2)



import uuid

from django.db import models


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255,default=uuid.uuid4())
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    consultation_fee = models.IntegerField(max_length=4)
    Duty_time = models.CharField(max_length=255)

    def _str_(self):
        return self.first_name


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    height = models.CharField(max_length=3)
    weight = models.CharField(max_length=3)
    date_registered = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.first_name


# class Appointment(models.Model):
#     appointment_id = models.AutoField(primary_key=True)
#     patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
#     doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
#     appointment_date = models.DateField(auto_now=True)
#     appointment_time = models.TimeField(auto_now=True)
#     token_no = models.CharField(max_length=10)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True, default='')
    dateandtime = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def _str_(self):
        return self.username


class Login(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def _str_(self):
        return self.email


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=255)
    phno = models.CharField(max_length=15)
    address = models.TextField()
    dob = models.DateField()
    qualification = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    doj = models.DateField()
    status = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class StaffRoleLink(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='staff_role_link_staff')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='staff_role_link_role')

    class Meta:
        db_table = 'staff_role_link'


class LoginDetails(models.Model):
    Logindetails_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    logged_in = models.DateTimeField()
    logged_out = models.DateTimeField()


class Receptionist(models.Model):
    register_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=5)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.EmailField()
    dov = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    const_fee = models.DecimalField(max_digits=10, decimal_places=2)
    duty_time = models.CharField(max_length=50)


class BookAppointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    token_no = models.CharField(max_length=10)
    register_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    apnt_date = models.DateField()


class RepBill(models.Model):
    recbill_id = models.AutoField(primary_key=True)
    register_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    reg_fee = models.DecimalField(max_digits=10, decimal_places=2)
    appointment_id = models.ForeignKey(BookAppointment, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    data_and_time = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class Medicine(models.Model):
    med_id = models.AutoField(primary_key=True)
    generic_name = models.CharField(max_length=255)
    med_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    exp_date = models.DateField()


class LabTest(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255)
    low_range = models.DecimalField(max_digits=10, decimal_places=2)
    high_range = models.DecimalField(max_digits=10, decimal_places=2)
    normal_range = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
