from ...postypes.configuration import configuration
# import math
# import numpy as np

# # Constants
# PI = math.pi
# d_6 = 0.215
# m = 0.33
# n = 0.645
# o = 0.115
# a = 1.15
# b = 1.22

# class InvKinematics:

   
#     R0_6 = np.zeros((3, 3))

#     def get_inv_kinematics(self, _pos):
        
#         # TODO: Implement inverse kinematics
         
#         new_X = _pos[0]
#         new_Y = _pos[1]
#         new_Z = _pos[2]
#         new_roll = _pos[3]
#         new_pitch = _pos[4]
#         new_yaw = _pos[5]
            
#         r11 = math.cos(new_roll) * math.cos(new_pitch)
#         r12 = (math.cos(new_roll) * math.sin(new_pitch) *
#                    math.sin(new_yaw)) - (math.sin(new_roll) * math.cos(new_yaw))
#         r13 = (math.cos(new_roll) * math.sin(new_pitch)* math.cos(new_yaw))+ (math.sin(new_roll) * math.sin(new_yaw))
#         r21 = math.sin(new_roll) * math.cos(new_pitch)
#         r22 = (math.sin(new_roll) * math.sin(new_pitch) * math.sin(new_yaw)) +(math.cos(new_roll) * math.cos(new_pitch))
#         r23 = (math.sin(new_roll) * math.sin(new_pitch) *math.cos(new_yaw)) - (math.cos(new_roll) * math.sin(new_yaw))
#         r31 = -math.sin(new_pitch)
#         r32 = math.cos(new_pitch) * math.sin(new_yaw)
#         r33 = math.cos(new_pitch) * math.cos(new_yaw)

#         R0_6 = np.array([[r11, r12, r13],
#                             [r21, r22, r23],
#                             [r31, r32, r33]])
        
#         # Compute the wrist center position Oc [Xc, Yc, Zc]
#         X_c = new_X - (d_6 * R0_6[0, 2])
#         Y_c = new_Y - (d_6 * R0_6[1, 2])
#         Z_c = new_Z - (d_6 * R0_6[2, 2])

#         d1 = np.sqrt(X_c ** 2 + Y_c ** 2)
#         Px_dash = None
#         Py_dash = Z_c - n

#         #Joint 5 points
#         print(f"P_x: {X_c}, P_y: {Y_c}, P_z: {Z_c}")
            
          
#         theta1_arr, theta2_arr, theta3_arr, theta4_arr, theta5_arr, theta6_arr = [], [], [], [], [], []
#         theta1_f, theta2_f, theta3_f = [], [], []
        
#         if X_c==0 and Y_c==0:
#              print("Shoulder Singularity detected")
#         else:
#             theta1_arr = find_theta1(X_c, Y_c)       

#             for i in range(len(theta1_arr) ):
#                 d1 = np.abs(Y_c)

#                 if (-175 < theta1_arr[i] < 175 and theta1_arr[i] != -90 and theta1_arr[i] != 90):
#                     if d1 > m:
#                         Px_dash = d1 - m
#                         theta2_arr, theta3_arr= forward_calc(Px_dash, Py_dash)    

#                         for j in range(len(theta2_arr)):
#                             if -140 < theta2_arr[j] < -5 and -120 < theta3_arr[j] < 168:
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

#                         Px_dash = m + d1

#                         if -185 < theta1_arr[i] < 185:
#                             theta2_arr, theta3_arr= backward_calc(Px_dash, Py_dash)
#                             if len(theta2_arr) == 2 or len(theta2_arr) == 1:
#                                 break

#                             #k = len(theta2_arr) - 1 if len(theta2_arr) == 3 else len(theta2_arr) - 2

#                             for j in range(len(theta2_arr)):
#                                 if -140 < theta2_arr[j] < -5 and -120 < theta3_arr[j] < 168:
#                                     print(f"Theta1: {theta1_arr[i+1]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                     theta1_f.append(theta1_arr[i+1])
#                                     theta2_f.append(theta2_arr[j])
#                                     theta3_f.append(theta3_arr[j])

                    

