class controlador:
    def __init__(self):
        self.genero = ""
        self.tipo = ""
        self.enfermedad = ""
        self.clave = 0
        self.probabilidad = 0
        
    def calcularProbabilidad(self, genero, tipo, enfermedad):
        #Género
        H=0.5388
        M=0.4612
        #Tipo
        A=0.9209
        H=0.0791
        #Enfermedad
        D=0.0815
        O=0.1028
        T=0.0581
        S=0.1126
        N=0.645
        #Hombre hospitalizado y ambulatorio
        HA= H*A
        HH= H*H
        #Mujer hospitalizada y ambulatorio
        MA= M*A
        MH= M*H
        
        #Hombre enfermedades ambulatorio
        HAD = HA * D
        HAO = HA * O
        HAT = HA * T
        HAS = HA * S
        HAN = HA * N
        
        #Hombre enfermedades hospitalizado
        HHD = HH * D
        HHO = HH * O
        HHT = HH * T
        HHS = HH * S
        HHN = HH * N
        
        #Mujer enfermedades ambulatorio
        MAD = MA * D
        MAO = MA * O
        MAT = MA * T
        MAS = MA * S
        MAN = MA * N
        
        #Mujer enfermedades hospitalizado
        MHD = MH * D
        MHO = MH * O
        MHT = MH * T
        MHS = MH * S
        MHN = MH * N
        
        if genero == "Hombre":
            if tipo == "Ambulatorio":
                if enfermedad == "Diabetes":
                    self.probabilidad = (HA * HAD)/(HA * HAD + HH * HHD)
                    self.clave = 1
                elif enfermedad == "Hipertensión":
                    self.probabilidad = (HA * HAS)/(HA * HAS + HH * HHS)
                    self.clave = 2
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = (HA * HAT)/(HA * HAT + HH * HHT)
                    self.clave = 3
                elif enfermedad == "Obesidad":
                    self.probabilidad = (HA * HAO)/(HA * HAO + HH * HHO)
                    self.clave = 4
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = (HA * HAN)/(HA * HAN + HH * HHN)
                    self.clave = 5
                else:
                    print("Error en enfermedad")
            elif tipo == "Hospitalizado":
                if enfermedad == "Diabetes":
                    self.probabilidad = HH * HHD/(HH * HHD + HA * HAD)
                    self.clave = 6
                elif enfermedad == "Hipertensión":
                    self.probabilidad = HH * HHS/(HH * HHS + HA * HAS)
                    self.clave = 7
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = HH * HHT/(HH * HHT + HA * HAT)
                    self.clave = 8
                elif enfermedad == "Obesidad":
                    self.probabilidad = HH * HHO/(HH * HHO + HA * HAO)
                    self.clave = 9
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = HH * HHN/( HH * HHN + HA * HAN)
                    self.clave = 10
                else:
                    print("Error en enfermedad")
            else:
                print("Error en tipo")
        elif genero == "Mujer":
            if tipo == "Ambulatorio":
                if enfermedad == "Diabetes":
                    self.probabilidad = MA * MAD/(MA * MAD + MH * MHD)
                    self.clave = 11
                elif enfermedad == "Hipertensión":
                    self.probabilidad = MA * MAS/(MA * MAS + MH * MHS)
                    self.clave = 12
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = MA * MAT/(MA * MAT + MH * MHT)
                    self.clave = 13
                elif enfermedad == "Obesidad":
                    self.probabilidad = MA * MAO/(MA * MAO + MH * MHO)
                    self.clave = 14
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = MA * MAN/(MA * MAN + MH * MHN)
                    self.clave = 15
                else:
                    print("Error en enfermedad")
            elif tipo == "Hospitalizado":
                if enfermedad == "Diabetes":
                    self.probabilidad = MH * MHD/(MH * MHD + MA * MAD)
                    self.clave = 16
                elif enfermedad == "Hipertensión":
                    self.probabilidad = MH * MHS/(MH * MHS + MA * MAS)
                    self.clave = 17
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = MH * MHT/(MH * MHT + MA * MAT)
                    self.clave = 18
                elif enfermedad == "Obesidad":
                    self.probabilidad = MH * MHO/(MH * MHO + MA * MAO)
                    self.clave = 19
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = MH * MHN/(MH * MHN + MA * MAN)
                    self.clave = 20
                else:
                    print("Error en enfermedad")
            else:
                print("Error en tipo")
        else:
            print("Error en genero")
        self.probabilidad = self.probabilidad * 100
        print(self.probabilidad)
        return self.probabilidad
