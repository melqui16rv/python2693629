class Filtro:
    def __init__ (self,salario,departamento,municipio,desempeño,ocupacion,contrato,jornada,fechapu,economianara,teletrabajo):
        self.__salario=salario
        self.__departamento=departamento
        self.__municipio=municipio
        self.__desempeño=desempeño
        self.__ocupacion=ocupacion
        self.__contrato=contrato
        self.__jornada=jornada
        self.__fechapu=fechapu
        self.__economianara=economianara
        self.__teletrabajo=teletrabajo


    def setSalario(self,salario):
        self.__salario=salario
    def getSalario(self):
        return self.__salario
    
    def setDepartamento(self,departamento):
        self.__departamento=departamento
    def getDepartamento(self):
        return self.__departamento 
    
    def setMunicipo(self,municipio):
        self.__municipio=municipio
    def getMunicipio(self):
        return self.__municipio
    
    def setDesempeño(self,desempeño):
        self.__desempeño=desempeño
    def getDesempeño(self):
        return self.__desempeño
    
    def setOcupacion(self,ocupacion):
        self.__ocupacion=ocupacion
    def getOcupacion(self):
        return self.__ocupacion
    
    def setContrato(self,contrato):
        self.__contrato=contrato
    def getSalario(self):
        return self.__contrato
    
    def setJornada(self,jornada):
        self.__jornada=jornada
    def getJornada(self):
        return self.__jornada
    
    def setFechapu(self,fechapu):
        self.__fechapu=fechapu
    def getSalario(self):
        return self.__fechapu
    
    def setEconomianara(self,economianara):
        self.__economianara=economianara
    def getEconomianara(self):
        return self.__economianara
    
    def setTeletrabajo(self,teletrabajo):
        self.__teletrabajo=teletrabajo
    def getTeletrabajo(self):
        return self.__teletrabajo
    
    