#                     elif d1 < m:
#                         Px_dash = m - d1
#                         theta2_arr, theta3_arr= backward_calc(Px_dash, Py_dash)

#                         for j in range(len(theta2_arr)):
#                             if -140 < theta2_arr[j] < -5 and -120 < theta3_arr[j] < 168:
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

#                         Px_dash = m + d1

#                         if -185 < theta1_arr[i] < 185:
#                             theta2_arr, theta3_arr=backward_calc(Px_dash, Py_dash)
#                             if len(theta2_arr) == 2 or len(theta2_arr) == 1:
#                                 break

#                             #k = len(theta2_arr) - 1 if len(theta2_arr) == 3 else len(theta2_arr) - 2

#                             for j in range(len(theta2_arr)):
#                                 if -140 < theta2_arr[j] < -5 and -120 < theta3_arr[j] < 168:
#                                     print(f"Theta1: {theta1_arr[i+1]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                     theta1_f.append(theta1_arr[i+1])
#                                     theta2_f.append(theta2_arr[j])
#                                     theta3_f.append(theta3_arr[j])

#                 elif theta1_arr[i] == -90:
#                     if Y_c > m:
#                         d1 = Y_c
#                         Px_dash = d1 - m
#                         theta2_arr, theta3_arr=forward_calc(Px_dash, Py_dash)
            
#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

                    
#                     elif Y_c < m:
#                         d1 = Y_c
#                         Px_dash = m - d1
#                         theta2_arr, theta3_arr=backward_calc(Px_dash, Py_dash)
        
#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

                    
            
#                 elif theta1_arr[i] == 90:
#                     if Y_c > m:
#                         d1 = Y_c
#                         Px_dash = d1 - m
#                         theta2_arr, theta3_arr=forward_calc(Px_dash, Py_dash)
            
#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])                  
        
#                     elif Y_c < m:
#                         d1 = Y_c
#                         Px_dash = m - d1
#                         theta2_arr, theta3_arr=backward_calc(Px_dash, Py_dash )
            
#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])



#                 elif -185 < theta1_arr[i] < -175:
#                     if d1 > m:
#                         Px_dash = d1 - m
#                         theta2_arr, theta3_arr=forward_calc(Px_dash, Py_dash )
            
#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

#                         if -185 < theta1_arr[i] < 185:
#                             theta2_arr, theta3_arr=forward_calc(Px_dash, Py_dash )
#                             if len(theta2_arr) == 2 or len(theta2_arr) == 1:
#                                 break

#                             #k = len(theta2_arr) - 1 if len(theta2_arr) == 3 else len(theta2_arr) - 2
#                             for j in range(len(theta2_arr)):
#                                 if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                     print(f"Theta1: {theta1_arr[i+1]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                     theta1_f.append(theta1_arr[i+1])
#                                     theta2_f.append(theta2_arr[j])
#                                     theta3_f.append(theta3_arr[j])

                    

#                     elif d1 < m:
#                         Px_dash = m - d1
#                         theta2_arr, theta3_arr=backward_calc(Px_dash, Py_dash)

#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

#                         if -185 < theta1_arr[i] < 185:
#                             theta2_arr, theta3_arr=backward_calc(Px_dash, Py_dash)
#                             if len(theta2_arr) == 2 or len(theta2_arr) == 1:
#                                 break

#                             #k = len(theta2_arr) - 1 if len(theta2_arr) == 3 else len(theta2_arr) - 2
#                             for j in range(len(theta2_arr)):
#                                 if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                     print(f"Theta1: {theta1_arr[i+1]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                     theta1_f.append(theta1_arr[i+1])
#                                     theta2_f.append(theta2_arr[j])
#                                     theta3_f.append(theta3_arr[j])

#                 elif 175 < theta1_arr[i] < 185:
#                     if d1 > m:
#                         Px_dash = d1 - m
#                         theta2_arr, theta3_arr=forward_calc(Px_dash, Py_dash )
            
