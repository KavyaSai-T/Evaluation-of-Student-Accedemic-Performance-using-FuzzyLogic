import random 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def Excellent(request):
	list_time_array = ['Excellent Performance','Great','Outstanding Performance','Impressive Performance']
	random_num = random.choice(list_time_array) 
	return random_num
def Good(request):
	list_time_array = ['Good Performance','Try to Get Excellent','Superb','Work to Improve']
	random_num = random.choice(list_time_array) 
	return random_num
def Average(request):
	list_time_array = ['Not Okay Improve','Average Performance','Try to Get Good Level','Work Hard']
	random_num = random.choice(list_time_array) 
	return random_num
def Poor(request):
	list_time_array = ['Poor Performance','You need to Improve Skill','Spend more time','Concentrate on your Studies']
	random_num = random.choice(list_time_array) 
	return random_num
def VeryPoor(request):
	list_time_array = ['Very Worst Performance','You need to Improve your level','Very Poor Performance']
	random_num = random.choice(list_time_array) 
	return random_num



ATTENDANCE = 'Attendance'
PERFORMANCE = 'Performance'
INTERNAL_MARKS = 'Internal_Marks'
EXTERNAL_MARKS = 'External_Marks'
POOR = 'Poor'
AVERAGE = 'Average'
GOOD = 'Good'
V_POOR = 'Very Poor'
EXCELLENT = 'Excellent'
low_parameter = [25,30,35,38]
average_parameter = [45,50,55,60]
good_parameter = [70,75,80,85]
V_POOR_parameter = [0,10,15,20]
excellent_parameter = [90,95,99,100]


