#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 20:15:11 2022

@author: ab
"""

def extractor(data):
    # for i in data:
        # print(i)
    data_length=len(data)
    d=data_length
    # print(data_length)
    # print("last index value ={}".format(data[data_length-1][data_length-1]))
    # print("last 2nd index value ={}".format(data[data_length-1][data_length-2]))
    # print("last index value ={}".format(data[data_length-2][data_length-1]))
    # print("last index value ={}".format(data[data_length-2][data_length-2]))
    
    
    # i need to go using index and collect all data using index and store value in a list and return the list.
    if data_length==21:
        data_mode= data[d-1][d-1]+data[d-1][d-2]+data[d-2][d-1]+data[d-2][d-2]
        # print(data_mode)
        data_character_size = data[d-3][d-1]+data[d-3][d-2]+data[d-4][d-1]+data[d-4][d-2]
        # print(data_character_size)
        
        """block line 1 from last upward"""
        block1_data1 =data[d-5][d-1]+data[d-5][d-2]+data[d-6][d-1]+data[d-6][d-2]
        block1_data2 =data[d-7][d-1]+data[d-7][d-2]+data[d-8][d-1]+data[d-8][d-2]
        block1_data3 =data[d-9][d-1]+data[d-9][d-2]+data[d-10][d-1]+data[d-10][d-2]
        block1_data4 =data[d-11][d-1]+data[d-11][d-2]+data[d-12][d-1]+data[d-12][d-2]
        
        """block1 combine data"""
        b1_d = block1_data1+block1_data2+block1_data3+block1_data4
        # block combine end
        
        """block line 2 from last downward"""
        block2_data1 =data[d-12][d-3]+data[d-12][d-4]+data[d-11][d-3]+data[d-11][d-4]
        block2_data2 =data[d-10][d-3]+data[d-10][d-4]+data[d-9][d-3]+data[d-9][d-4]
        block2_data3 =data[d-8][d-3]+data[d-8][d-4]+data[d-7][d-3]+data[d-7][d-4]
        block2_data4 =data[d-6][d-3]+data[d-6][d-4]+data[d-5][d-3]+data[d-5][d-4]
        block2_data5 =data[d-4][d-3]+data[d-4][d-4]+data[d-3][d-3]+data[d-3][d-4]
        block2_data6 =data[d-2][d-3]+data[d-2][d-4]+data[d-1][d-3]+data[d-1][d-4]
        """block2 combine data"""
        b2_d = block2_data1+block2_data2+block2_data3+block2_data4+block2_data5+block2_data6
        # data combine end.
        """block line 3 from last upward"""
        block3_data1 =data[d-1][d-5]+data[d-1][d-6]+data[d-2][d-5]+data[d-2][d-6]
        block3_data2 =data[d-3][d-5]+data[d-3][d-6]+data[d-4][d-5]+data[d-4][d-6]
        block3_data3 =data[d-5][d-5]+data[d-5][d-6]+data[d-6][d-5]+data[d-6][d-6]
        block3_data4 =data[d-7][d-5]+data[d-7][d-6]+data[d-8][d-5]+data[d-8][d-6]
        block3_data5 =data[d-9][d-5]+data[d-9][d-6]+data[d-10][d-5]+data[d-10][d-6]
        block3_data6 =data[d-11][d-5]+data[d-11][d-6]+data[d-12][d-5]+data[d-12][d-6]
        """block2 combine data"""
        b3_d = block3_data1+block3_data2+block3_data3+block3_data4+block3_data5+block3_data6
        # data combine end
        """block line 4 from last downward"""
        block4_data1 =data[d-12][d-7]+data[d-12][d-8]+data[d-11][d-7]+data[d-11][d-8]
        block4_data2 =data[d-10][d-7]+data[d-10][d-8]+data[d-9][d-7]+data[d-9][d-8]
        block4_data3 =data[d-8][d-7]+data[d-8][d-8]+data[d-7][d-7]+data[d-7][d-8]
        block4_data4 =data[d-6][d-7]+data[d-6][d-8]+data[d-5][d-7]+data[d-5][d-8]
        block4_data5 =data[d-4][d-7]+data[d-4][d-8]+data[d-3][d-7]+data[d-3][d-8]
        block4_data6 =data[d-2][d-7]+data[d-2][d-8]+data[d-1][d-7]+data[d-1][d-8]
        """block2 combine data"""
        b4_d = block4_data1+block4_data2+block4_data3+block4_data4+block4_data5+block4_data6
        # data combine end
        """block line 5 from last upward"""
        block5_data1 =data[d-1][d-9]+data[d-1][d-10]+data[d-2][d-9]+data[d-2][d-10]
        block5_data2 =data[d-3][d-9]+data[d-3][d-10]+data[d-4][d-9]+data[d-4][d-10]
        block5_data3 =data[d-5][d-9]+data[d-5][d-10]+data[d-6][d-9]+data[d-6][d-10]
        block5_data4 =data[d-7][d-9]+data[d-7][d-10]+data[d-8][d-9]+data[d-8][d-10]
        block5_data5 =data[d-9][d-9]+data[d-9][d-10]+data[d-10][d-9]+data[d-10][d-10]
        block5_data6 =data[d-11][d-9]+data[d-11][d-10]+data[d-12][d-9]+data[d-12][d-10]
        block5_data7 =data[d-13][d-9]+data[d-13][d-10]+data[d-14][d-9]+data[d-14][d-10]
        block5_data8 =data[d-16][d-9]+data[d-16][d-10]+data[d-17][d-9]+data[d-17][d-10]
        block5_data9 =data[d-18][d-9]+data[d-18][d-10]+data[d-19][d-9]+data[d-19][d-10]
        block5_data10 =data[d-20][d-9]+data[d-20][d-10]+data[d-21][d-9]+data[d-21][d-10]
        """block5 cobine data"""
        b5_d = block5_data1+block5_data2+block5_data3+block5_data4+block5_data5+block5_data6+block5_data7+block5_data8+block5_data9+block5_data10
        """block line 6 from last downward"""
        block6_data1 =data[d-21][d-11]+data[d-21][d-12]+data[d-20][d-11]+data[d-20][d-12]
        block6_data2 =data[d-19][d-11]+data[d-19][d-12]+data[d-18][d-11]+data[d-18][d-12]
        block6_data3 =data[d-17][d-11]+data[d-17][d-12]+data[d-16][d-11]+data[d-16][d-12]
        block6_data4 =data[d-14][d-11]+data[d-14][d-12]+data[d-13][d-11]+data[d-13][d-12]
        block6_data5 =data[d-12][d-11]+data[d-12][d-12]+data[d-11][d-11]+data[d-11][d-12]
        block6_data6 =data[d-10][d-11]+data[d-10][d-12]+data[d-9][d-11]+data[d-9][d-12]
        block6_data7 =data[d-8][d-11]+data[d-8][d-12]+data[d-7][d-11]+data[d-7][d-12]
        block6_data8 =data[d-6][d-11]+data[d-6][d-12]+data[d-5][d-11]+data[d-5][d-12]
        block6_data9 =data[d-4][d-11]+data[d-4][d-12]+data[d-3][d-11]+data[d-3][d-12]
        block6_data10 =data[d-2][d-11]+data[d-2][d-12]+data[d-1][d-11]+data[d-1][d-12]
        """block 6 data combine"""
        b6_d = block6_data1+block6_data2+block6_data3+block6_data4+block6_data5+block6_data6+block6_data7+block6_data8+block6_data9+block6_data10
        
        # this block are from left side mid block 
        """block line 7 from last upward"""
        block7_data1 =data[d-9][d-13]+data[d-9][d-14]+data[d-10][d-13]+data[d-10][d-14]
        block7_data2 =data[d-11][d-13]+data[d-11][d-14]+data[d-12][d-13]+data[d-12][d-14]
        """block2 combine data"""
        b7_d = block7_data1+block7_data2
        # data cmbn end
        """block line 8 from last downward"""
        block8_data1 =data[d-12][d-16]+data[d-12][d-17]+data[d-11][d-16]+data[d-11][d-17]
        block8_data2 =data[d-10][d-16]+data[d-10][d-17]+data[d-9][d-16]+data[d-9][d-17]
        """block8 combine data"""
        b8_d =block8_data1+block8_data2
        # block 8 end
        """block line 9 from last upward"""
        block9_data1 =data[d-9][d-18]+data[d-9][d-19]+data[d-10][d-18]+data[d-10][d-19]
        block9_data2 =data[d-11][d-18]+data[d-11][d-19]+data[d-12][d-18]+data[d-12][d-19]
        """block9 combine data"""
        b9_d = block9_data1+block9_data2
        # b9 end
        """block line 10 from last downward"""
        block10_data1 =data[d-12][d-20]+data[d-12][d-21]+data[d-11][d-20]+data[d-11][d-21]
        block10_data2 =data[d-10][d-20]+data[d-10][d-21]+data[d-9][d-20]+data[d-9][d-21]
        """block 10 combine"""
        b10_d = block10_data1+block10_data2
        #  all block end ###
        
        
        # need to add all the datablock 
        data_stream =data_mode+data_character_size+b1_d+b2_d+b3_d+b4_d+b5_d+b6_d+b7_d+b8_d+b9_d+b10_d
        
        # print(data_stream)
        return data_stream
    
    elif data_length==25:
        data_mode= data[d-1][d-1]+data[d-1][d-2]+data[d-2][d-1]+data[d-2][d-2]
        # print(data_mode)
        data_character_size = data[d-3][d-1]+data[d-3][d-2]+data[d-4][d-1]+data[d-4][d-2]
        # print(data_character_size)
        # data block 1 upward
        block1_data1 = data[d-5][d-1]+data[d-5][d-2]+data[d-6][d-1]+data[d-6][d-2]
        block1_data2 = data[d-7][d-1]+data[d-7][d-2]+data[d-8][d-1]+data[d-8][d-2]
        block1_data3 = data[d-9][d-1]+data[d-9][d-2]+data[d-10][d-1]+data[d-10][d-2]
        block1_data4 = data[d-11][d-1]+data[d-11][d-2]+data[d-12][d-1]+data[d-12][d-2]
        block1_data5 = data[d-13][d-1]+data[d-13][d-2]+data[d-14][d-1]+data[d-14][d-2]
        block1_data6 = data[d-15][d-1]+data[d-15][d-2]+data[d-16][d-1]+data[d-16][d-2]
        
        # block 1 data combine
        b1_d=data_mode+data_character_size+block1_data1+block1_data2+block1_data3+block1_data4+block1_data5+block1_data6
        
        # data block 2 downward 
        block2_data1 = data[d-16][d-3]+data[d-16][d-4]+data[d-15][d-3]+data[d-15][d-4]
        block2_data2 = data[d-14][d-3]+data[d-14][d-4]+data[d-13][d-3]+data[d-13][d-4]
        block2_data3 = data[d-12][d-3]+data[d-12][d-4]+data[d-11][d-3]+data[d-11][d-4]
        block2_data4 = data[d-10][d-3]+data[d-10][d-4]+data[d-9][d-3]+data[d-9][d-4]
        block2_data5 = data[d-8][d-3]+data[d-8][d-4]+data[d-7][d-3]+data[d-7][d-4]
        block2_data6 = data[d-6][d-3]+data[d-6][d-4]+data[d-5][d-3]+data[d-5][d-4]
        block2_data7 = data[d-4][d-3]+data[d-4][d-4]+data[d-3][d-3]+data[d-3][d-4]
        block2_data8 = data[d-2][d-3]+data[d-2][d-4]+data[d-1][d-3]+data[d-1][d-4]
        # block2 data combine
        b2_d =block2_data1+block2_data2+block2_data3+block2_data4+block2_data5+block2_data6+block2_data7+block2_data8
        
        # block3 data upward
        block3_data1= data[d-1][d-5]+data[d-1][d-6]+data[d-2][d-5]+data[d-2][d-6]
        block3_data2 = data[d-3][d-5]+data[d-3][d-6]+data[d-4][d-5]+data[d-4][d-6]
        block3_data3 = data[d-10][d-5]+data[d-10][d-6]+data[d-11][d-5]+data[d-11][d-6]
        block3_data4 = data[d-12][d-5]+data[d-12][d-6]+data[d-13][d-5]+data[d-13][d-6]
        block3_data5 = data[d-14][d-5]+data[d-14][d-6]+data[d-15][d-5]+data[d-15][d-6]
        block3_data6 = data[d-16][d-5]+data[d-16][d-6]+data[d-16][d-7]+data[d-16][d-8]
        # block 3 combine
        b3_d = block3_data1+block3_data2+block3_data3+block3_data4+block3_data5+block3_data6
        
        # block 4 data downward
        block4_data1 = data[d-15][d-7]+data[d-15][d-8]+data[d-14][d-7]+data[d-14][d-8]
        block4_data2 = data[d-13][d-7]+data[d-13][d-8]+data[d-12][d-7]+data[d-12][d-8]
        block4_data3 = data[d-11][d-7]+data[d-11][d-8]+data[d-10][d-7]+data[d-10][d-8]
        block4_data4 = data[d-4][d-7]+data[d-4][d-8]+data[d-3][d-7]+data[d-3][d-8]
        block4_data5 = data[d-2][d-7]+data[d-2][d-8]+data[d-1][d-7]+data[d-1][d-8]
        # block4 data conbine
        b4_d =block4_data1+block4_data2+block4_data3+block4_data4+block4_data5
        
        # block5 data upward
        block5_data1 = data[d-1][d-9]+data[d-1][d-10]+data[d-2][d-9]+data[d-2][d-10]
        block5_data2 = data[d-3][d-9]+data[d-3][d-10]+data[d-4][d-9]+data[d-4][d-10]
        
        block5_data3 = data[d-5][d-10]+data[d-6][d-10]+data[d-7][d-10]+data[d-8][d-10]
        
        block5_data4 = data[d-9][d-10]+data[d-10][d-9]+data[d-10][d-10]+data[d-11][d-9]
        block5_data5 = data[d-11][d-10]+data[d-12][d-9]+data[d-12][d-10]+data[d-13][d-9]
        block5_data6 = data[d-13][d-10]+data[d-14][d-9]+data[d-14][d-10]+data[d-15][d-9]
        block5_data7 = data[d-15][d-10]+data[d-16][d-9]+data[d-16][d-10]+data[d-17][d-9]
        block5_data8 = data[d-17][d-10]+data[d-18][d-9]+data[d-18][d-10]+data[d-20][d-9]
        block5_data9 = data[d-20][d-10]+data[d-21][d-9]+data[d-21][d-10]+data[d-22][d-9]
        block5_data10 = data[d-22][d-10]+data[d-23][d-9]+data[d-23][d-10]+data[d-24][d-9]
        block5_data11 = data[d-24][d-10]+data[d-25][d-9]+data[d-25][d-10]+data[d-25][d-11]
        # block 5 data combine
        b5_d = block5_data1+block5_data2+block5_data3+block5_data4+block5_data5+block5_data6+block5_data7+block5_data8+block5_data9+block5_data10+block5_data11
        
        # block 6 downward
        block6_data1 = data[d-25][d-12]+data[d-24][d-11]+data[d-24][d-12]+data[d-23][d-11]
        block6_data2 = data[d-23][d-12]+data[d-22][d-11]+data[d-22][d-12]+data[d-21][d-11]
        block6_data3 = data[d-21][d-12]+data[d-20][d-11]+data[d-20][d-12]+data[d-18][d-11]
        block6_data4 = data[d-18][d-12]+data[d-17][d-11]+data[d-17][d-12]+data[d-16][d-11]
        block6_data5 = data[d-16][d-12]+data[d-15][d-11]+data[d-15][d-12]+data[d-14][d-11]
        block6_data6 = data[d-14][d-12]+data[d-13][d-11]+data[d-13][d-12]+data[d-12][d-11]
        block6_data7 = data[d-12][d-12]+data[d-11][d-11]+data[d-11][d-12]+data[d-10][d-11]
        block6_data8 = data[d-10][d-12]+data[d-9][d-11]+data[d-9][d-12]+data[d-8][d-11]
        block6_data9 = data[d-8][d-12]+data[d-7][d-11]+data[d-7][d-12]+data[d-6][d-11]
        block6_data10 = data[d-6][d-12]+data[d-5][d-11]+data[d-5][d-12]+data[d-4][d-11]
        block6_data11 = data[d-4][d-12]+data[d-3][d-11]+data[d-3][d-12]+data[d-2][d-11]
        block6_data12 = data[d-2][d-12]+data[d-1][d-11]+data[d-1][d-12]+data[d-1][d-13]
        # block6 data combine
        b6_d =block6_data1+block6_data2+block6_data3+block6_data4+block6_data5+block6_data6+block6_data7+block6_data8+block6_data9+block6_data10+block6_data11+block6_data12
        
        # block7 data upward
        block7_data1 = data[d-1][d-14]+data[d-2][d-13]+data[d-2][d-14]+data[d-3][d-13]
        block7_data2 = data[d-3][d-14]+data[d-4][d-13]+data[d-4][d-14]+data[d-5][d-13]
        block7_data3 = data[d-5][d-14]+data[d-6][d-13]+data[d-6][d-14]+data[d-7][d-13]
        block7_data4 = data[d-7][d-14]+data[d-8][d-13]+data[d-8][d-14]+data[d-9][d-13]
        block7_data5 = data[d-9][d-14]+data[d-10][d-13]+data[d-10][d-14]+data[d-11][d-13]
        block7_data6 = data[d-11][d-14]+data[d-12][d-13]+data[d-12][d-14]+data[d-13][d-13]
        block7_data7 = data[d-13][d-14]+data[d-14][d-13]+data[d-14][d-14]+data[d-15][d-13]
        block7_data8 = data[d-15][d-14]+data[d-16][d-13]+data[d-16][d-14]+data[d-17][d-13]
        
        block7_data9 = data[d-17][d-14]+data[d-18][d-13]+data[d-18][d-14]+data[d-20][d-13]
        block7_data10 = data[d-20][d-14]+data[d-21][d-13]+data[d-21][d-14]+data[d-22][d-13]
        
        block7_data11 = data[d-22][d-14]+data[d-23][d-13]+data[d-23][d-14]+data[d-24][d-13]
        block7_data12 = data[d-24][d-14]+data[d-25][d-13]+data[d-25][d-14]+data[d-25][d-15]
        # block7 data combine
        b7_d = block7_data1+block7_data2+block7_data3+block7_data4+block7_data5+block7_data6+block7_data7+block7_data8+block7_data9+block7_data10+block7_data11+block7_data12
        
        # block 8 data downward
        block8_data1 = data[d-25][d-16]+data[d-24][d-15]+data[d-24][d-16]+data[d-23][d-15]
        block8_data2 = data[d-23][d-16]+data[d-22][d-15]+data[d-22][d-16]+data[d-21][d-15]
        block8_data3 = data[d-21][d-16]+data[d-20][d-15]+data[d-20][d-16]+data[d-18][d-15]
        block8_data4 = data[d-18][d-16]+data[d-17][d-15]+data[d-17][d-16]+data[d-16][d-15]
        
        block8_data5 = data[d-16][d-16]+data[d-15][d-15]+data[d-15][d-16]+data[d-14][d-15]
        block8_data6 = data[d-14][d-16]+data[d-13][d-15]+data[d-13][d-16]+data[d-12][d-15]
        block8_data7 = data[d-12][d-16]+data[d-11][d-15]+data[d-11][d-16]+data[d-10][d-15]
        block8_data8 = data[d-10][d-16]+data[d-9][d-15]+data[d-9][d-16]+data[d-8][d-15]
        block8_data9 = data[d-8][d-16]+data[d-7][d-15]+data[d-7][d-16]+data[d-6][d-15]
        block8_data10 = data[d-6][d-16]+data[d-5][d-15]+data[d-5][d-16]+data[d-4][d-15]
        block8_data11 = data[d-4][d-16]+data[d-3][d-15]+data[d-3][d-16]+data[d-2][d-15]
        block8_data12 = data[d-2][d-16]+data[d-1][d-15]+data[d-1][d-16]+data[d-9][d-17]
        # block8 data combine
        b8_d = block8_data1+block8_data2+block8_data3+block8_data4+block8_data5+block8_data6+block8_data7+block8_data8+block8_data9+block8_data10+block8_data11+block8_data12

        # block 9 data upward
        block9_data1 = data[d-9][d-18]+data[d-10][d-17]+data[d-10][d-18]+data[d-11][d-17]
        block9_data2 = data[d-11][d-18]+data[d-12][d-17]+data[d-12][d-18]+data[d-13][d-17]
        block9_data3 = data[d-13][d-18]+data[d-14][d-17]+data[d-14][d-18]+data[d-15][d-17]
        block9_data4 = data[d-15][d-18]+data[d-16][d-17]+data[d-16][d-18]+data[d-16][d-20]
        # block9 data combine
        b9_d =block9_data1+block9_data2+block9_data3+block9_data4

        # block 10 downward
        block10_data1 = data[d-16][d-21]+data[d-15][d-20]+data[d-15][d-21]+data[d-14][d-20]
        block10_data2 = data[d-14][d-21]+data[d-13][d-20]+data[d-13][d-21]+data[d-12][d-20]
        block10_data3 = data[d-12][d-21]+data[d-11][d-20]+data[d-11][d-21]+data[d-10][d-20]
        block10_data4 = data[d-10][d-21]+data[d-9][d-20]+data[d-9][d-21]+data[d-9][d-22]
        # block 10 data combine
        b10_d = block10_data1+block10_data2+block10_data3+block10_data4
        
        # block 11 data upward
        block11_data1 = data[d-9][d-23]+data[d-10][d-22]+data[d-10][d-23]+data[d-11][d-22]
        block11_data2 = data[d-11][d-23]+data[d-12][d-22]+data[d-12][d-23]+data[d-13][d-22]
        block11_data3 = data[d-13][d-23]+data[d-14][d-22]+data[d-14][d-23]+data[d-15][d-22]
        block11_data4 = data[d-15][d-23]+data[d-16][d-22]+data[d-16][d-23]+data[d-16][d-24]
        # block11 data combine
        b11_d =block11_data1+block11_data2+block11_data3+block11_data4
        
        # block 12 data downward
        block12_data1 = data[d-16][d-25]+data[d-15][d-24]+data[d-15][d-25]+data[d-14][d-24]
        block12_data2 = data[d-14][d-25]+data[d-13][d-24]+data[d-13][d-25]+data[d-12][d-24]
        block12_data3 = data[d-12][d-25]+data[d-11][d-24]+data[d-11][d-25]+data[d-10][d-24]
        block12_data4 = data[d-10][d-25]+data[d-9][d-24]+data[d-9][d-25]
        # block 12 data combine
        b12_d = block12_data1+block12_data2+block12_data3+block12_data4
        
        return b1_d+b2_d+b3_d+b4_d+b5_d+b6_d+b7_d+b8_d+b9_d+b10_d+b11_d+b12_d
    
    else:
        print("upper version isnot done yet")
    






        