#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

#                         if -185 < theta1_arr[i] < 185:
#                             theta2_arr, theta3_arr=forward_calc(Px_dash, Py_dash )
#                             if len(theta2_arr) == 2 or len(theta2_arr) == 1:
#                                 break

#                             #k = len(theta2_arr) - 1 if len(theta2_arr) == 3 else len(theta2_arr) - 2
#                             for j in range(len(theta2_arr)):
#                                 if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                     print(f"Theta1: {theta1_arr[i+1]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                     theta1_f.append(theta1_arr[i+1])
#                                     theta2_f.append(theta2_arr[j])
#                                     theta3_f.append(theta3_arr[j])


#                     elif d1 < m:
#                         Px_dash = m - d1
#                         theta2_arr, theta3_arr=backward_calc(Px_dash, Py_dash)

#                         for j in range(len(theta2_arr)):
#                             if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                 print(f"Theta1: {theta1_arr[i]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                 theta1_f.append(theta1_arr[i])
#                                 theta2_f.append(theta2_arr[j])
#                                 theta3_f.append(theta3_arr[j])

#                         if -185 < theta1_arr[i] < 185:
#                             theta2_arr, theta3_arr=backward_calc(Px_dash, Py_dash)
#                             if len(theta2_arr) == 2 or len(theta2_arr) == 1:
#                                 break

#                             #k = len(theta2_arr) - 1 if len(theta2_arr) == 3 else len(theta2_arr) - 2
#                             for j in range(len(theta2_arr)):
#                                 if (-140 < theta2_arr[j] < -5) and (-120 < theta3_arr[j] < 168):
#                                     print(f"Theta1: {theta1_arr[i+1]}, Theta2: {theta2_arr[j]}, Theta3: {theta3_arr[j]}")
#                                     theta1_f.append(theta1_arr[i+1])
#                                     theta2_f.append(theta2_arr[j])
#                                     theta3_f.append(theta3_arr[j])

            
        
#         inv_R0_3 = np.zeros((3, 3))
#         R3_6 = np.zeros((3, 3))

#         a_x, a_y, a_z, n_z, s_z = 0, 0, 0, 0, 0
#         th_1, th_2, th_3 = 0, 0, 0

#         solutions=[]
        
#         for j in range(len(theta1_f)):
#         #Here we are finding base rotational matrix R0_3
#             inv_R0_3 = find_rotational_matrix_R0_3(theta1_f[j], theta2_f[j], theta3_f[j])

#             R3_6 = np.zeros((3, 3))

#             # Here we are multiplying first two rotational matrices R0_3 and R0_6
#             R3_6 = np.dot(inv_R0_3, R0_6)
            
#             # Here are finding the angles theta 4, theta 5, theta 6
#             a_x = R3_6[0][2]
#             a_y = R3_6[1][2]
#             a_z = R3_6[2][2]
#             n_z = R3_6[2][0]
#             s_z = R3_6[2][1]
            
#             theta4_arr, theta5_arr, theta6_arr = find_theta4_theta5_theta6(a_x, a_y, a_z, n_z, s_z)           
            
#             for t in range(len(theta5_arr)):
#               if theta5_arr[t]==0:
#                 print("wrist singularity detected")
#               else:
#                 print("*****CONFIGURATION******\n")
#                 for i in range(0, len(theta4_arr)):
#                      print(f"[ {theta1_f[j] * np.pi / 180} {theta2_f[j] * np.pi / 180} {theta3_f[j] * np.pi / 180} "
#                        f"{theta4_arr[i] * np.pi / 180} {theta5_arr[i] * np.pi / 180} {theta6_arr[i] * np.pi / 180} ]")
#                      solutions.append(configuration([theta1_f[j] * np.pi / 180, theta2_f[j] * np.pi / 180, theta3_f[j] * np.pi / 180,
#                                  theta4_arr[i] * np.pi / 180, theta5_arr[i] * np.pi / 180, theta6_arr[i] * np.pi / 180]))
#               break
#         return solutions