def compute_fuzzy(attend, intr_mark, extn_mark):
	
	intrn_marks = ctrl.Antecedent(np.arange(intr_mark), INTERNAL_MARKS)
	attendance = ctrl.Antecedent(np.arange(attend), ATTENDANCE)
	extrn_marks = ctrl.Antecedent(np.arange(extn_mark), EXTERNAL_MARKS)

	intrn_marks[POOR] = fuzz.trapmf(intrn_marks.universe, low_parameter)
	intrn_marks[AVERAGE] = fuzz.trapmf(intrn_marks.universe, average_parameter)
	intrn_marks[GOOD] = fuzz.trapmf(intrn_marks.universe, good_parameter)
	intrn_marks[V_POOR] = fuzz.trapmf(intrn_marks.universe, V_POOR_parameter)
	intrn_marks[EXCELLENT] = fuzz.trapmf(intrn_marks.universe, excellent_parameter)

	extrn_marks[POOR] = fuzz.trapmf(extrn_marks.universe, low_parameter)
	extrn_marks[AVERAGE] = fuzz.trapmf(extrn_marks.universe, average_parameter)
	extrn_marks[GOOD] = fuzz.trapmf(extrn_marks.universe, good_parameter)
	extrn_marks[V_POOR] = fuzz.trapmf(extrn_marks.universe, V_POOR_parameter)
	extrn_marks[EXCELLENT] = fuzz.trapmf(extrn_marks.universe, excellent_parameter)

	attendance[POOR] = fuzz.trapmf(attendance.universe, low_parameter)
	attendance[AVERAGE] = fuzz.trapmf(attendance.universe, average_parameter)
	attendance[GOOD] = fuzz.trapmf(attendance.universe, good_parameter)
	attendance[V_POOR] = fuzz.trapmf(attendance.universe, V_POOR_parameter)
	attendance[EXCELLENT] = fuzz.trapmf(attendance.universe, excellent_parameter)

	rule1 = ctrl.Rule(attendance[POOR] & extrn_marks[POOR] & intrn_marks[POOR])
	rule2 = ctrl.Rule(attendance[POOR] & extrn_marks[AVERAGE] & intrn_marks[POOR])
	rule3 = ctrl.Rule(attendance[POOR] & extrn_marks[GOOD] & intrn_marks[POOR])
	rule4 = ctrl.Rule(attendance[POOR] & extrn_marks[V_POOR] & intrn_marks[POOR])
	rule5 = ctrl.Rule(attendance[POOR] & extrn_marks[GOOD] & intrn_marks[V_POOR])
	rule6 = ctrl.Rule(attendance[POOR] & extrn_marks[POOR] & intrn_marks[AVERAGE])
	rule7 = ctrl.Rule(attendance[POOR] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE])
	rule8 = ctrl.Rule(attendance[POOR] & extrn_marks[GOOD] & intrn_marks[AVERAGE])
	rule9 = ctrl.Rule((attendance[POOR] & extrn_marks[GOOD] & intrn_marks[GOOD]))
	rule10 = ctrl.Rule(attendance[POOR] & extrn_marks[EXCELLENT] & intrn_marks[GOOD])
	rule11 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[AVERAGE] & intrn_marks[GOOD])
	rule12 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[GOOD] & intrn_marks[GOOD])
	rule13 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[V_POOR] & intrn_marks[GOOD])
	rule14 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[V_POOR] & intrn_marks[V_POOR])
	rule15 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[AVERAGE] & intrn_marks[EXCELLENT])
	rule16 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE])
	rule17 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[POOR] & intrn_marks[POOR])
	rule18 = ctrl.Rule(attendance[AVERAGE] & extrn_marks[POOR] & intrn_marks[GOOD])
	rule19 = ctrl.Rule(attendance[GOOD] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE])
	rule20 = ctrl.Rule(attendance[GOOD] & extrn_marks[EXCELLENT] & intrn_marks[EXCELLENT])
	rule21 = ctrl.Rule(attendance[GOOD] & extrn_marks[GOOD] & intrn_marks[AVERAGE])
	rule22 = ctrl.Rule(attendance[GOOD] & extrn_marks[POOR] & intrn_marks[POOR])
	rule23 = ctrl.Rule(attendance[V_POOR] & extrn_marks[EXCELLENT] & intrn_marks[V_POOR])
	rule24 = ctrl.Rule(attendance[V_POOR] & extrn_marks[V_POOR] & intrn_marks[V_POOR])
	rule25 = ctrl.Rule(attendance[V_POOR] & extrn_marks[POOR] & intrn_marks[POOR])
	rule26 = ctrl.Rule(attendance[V_POOR] & extrn_marks[GOOD] & intrn_marks[V_POOR])
	rule27 = ctrl.Rule(attendance[V_POOR] & extrn_marks[EXCELLENT] & intrn_marks[EXCELLENT])
	rule28 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[EXCELLENT] & intrn_marks[V_POOR])
	rule29 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE])
	rule30 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[V_POOR])
	rule31 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[GOOD])
	rule32 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[POOR])
	rule33 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[POOR])
	rule34 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[AVERAGE])
	rule35 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[GOOD] & intrn_marks[POOR])
	rule36 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[GOOD])
	rule37 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[V_POOR] & intrn_marks[POOR])
	rule38 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[V_POOR])
	rule39 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[EXCELLENT])
	rule40 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[EXCELLENT])
	rule41 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[GOOD] & intrn_marks[EXCELLENT])
	rule42 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[V_POOR] & intrn_marks[EXCELLENT])
	rule43 = ctrl.Rule(attendance[EXCELLENT] & extrn_marks[EXCELLENT] & intrn_marks[EXCELLENT])


	rule_list = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, 
				rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, 
				rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, 
				rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
				rule41, rule42, rule43]

	performance_ctrl = ctrl.ControlSystem(rule_list)
	perf_analysis = ctrl.ControlSystemSimulation(performance_ctrl)

	perf_analysis.input[ATTENDANCE] = attend
	perf_analysis.input[EXTERNAL_MARKS] = extn_mark
	perf_analysis.input[INTERNAL_MARKS] = intr_mark

	perf_analysis.compute()

	return (str(perf_analysis.output[PERFORMANCE]))