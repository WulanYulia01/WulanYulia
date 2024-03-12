from collections import namedtuple

def calculate_wages():
    name = input("Masukan nama karyawan: ")
    salary = float(input("Masukan gaji pokok: "))
    hours_per_day = 8

    daily_wage = salary / hours_per_day
    weekly_wage = daily_wage * (hours_per_day * 7)

    return namedtuple('Wages', 'name daily_wage weekly_wage')(name, daily_wage, weekly_wage)

wages = calculate_wages()
print(f'Nama karyawan: {wages.name}')
print(f'Masukan Pokok: {wages.daily_wage:.2f}')
print(f'Jumlah Jam kerja per Hari: {wages.daily_wage * 8:.2f}')

option = int(input("Pilih Rician Gaji Mingguan/ harian [1/2]: "))

if option == 1:
    print(f'Gaji Mingguan: {wages.weekly_wage:.2f}')
elif option == 2:
    print(f'Gaji Harian: {wages.daily_wage:.2f}')
else:
    print("Pilihan tidak valid.")