#         # solutions = []
#         # solutions.append(configuration([0, 0, 1, 0, 0, 0]))
#         # solutions.append(configuration([1/8. * math.pi, 0, 1, 0, 0, 0]))
#         # solutions.append(configuration([2/8. * math.pi, 0, 1, 0, 0, 0]))
#         # solutions.append(configuration([3/8. * math.pi, 0, 1, 0, 0, 0]))
#         # solutions.append(configuration([4/8. * math.pi, 0, 1, 0, 0, 0]))
#         # solutions.append(configuration([5/8. * math.pi, 0, 1, 0, 0, 0]))
#         # solutions.append(configuration([6/8. * math.pi, 0, 1, 0, 0, 0]))
#         # solutions.append(configuration([7/8. * math.pi, 0, 1, 0, 0, 0]))

#         #return solutions

# def find_theta1(X_c, Y_c):
        
#     theta1 = -math.atan2(Y_c, X_c) * 180 / math.pi
#     arr = []

#     if -175 < theta1 < 175:
#         if X_c > 0 and Y_c < 0:
#             arr.extend([theta1, theta1 + 180, theta1 - 180])
#         elif X_c < 0 and Y_c < 0:
#             arr.extend([theta1, theta1 + 180, theta1 - 180])
#         elif X_c < 0 and Y_c > 0:
#             arr.extend([theta1, theta1 + 180, theta1 - 180])
#         elif X_c > 0 and Y_c > 0:
#             arr.extend([theta1, theta1 + 180, theta1 - 180])
#         elif X_c == 0 and Y_c > 0:
#             arr.extend([theta1, theta1 + 180])
#         elif X_c == 0 and Y_c < 0:
#             arr.extend([theta1, theta1 - 180])
#         elif -185 < theta1 < -175:
#             case1, case2, case3 = theta1, theta1 + 180, theta1 - 180
#             arr.extend([case1, case2, case3])
#         elif 175 < theta1 < 185:
#             case1, case2, case3 = theta1, theta1 + 180, theta1 - 180
#             arr.extend([case1, case2, case3])

#     return arr
    

      
# def forward_calc(Px_dash, Py_dash):
#     arr2 = []
#     arr3 = []
#     d_2 = math.sqrt(b**2 + o**2)   #d2 is the new link instead of b
#     d_3 = math.sqrt(Px_dash**2 + Py_dash**2)
#     if a+d_2>d_3:
#         beta1 = math.acos(((d_3**2) - (a**2) - (d_2**2)) /(-2 * a * d_2)) * 180 / PI     #angle between d_2 and a
#         alpha1 = math.asin(math.sin(beta1 * PI / 180) * (d_2 / d_3)) * 180 / PI          #angle between d_3 and Px_dash
#         alpha2 = math.asin(Py_dash / d_3) * 180 / PI                                     #angle between d_3 and a
#         # Forward elbow down
#         theta2 = -(alpha2 - alpha1)
#         theta3 = beta1 - (math.asin(b / d_2) * 180 / PI) - 90

#         if (-140 < theta2 < -5) and (-120 < theta3 < 168):
#             arr2.append(theta2)
#             arr3.append(theta3)


#         # Forward elbow up
#         theta2 = -(alpha1 + alpha2)
#         theta3 = 360 - beta1 - (math.asin(b / d_2) * 180 / PI) - 90

#         if (-140 < theta2 < -5) and (-120 < theta3 < 168):
#             arr2.append(theta2)
#             arr3.append(theta3)
#         else: 
#             print("***VALUE ERROR***")
#     return arr2, arr3

