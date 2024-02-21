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
        Hospitalizado=0.0791
        #Enfermedad
        D=0.0815
        O=0.1028
        T=0.0581
        S=0.1126
        N=0.645
        #Hombre hospitalizado y ambulatorio
        HA= H*A
        HH= H*Hospitalizado
        #Mujer hospitalizada y ambulatorio
        MA= M*A
        MH= M*Hospitalizado
        
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
                    self.probabilidad = (HAD)/(HAD + HAO + HAT+ HAS + HAN)
                    self.clave = 1
                elif enfermedad == "Hipertensión":
                    self.probabilidad = (HAS)/(HAD + HAO + HAT+ HAS + HAN)
                    self.clave = 2
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = (HAT)/(HAD + HAO + HAT+ HAS + HAN)
                    self.clave = 3
                elif enfermedad == "Obesidad":
                    self.probabilidad = (HAO)/(HAD + HAO + HAT+ HAS + HAN)
                    self.clave = 4
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = (HAN)/(HAD + HAO + HAT+ HAS + HAN)
                    self.clave = 5
                else:
                    print("Error en enfermedad")
            elif tipo == "Hospitalizado":
                if enfermedad == "Diabetes":
                    self.probabilidad = HHD/(HHD + HHO + HHS + HHN + HHT)
                    self.clave = 6
                elif enfermedad == "Hipertensión":
                    self.probabilidad = HHS/(HHD + HHO + HHS + HHN + HHT)
                    self.clave = 7
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = HHT/(HHD + HHO + HHS + HHN + HHT)
                    self.clave = 8
                elif enfermedad == "Obesidad":
                    self.probabilidad = HHO/(HHD + HHO + HHS + HHN + HHT)
                    self.clave = 9
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = HHN/(HHD + HHO + HHS + HHN + HHT)
                    self.clave = 10
                else:
                    print("Error en enfermedad")
            else:
                print("Error en tipo")
        elif genero == "Mujer":
            if tipo == "Ambulatorio":
                if enfermedad == "Diabetes":
                    self.probabilidad = MAD/(MAD+ MAN + MAO + MAS + MAT)
                    self.clave = 11
                elif enfermedad == "Hipertensión":
                    self.probabilidad = MAS/(MAD+ MAN + MAO + MAS + MAT)
                    self.clave = 12
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = MAT/(MAD+ MAN + MAO + MAS + MAT)
                    self.clave = 13
                elif enfermedad == "Obesidad":
                    self.probabilidad = MAO/(MAD+ MAN + MAO + MAS + MAT)
                    self.clave = 14
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = MAN/(MAD+ MAN + MAO + MAS + MAT)
                    self.clave = 15
                else:
                    print("Error en enfermedad")
            elif tipo == "Hospitalizado":
                if enfermedad == "Diabetes":
                    self.probabilidad = MHD/(MHD + MHN + MHO + MHS + MHT)
                    self.clave = 16
                elif enfermedad == "Hipertensión":
                    self.probabilidad = MHS/(MHD + MHN + MHO + MHS + MHT)
                    self.clave = 17
                elif enfermedad == "Tabaquismo":
                    self.probabilidad = MHT/(MHD + MHN + MHO + MHS + MHT)
                    self.clave = 18
                elif enfermedad == "Obesidad":
                    self.probabilidad = MHO/(MHD + MHN + MHO + MHS + MHT)
                    self.clave = 19
                elif enfermedad == "Otros/Ninguna":
                    self.probabilidad = MHN/(MHD + MHN + MHO + MHS + MHT)
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
