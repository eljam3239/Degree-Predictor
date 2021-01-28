import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


print("Welcome to EngSelect! Choosing a discipline in your engineering undergrad can be stressful. We're here to help!")
print("You will be prompted for your achieved or projected grades in the first year engineering courses, as well as your overall enjoyment of those courses.")
print("Our algorithm will use your information to calculate which discipline(s) we think you'd be best suited for.")

#use try-catch statements to test if the user input is valid, and if so, stores the data to a variable which will be written to a csv file. 
courses = []
letterGrades = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'f','F']
#mod 1 enjoyment
while True:
    try:
        enjoy100=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 100?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy100 <11:
            courses.append(enjoy100)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#mod 1 grade
while True:
    try:
        grade100=input("What letter grade (A, B, C, D, F) did you achieve in APSC 100? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade100 in letterGrades:
            
            courses.append(grade100.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#phys1 enjoyment
while True:
    try:
        enjoy111=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 111?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy111 <11:
            courses.append(enjoy111)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#phys 1  grade
while True:
    try:
        grade111=input("What letter grade (A, B, C, D, F) did you achieve in APSC 111? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade111 in letterGrades:
            
            courses.append(grade111.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 131 enjoyment
while True:
    try:
        enjoy131=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 131?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy131 <11:
            courses.append(enjoy131)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 131 grade
while True:
    try:
        grade131=input("What letter grade (A, B, C, D, F) did you achieve in APSC 131? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade131 in letterGrades:
            
            courses.append(grade131.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 143 enjoyment
while True:
    try:
        enjoy143=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 143?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy143 <11:
            courses.append(enjoy143)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 143 grade
while True:
    try:
        grade143=input("What letter grade (A, B, C, D, F) did you achieve in APSC 143? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade143 in letterGrades:
            
            courses.append(grade143.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 151 enjoyment
while True:
    try:
        enjoy151=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 151?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy151 <11:
            courses.append(enjoy151)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 151 grade
while True:
    try:
        grade151=input("What letter grade (A, B, C, D, F) did you achieve in APSC 151? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade151 in letterGrades:
            
            courses.append(grade151.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 171 enjoyment
while True:
    try:
        enjoy171=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 171?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy171 <11:
            courses.append(enjoy171)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 171 grade
while True:
    try:
        grade171=input("What letter grade (A, B, C, D, F) did you achieve in APSC 171? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade171 in letterGrades:
            
            courses.append(grade171.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 112 enjoyment
while True:
    try:
        enjoy112=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 112?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy112 <11:
            courses.append(enjoy112)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 112 grade
while True:
    try:
        grade112=input("What letter grade (A, B, C, D, F) did you achieve in APSC 112? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade112 in letterGrades:
            
            courses.append(grade112.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")
#apsc 132 enjoyment
while True:
    try:
        enjoy132=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 132?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy132 <11:
            courses.append(enjoy132)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 132 grade
while True:
    try:
        grade132=input("What letter grade (A, B, C, D, F) did you achieve in APSC 132? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade132 in letterGrades:
            
            courses.append(grade132.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 162 enjoyment
while True:
    try:
        enjoy162=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 162?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy162 <11:
            courses.append(enjoy162)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 162 grades
while True:
    try:
        grade162=input("What letter grade (A, B, C, D, F) did you achieve in APSC 162? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade162 in letterGrades:
            
            courses.append(grade162.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 174 enjoyment
while True:
    try:
        enjoy174=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 174?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy174 <11:
            courses.append(enjoy174)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 174 grades
while True:
    try:
        grade174=input("What letter grade (A, B, C, D, F) did you achieve in APSC 174? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade174 in letterGrades:
            
            courses.append(grade174.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")

#apsc 182 enjoyment
while True:
    try:
        enjoy182=int(input("On a scale of 1 to 10, how would you rate your enjoyment for APSC 182?> "))
    except ValueError:
        print("Sorry, please input a number between 1 and 10: ")
        continue

    else:
        if 1<=enjoy182 <11:
            courses.append(enjoy182)
            break
        else:
            print("Sorry, please input a number between 1 and 10: ")
#apsc 182 grades
while True:
    try:
        grade182=input("What letter grade (A, B, C, D, F) did you achieve in APSC 182? ")
    except ValueError:
        print("Sorry, please input a letter grade : ")
        continue

    else:
        if grade182 in letterGrades:
            
            courses.append(grade182.upper())
            break
        else:
            print("Sorry, please input a letter grade: ")


for i in range(len(courses)):
    if courses[i] == 'A':
        courses[i] = 1
    elif courses[i] == 'B':
        courses[i] =2
    elif courses[i] == 'C':
        courses[i] =3
    elif courses[i] == 'D':
        courses[i] =4
    elif courses[i] == 'F':
        courses[i] =5 

#classification algorithm
df = pd.read_csv('Engineering Discipline Survey Results.csv')
df.head()
num_of_classes = len(df.Class.unique())
df.describe()

X = df.drop(axis=0, columns=['Class', 'Case #'])
Y = df.Class

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

xgb = XGBClassifier(booster='gbtree', objective='multi:softprob', random_state=42, eval_metric="auc", num_class=num_of_classes)

xgb.fit(X_train,y_train)

val = xgb.predict(X_test)

lb = preprocessing.LabelBinarizer()
lb.fit(y_test)

y_test_lb = lb.transform(y_test)
val_lb = lb.transform(val)

roc_auc_score(y_test_lb, val_lb, average='macro')
output = pd.DataFrame()
output['Expected Output'] = y_test
output['Predicted Output'] = val

output.tail()

#predict user's discipline
userInput = pd.DataFrame(courses).to_csv('UserInput.csv',index=False)
userInput = pd.read_csv('UserInput.csv', names = ['100 Interest','100 Grade','111 Interest', '111 Grade','131 Interest',	'131 Grade','143 Interest',	'143 Grade','151 Interest',	'151 Grade','171 Interest',	'171 Grade','112 Interest',	'112 Grade','132 Interest',	'132 Grade',	'162 Interest',	'162 Grade','174 Interest',	'174 Grade',	'182 Interest',	'182 Grade'])
discipline = pd.DataFrame()
discipline['Your Discipline is'] = xgb.predict(userInput)
d = discipline.head(1).iloc[0]['Your Discipline is']

#convert prediction to text and print discipline information
if d == 1: 
    print('\nYour recommended discipline is Chemical Engineering.\nChemical Engineers are in demand in almost every imaginable sector of the economy. Many start their careers as process engineers, working in the design and operation of manufacturing plants, and then progress to key management positions in their firms. Chemical Engineering is a broadly based engineering discipline, which combines the study of mathematics, chemistry, physics and biology, with engineering science, design, and economics. Chemical Engineers develop new advanced materials and design the processes that convert raw materials into value-added products. Students in Chemical Engineering learn how to design safe, efficient, environmentally-friendly, sustainable and economical processes and products. They also acquire direct experience with pilot-scale chemical process equipment and simulators. Queen’s Chemical Engineering offers options in Chemical Process Engineering and in Biochemical Engineering. What is Chemical Engineering: https://www.youtube.com/watch?v=RJeWKvQD90Y\nDay in the Life: https://www.youtube.com/watch?v=doLVkXi4j3w\nRelated: Engineering Chemistry ')
elif d == 2: 
    print('\nYour recommended discipline is Engineering Chemistry.\nAs the only program of its kind in North America, Engineering Chemistry provides in-depth knowledge of chemistry in addition to engineering core knowledge. Engineering Chemistry graduates are experts in the chemistry behind industrial processes and combine a strong background in both chemistry and chemical engineering to treat problems of industrial interest. In this program, you will study applied organic chemistry, inorganic chemistry, reactivity principles, methods of determining structure, and you will acquire knowledge of materials at a molecular level. You will be able to apply this core chemical knowledge to design and improve processes and materials, ranging from fuel cells to pharmaceuticals. Accreditation by the Canadian Society for Chemistry as a chemistry program, and the Canadian Engineering Accreditation Board as an engineering program, allows graduates to pursue professional careers in both disciplines – a truly unique benefit of an Engineering Chemistry degree.\nWhat is engineering chemistry: https://www.youtube.com/watch?v=78WJXwwDlbQ ')
elif d == 3: 
    print('\nYour recommended discipline is Engineering Physics.\nStudents in Engineering Physics learn how to apply the knowledge of the fundamental physical principles underlying modern technology and processes. You will study a strategic combination of math, physics, and engineering courses from a chosen specialty area. Courses in quantum mechanics, laser optics and nanotechnology will help prepare you for an engineering career at the leading edge of technology. You will acquire advanced problem-solving and instrumentation skills, and will be able to apply your superior mathematical, analytical and abstract-thinking ability to modern engineering challenges. Engineering Physics offers 4 options; mechanical, computing, electrical and materials.\nQueen’s Engineering Physics: https://www.youtube.com/watch?v=H2EAv3f9S50&t=100s\nWhat is engineering physics: https://www.youtube.com/watch?v=BTWjaLv5wr8 ')
elif d == 4: 
    print('\nYour recommended discipline is Mechanical and Materials Engineering.\nMechanical engineers are needed wherever there are machines or devices, including the human body! Their work encompasses every stage of design, manufacturing, testing, operation, and research. In this program, you will combine the study of basic engineering with practical courses in mechanical design, materials, and manufacturing methods. \nMany students are attracted to the mechanical engineering program because it is the most broadly based of the engineering disciplines. The mechanical engineer’s knowledge and skills are needed in a remarkable range of industries. \nLike chemical engineering student’s, mechanical engineering students have a broad range of career opportunities due to the multidisciplinary nature of mechanical engineering. Students can choose to concentrate in one of the following areas: aerospace, biomechanical, energy and fluid systems, manufacturing, materials, or mechatronics. \nQueen’s Mechanical Engineering: \nhttps://www.youtube.com/watch?v=LqMIklql6Gw \nDay in the Life of a Mechanical Engineer: \nhttps://www.youtube.com/watch?v=2M4Ry2pkBl4 \nWhat is mechanical engineering? https://www.youtube.com/watch?v=W74y1RxN6BA ')
elif d == 5: 
    print('\nYour recommended discipline is Civil Engineering.\nWe go about our lives within a physical environment created by civil engineers: houses, schools, office buildings, highways, and bridges, even river and coastal systems, and green landfills. Civil Engineering is a challenging and dynamic profession serving society to improve the quality of our life, the health of our social system, the continuity of our economy and business activities, and our competitive position in the international market place.\nAs a civil engineering student, you will study how to plan, design, and build these structures and systems with an environmentally respectful approach. As part of its real-world preparation, this innovative program emphasizes self-learning, teamwork, communication, leadership and problem solving. Students can pick one of 4 options: Structural Design, Environmental Engineering, Geotechnical Engineering and Hydraulics. \nQueen’s Civil Engineering: https://www.youtube.com/watch?v=RxYbiTRTH_w&t=21s \nDay in the Life of a Civil Engineer: https://www.youtube.com/watch?v=mwbekuQSJWc ')
elif d == 6:
    print('\nYour recommended discipline is Geological Engineering. \nGeological engineers combine systems engineering skills with earth science principles to find and extract energy and mineral resources, to design foundations for dams and buildings, to design tunnels, caverns and mine openings, to stabilize slopes and protect against natural hazards, to manage our underground water resources and to protect our environment from contamination. Geological Engineers connect earth sciences with engineering – they apply geosciences, mathematics, physics, and chemistry to solve engineering challenges in fields such as civil engineering and construction, mining and energy resource exploration and development, environmental engineering, forensic engineering, and forestry, amongst others. Intro to geological engineering at Queen’s: https://www.youtube.com/watch?v=UVJmo76l64k\nPrinciples of Geological Engineering and It’s Careers: https://www.youtube.com/watch?v=e9QvO5fX7Cs\nDay in the Life of a Geological Engineer: https://www.youtube.com/watch?v=yi-qgPY4urA\nRelated: Civil, Mining ')
elif d == 7: 
    print('\nYour recommended discipline is Mathematics & Engineering.\nThis program is unique in Canada. Course content includes highly sophisticated mathematical approaches to engineering issues. As a Mathematics and Engineering student, you will take pure and applied math along with engineering courses in your chosen area of specialization. You will learn to analyze and solve engineering problems requiring superior math skills, such as those involving modern communications, control and mechatronic systems. Students can choose from one of three options: Applied Mechanics, Computing and Communications and Systems and Robotics.\nQueen’s Applied Math and Engineering: https://www.youtube.com/watch?v=oj_i87quRpc \nStudies in Math and Engineering: \nhttps://www.youtube.com/watch?v=cnntaDaGpJ4 ')
elif d == 8: 
    print('\nYour recommended discipline is Electrical Engineering.\nElectrical engineers are specialists who provide essential support for the conveniences and services related to electric power and communications and take leading roles in the design of new products and services. As an electrical engineering student, you will study electric circuits and motors, electromagnetics, microelectronics, signal processing, communications, robotics and control, digital logic, and microprocessors. You will build on a base of applied mathematics and physics and learn to use the laws of physics that govern electrical systems to design new products and services. \nStudents can specialize into the following streams: biomedical engineering, communications and signal processing, communications systems and networks, microelectronics and photonic, mechatronics, power electronics and systems and robotics and control. \nQueen’s Electrical Engineering: https://www.youtube.com/watch?v=2nh4bNs2suA \nDay in the Life of an Electrical Engineer: https://www.youtube.com/watch?v=Va0F9_0T9R4 \nWhat is electrical engineering: https://www.youtube.com/watch?v=QQewdCJTcIU ')
elif d == 9: 
    print('\nYour recommended discipline is Mining Engineering.\nAside from plants, all of the raw materials used by human society come from minerals extracted from the earth. This program prepares you for careers in the minerals industry and related environmental and technological fields. Traditionally, mining has been one of the broadest engineering fields. A mining engineer is required to be familiar with all of aspects of work involved in the operation of a mining project – from the initial discovery stage to the marketing of a final product. For this reason, mining students receive some basic training in each of the major engineering fields. \nAs a Mining Engineering student, you will study a broad range of disciplines involved in locating, extracting, refining, and disposing of mineral and metal products and by-products. The program teaches students how these processes can be carried out efficiently and competitively, with a focus on sustainability and the environment. \nStudents can choose from one of three options: mining engineering, mine-mechanical engineering or mineral processing and environmental engineering. \nQueen’s Mining engineering: https://www.youtube.com/watch?v=DjrN66lfvHM \nWhat is mining engineering: https://www.youtube.com/watch?v=3CFVGU9WJUo \nDay in the life of a mining engineer: https://www.youtube.com/watch?v=Sw6gpMmZmXM ')
else: 
    print('\nYour recommended discipline is Computer Engineering.\nThe information and communications technology of our knowledge-based society places computer engineers at the hub of a revolution that is perpetually evolving and changing the way we live and work. Computer Engineering provides the software and hardware that govern how we produce, consume, learn, shop, bank, entertain, travel, and connect with each other.\nThe discipline is at the intersection of engineering, computer science, and mathematics and combines software engineering and computer hardware and architecture. In this program, you will study circuits, electronics, digital systems, microprocessors, computer architecture, data structures, algorithms, computer networks, operating systems, and software specification and development. \nStudents in Computer Engineering have a flexibility in areas of specialization that other options do not have. The general areas in which they can tailor their courses are Computer Hardware, Computer Systems, Software Engineering, Mechatronics and Artificial Intelligence.  \nQueen’s Computer Engineering: https://www.youtube.com/watch?v=eTyPXWqPJUM \nDay in the Life of a computer engineering student: https://www.youtube.com/watch?v=2eV6_yngcEY \nWhat is Computer Engineering: https://www.youtube.com/watch?v=avZTQgLs064 ')