# def backward_calc(Px_dash, Py_dash):
#     arr4 = []
#     arr5 = []
#     d_2 = math.sqrt(b**2 + o**2)
#     d_3 = math.sqrt(Px_dash**2 + Py_dash**2)
#     if a+d_2>d_3:
#         beta1 = math.acos(((d_3**2) - (a**2) - (d_2**2)) /(-2 * a * d_2)) * 180 / PI
#         alpha1 = math.asin(math.sin(beta1 * PI / 180) * (d_2 / d_3)) * 180 / PI
#         alpha2 = math.asin(Py_dash / d_3) * 180 / PI
#         # Backward elbow down
#         theta2 = (alpha2 - alpha1) - 180
#         theta3 = 270 - beta1 - (math.asin(b / d_2) * 180 / PI)
#         if (-140 < theta2 < -5) and (-120 < theta3 < 168):
#             arr4.append(theta2)
#             arr5.append(theta3)
#         # Backward elbow up
#         theta2 = (alpha1 + alpha2) - 180
#         theta3 = -(90 - (beta1 - (math.asin(b / d_2) * 180 / PI)))
#         if (-140 < theta2 < -5) and (-120 < theta3 < 168):
#             arr4.append(theta2)
#             arr5.append(theta3)
#     else:
#       print("***VALUE ERROR***")
    
#     return arr4, arr5


# def find_rotational_matrix_R0_3(theta_1, theta_2, theta_3):
#     alpha = [180, 90, 0, 90]                       #Represents the twist angle about the Z axis between consecutive joint axes.
#     theta = [0, theta_1, theta_2, theta_3 - 90]    #Represents the joint angle about the common normal between consecutive joint axes.
#     R0_3 = np.eye(3)
#     for th, al in zip(theta, alpha):
#         c = math.cos(th * math.pi / 180)
#         s = math.sin(th * math.pi / 180)
#         nx, sx, ax = c, -s * math.cos(al * math.pi / 180), s * math.sin(al * math.pi / 180)
#         ny, sy, ay = s, c * math.cos(al * math.pi / 180), -c * math.sin(al * math.pi / 180)
#         nz, sz, az = 0, math.sin(al * math.pi / 180), math.cos(al * math.pi / 180)
#         Ri = np.array([[nx, sx, ax], [ny, sy, ay], [nz, sz, az]])                       #Denavit-Hartenberg Convention
#         R0_3 = np.dot(R0_3, Ri)
        
#     print("***********Rotational Matrix R0_3***********:\n", R0_3)
#     return R0_3

# def find_theta4_theta5_theta6(a_x, a_y, a_z, n_z, s_z):
#     arr4, arr5, arr6 = [], [], []
#     # Computing theta4
#     theta_4 = math.atan2(-a_y, -a_x) * 180 / math.pi
#     if (theta_4 - 360) > -350:
#         arr4.extend([theta_4, theta_4, theta_4 - 360, theta_4 - 360])
#     elif (theta_4 + 360) < 350:
#         arr4.extend([theta_4, theta_4, theta_4 + 360, theta_4 + 360])
#     # Computing theta5 and theta6
#     theta_5 = math.atan2(math.sqrt(1 - (a_z * a_z)), -a_z) * 180 / math.pi
#     theta_6 = math.atan2(s_z, n_z) * 180 / math.pi
#     if (theta_6 - 360) > -350:
#         arr5.extend([theta_5] * 4)
#         arr6.extend([theta_6, theta_6 - 360, theta_6, theta_6 - 360])
#     elif (theta_6 + 360) < 350:
#         arr5.extend([theta_5] * 4)
#         arr6.extend([theta_6, theta_6 + 360, theta_6, theta_6 + 360])

#     theta_5 = -theta_5

#     if theta_4 > 0:
#         theta_4 -= 180
#     else:
#         theta_4 += 180

#     if (theta_4 - 360) > -350:
#         arr4.extend([theta_4, theta_4, theta_4 - 360, theta_4 - 360])
#     elif (theta_4 + 360) < 350:
#         arr4.extend([theta_4, theta_4, theta_4 + 360, theta_4 + 360])

#     if theta_6 > 0:
#         theta_6 -= 180
#     else:
#         theta_6 += 180

