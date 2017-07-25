from sqlalchemy import Column, String, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    co_ruc = Column(String, primary_key = True)
    no_razons = Column(String)
    no_direccion = Column(String)
    tx_correo = Column(String)
    nu_telefono = Column(String)
    no_rubro = Column(String)
    lineas = relationship('Linea')
    personas = relationship('PersonalAutorizado')

    def __repr__(self):
        return '''<Empresa(co_ruc = '%s', no_razons = '%s', no_direccion = '%s', tx_correo = '%s', nu_telefono = '%s', no_rubro = '%s')>
        ''' % (self.co_ruc,
            self.no_razons,
            self.no_direccion,
            self.tx_correo,
            self.nu_telefono,
            self.no_rubro,)

class Linea(Base):
    __tablename__='linea'
    nu_linea = Column(String, primary_key=True)
    co_idplan = Column(String)
    nu_estado = Column(String)
    fe_fechaestado = Column(DateTime)
    co_rucempresa = Column(String, ForeignKey("empresa.co_ruc"),nullable= False)

    def __repr__(self):
        return '''<Linea(nu_linea = '%s', co_idplan = '%s', nu_estado = '%s', fe_fechaestado = '%s', co_rucempresa = '%s')>
        ''' % (
        self.nu_linea,
        self.co_idplan,
        self.nu_estado,
        self.fe_fechaestado,
        self.co_rucempresa,
        )


class PersonalAutorizado(Base):
    __tablename__='personalautorizado'
    co_dni = Column(String, primary_key=True)
    no_nombres = Column(String)
    no_apellidopat = Column(String)
    no_apellidomat = Column(String)
    nu_telefono = Column(String)
    tx_correo = Column(String)
    tx_estado = Column(String)
    fe_fechregistro = Column(String)
    co_rucemp = Column(String, ForeignKey('empresa.co_ruc'), nullable=False)

    def __repr__(self):
        return '''<PersonalAutorizado(co_dni = '%s', no_nombres = '%s', no_apellidopat = '%s', no_apellidomat = '%s', nu_telefono = '%s', tx_correo = '%s', tx_estado = '%s', fe_fechregistro = '%s', co_rucemp = '%s')>
        ''' % (
        self.co_dni,
        self.no_nombres,
        self.no_apellidopat,
        self.no_apellidomat,
        self.nu_telefono,
        self.tx_correo,
        self.tx_estado,
        self.fe_fechregistro,
        self.co_rucemp,
        )