#     if (theta_6 - 360) > -350:
#         arr5.extend([theta_5] * 4)
#         arr6.extend([theta_6, theta_6 - 360, theta_6, theta_6 - 360])
#     elif (theta_6 + 360) < 350:
#         arr5.extend([theta_5] * 4)
#         arr6.extend([theta_6, theta_6 + 360, theta_6, theta_6 + 360])

#     return arr4, arr5, arr6

##############################                  7 DOF ROBOT           #########################################################
import numpy as np
import math

#given parameteSrs:
alpha = [-np.pi/2, np.pi/2, -np.pi/2, -np.pi/2, np.pi/2, np.pi/2, 0]

d_bs = 0.340  # in mm
d_se = 0.400  
d_ew = 0.400  
d_wf = 0.126

class InvKinematics:
    
    
    
    def get_inv_kinematics(self,_pos):
        
        pos_X = _pos[0]
        pos_Y = _pos[1]
        pos_Z = _pos[2]
        roll = _pos[3]
        pitch = _pos[4]
        yaw = _pos[5]
            
        psi = np.concatenate((np.arange(-90, 0, 90), np.arange(0, 91, 90)))   
           
        # Rotation matrix R0_7
        r11 = math.cos(roll) * math.cos(pitch)
        r12 = (math.cos(roll) * math.sin(pitch) * math.sin(yaw)) - (math.sin(roll) * math.cos(yaw))
        r13 = (math.cos(roll) * math.sin(pitch) * math.cos(yaw)) + (math.sin(roll) * math.sin(yaw))
        r21 = math.sin(roll) * math.cos(pitch)
        r22 = (math.sin(roll) * math.sin(pitch) * math.sin(yaw)) + (math.cos(roll) * math.cos(pitch))
        r23 = (math.sin(roll) * math.sin(pitch) * math.cos(yaw)) - (math.cos(roll) * math.sin(yaw))
        r31 = -math.sin(pitch)
        r32 = math.cos(pitch) * math.sin(yaw)
        r33 = math.cos(pitch) * math.cos(yaw)

        R0_7 = np.array([[r11, r12, r13],
                        [r21, r22, r23],
                        [r31, r32, r33]])

      

        # Calculate shoulder to elbow (2p4), elbow to wrist (4p6), and wrist to flange (6p7) vectors
        p0_2 = np.array([0, 0, d_bs])
        p2_4 = np.array([0, d_se, 0])
        p4_6 = np.array([0, 0, d_ew])
        p6_7 = np.array([0, 0, d_wf])
        p0_7= np.array([pos_X, pos_Y, pos_Z])
       
        # Calculate the shoulder-wrist vector (2p6)
        p2_6 = p0_7 - p0_2 - np.dot(R0_7, p4_6)       
        print("Shoulder-Wrist vector:",p2_6)
        
        conventions = [
                {"GC2": 1, "GC4": 1, "GC6": 1},
                {"GC2": -1, "GC4": 1, "GC6": 1},
                {"GC2": 1, "GC4": 1, "GC6": -1},
                {"GC2": -1, "GC4": 1, "GC6": -1},
                {"GC2": 1, "GC4": -1, "GC6": 1},
                {"GC2": -1, "GC4": -1, "GC6": 1},
                {"GC2": 1, "GC4": -1, "GC6": -1},
                {"GC2": -1, "GC4": -1, "GC6": -1},
]        
        
        for gc in conventions: 
       
            # Virtual Joint angles
            theta_V= calculate_virtual_angle(p0_2,p2_4,p4_6,p2_6,gc["GC4"])
        
            theta_V1,theta_V2,theta_V3,theta_V4=theta_V
               
            #Virtual Rotational matrix
            R0_3_V= virtual_rotational_matrics(theta_V[:3])
        
            As = np.dot(cross_product_matrix(p2_6), R0_3_V)
            Bs = -np.dot(cross_product_matrix(p2_6)**2,  R0_3_V)
            Cs = np.dot(np.dot((cross_product_matrix(p2_6)),np.transpose(cross_product_matrix(p2_6))), R0_3_V)

            print("*****CONFIGURATION******\n")
        
            theta_all = []

            for psi_value in psi:
            
                #print(psi_value)
                # Extract values from matrices
                a_s31, b_s31, c_s31 = As[2, 0], Bs[2, 0], Cs[2, 0]
                a_s32, b_s32, c_s32 = As[2, 1], Bs[2, 1], Cs[1, 1]
                a_s33, b_s33, c_s33 = As[2, 2], Bs[2, 2], Cs[2, 2]
                a_s22, b_s22, c_s22 = As[1, 1], Bs[1, 1], Cs[1, 1]
                a_s12, b_s12, c_s12 = As[0, 1], Bs[0, 1], Cs[0, 1]


                # Calculate joint angles

                theta1 = np.arctan2(gc["GC2"] * (a_s22 * np.sin(psi_value) + b_s22 * np.cos(psi_value) + c_s22),
                                    gc["GC2"] * (a_s12 * np.sin(psi_value) + b_s12 * np.cos(psi_value) + c_s12))
                print("theta", theta1)
                
                #theta2 = np.arccos(a_s32 * np.sin(psi_value) + b_s32 * np.cos(psi_value) + c_s32)
           
                theta2 = gc["GC2"] * np.arccos(np.clip((a_s32 * np.sin(psi_value) + b_s32 * np.cos(psi_value) + c_s32), -1, 1))

          
                theta3 = np.arctan2(gc["GC2"] * (-a_s33 * np.sin(psi_value) - b_s33 * np.cos(psi_value) - c_s33),
                                    gc["GC2"] * (-a_s31 * np.sin(psi_value) - b_s31 * np.cos(psi_value) - c_s31))

                theta_4=theta_V4
           
        
                R3_4=np.array([
                                    [np.cos(theta_4), -np.sin(theta_4) * np.cos(alpha[3]), np.sin(theta_4) * np.sin(alpha[3])],
                                    [np.sin(theta_4), np.cos(theta_4) * np.cos(alpha[3]), -np.cos(theta_4) * np.sin(alpha[3])],
                                    [0, np.sin(alpha[3]), np.cos(alpha[3])]
                            
                                ])
    
                Aw = np.dot(np.dot(np.transpose(As), np.transpose(R3_4)), R0_7)
                Bw = np.dot(np.dot(np.transpose(Bs), np.transpose(R3_4)), R0_7)
                Cw = np.dot(np.dot(np.transpose(Cs), np.transpose(R3_4)), R0_7)
      
                # Extract values from matrices
                a_w31, b_w31, c_w31 = Aw[2, 0], Bw[2, 0], Cw[2, 0]
                a_w32, b_w32, c_w32 = Aw[2, 1], Bw[2, 1], Cw[1, 1]
                a_w33, b_w33, c_w33 = Aw[2, 2], Bw[2, 2], Cw[2, 2]
                a_w23, b_w23, c_w23 = Aw[1, 2], Bw[1, 2], Cw[1, 2]
                a_w13, b_w13, c_w13 = Aw[0, 2], Bw[0, 2], Cw[0, 2]

                theta_5 = np.arctan2(gc["GC6"] * (a_w23 * np.sin(psi_value) + b_w23 * np.cos(psi_value) + c_w23),
                                    gc["GC6"] * (a_w13 * np.sin(psi_value) + b_w13 * np.cos(psi_value) + c_w13))

            
                theta_6 = gc["GC6"] * np.arccos(np.clip((a_w33 * np.sin(psi_value) + b_w33 * np.cos(psi_value) + c_w33), -1, 1))


                theta_7 = np.arctan2(gc["GC6"] * (-a_w32 * np.sin(psi_value) - b_w32 * np.cos(psi_value) - c_w32),
                                    gc["GC6"] * (-a_w31 * np.sin(psi_value) - b_w31 * np.cos(psi_value) - c_w31))
            
                print("psi:", psi_value)
                print("Global_Configuration:",[gc["GC2"],gc["GC4"],gc["GC6"]])
                print("Solutions:",[theta1* 180 / np.pi,theta2* 180/np.pi, theta3* 180/np.pi, theta_4* 180 / np.pi, theta_5* 180 / np.pi, theta_6* 180 / np.pi, theta_7* 180 / np.pi])

                theta_all.append(configuration([np.degrees(theta1), np.degrees(theta2), np.degrees(theta3),
                            np.degrees(theta_4), np.degrees(theta_5), np.degrees(theta_6), np.degrees(theta_7)]))       

        return theta_all


def calculate_virtual_angle(p0_2,p2_4,p4_6,p2_6,GC4):
        
    v_se = p2_4 - p0_2
    v_ew = p4_6 - p2_4
    
    theta_v3=0
    
    theta_v1=np.arctan2(p2_6[1],p2_6[0])
    
    # Calculate θv4 using the law of cosines
    norm_2p6 = np.linalg.norm(p2_6)

    
    # Calculate the phi
    phi = np.arccos(np.clip((d_se**2 + np.dot(p2_6, p2_6) - d_ew**2) / (2 * d_se * np.linalg.norm(p2_6)),-1,1))
    
   
        
    # Calculate the virtual shoulder angle (θv4)
    theta_v4 = GC4 * np.arccos(np.clip((norm_2p6**2 - d_se**2 - d_ew**2) / (2 * d_se * d_ew), -1, 1))    # Calculate the virtual shoulder angle (θv2)
    theta_v2 = np.arctan2(np.sqrt(p2_6[0]**2 + p2_6[1]**2), p2_6[2]) + GC4 * phi
    
    #print(f"Virtual Elbow Angle (θv2): {theta_v2} degrees")
        
    theta_v=[theta_v1, theta_v2,theta_v3,theta_v4]
    
    return theta_v
        

def cross_product_matrix(v):

    cross= np.array([[0, -v[2], v[1]],
                    [v[2], 0, -v[0]],
                    [-v[1], v[0], 0]])
     
     
    return cross

def virtual_rotational_matrics(theta_v):
    R0_3_V = np.eye(3)

    for i in range(len(theta_v)):
        theta_i = theta_v[i]  # Convert degrees to radians 
        A_i = np.array([
            [np.cos(theta_i), -np.sin(theta_i) * np.cos(alpha[i]), np.sin(theta_i) * np.sin(alpha[i])],
            [np.sin(theta_i), np.cos(theta_i) * np.cos(alpha[i]), -np.cos(theta_i) * np.sin(alpha[i])],
            [0, np.sin(alpha[i]), np.cos(alpha[i])]
        ])
        R0_3_V = np.dot(R0_3_V, A_i)

    return R0_3_V


def detect_singularity(psi,gc_k,a_n,b_n,c_n,a_d,b_d,c_d):
    a_t= gc_k*(c_n*b_d - b_n*c_d)
    b_t= gc_k*(a_n*c_d - c_n*a_d)
    c_t= gc_k*(a_n*b_d - b_n*a_d)
    expression_value = (np.tan(psi/2)**2 * (b_t - c_t) - a_t)**2
   
    return expression_value


def singular_arm_angle(psi,gc_k,a_n,b_n,c_n,a_d,b_d,c_d):
    a_t= gc_k*(c_n*b_d - b_n*c_d)
    b_t= gc_k*(a_n*c_d - c_n*a_d)
    c_t= gc_k*(a_n*b_d - b_n*a_d)
    psi_sing = 2 * np.arctan(a_t * b_t - c_t)
    return psi_sing 
  

    

#target_pose = [0.117, -0.131,1, math.radians(45), math.radians(60), math.radians(60)]
#target_pose = [-1, -0.131,7, 45,80,60]
#inv_kinematics_instance = InvKinematics()
#joint_angles =inv_kinematics_instance.get_inv_kinematics(*target_pose)


