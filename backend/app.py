# import pyscopg2
from flask import Flask
from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_restful import Resource, Api, fields, marshal_with, abort
from models.models import Empresa, Linea, PersonalAutorizado

app =  Flask(__name__)
app.config.from_pyfile('config.cfg')
api = Api(app)
app.config['DEBUG'] = True

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

#BE CAREFUL: Case sensitive(not like SQL)
empresa_fields = {
    'co_ruc': fields.String,
    'no_razons':  fields.String,
    'no_direccion': fields.String,
    'tx_correo': fields.String,
    'nu_telefono': fields.String,
    'no_rubro': fields.String,
}

personal_autorizado_fields = {
    'co_dni': fields.String,
    'no_nombres': fields.String,
    'no_apellidopat': fields.String,
    'no_apellidomat': fields.String,
    'nu_telefono': fields.String,
    'tx_correo': fields.String,
    'tx_estado': fields.String,
    'fe_fechregistro': fields.String,
    'co_rucemp': fields.String
}

linea_fields = {
    'nu_linea': fields.String,
    'co_idplan': fields.String,
    'nu_estado': fields.String,
    'fe_fechaestado': fields.String,
    'co_rucempresa': fields.String
}

@app.route('/')
def index():
    return 'API working'

class Empresas(Resource):

    @marshal_with(empresa_fields)
    def get(self,empresa_id=None):
        if empresa_id:
            result = session.query(Empresa).filter(Empresa.co_ruc==empresa_id).all()
            if result:
                return result
            else:
                abort(404)
        return session.query(Empresa).all()

    def post(self):
        return "posted"

class Lineas(Resource):
    @marshal_with(linea_fields)
    def get(self,empresa_id=None,nu_linea=None):
        return session.query(Linea).join(Empresa).all()

class PersonasAutorizados(Resource):
    @marshal_with(personal_autorizado_fields)
    def get(self, empresa_id, co_dni=None):
        if co_dni:
            results = session.query(PersonalAutorizado).join(Empresa).filter(
                Empresa.co_ruc==empresa_id,
                PersonalAutorizado.co_dni==co_dni
            ).all()
            if results:
                return results
            else:
                abort(404)
        return session.query(PersonalAutorizado).join(Empresa).filter(
            Empresa.co_ruc==empresa_id,
        ).all()

api.add_resource(Empresas,
                '/empresas',
                '/empresas/<string:empresa_id>')
api.add_resource(Lineas,
                '/empresas/<string:empresa_id>/lineas')
api.add_resource(PersonasAutorizados,
                '/empresas/<string:empresa_id>/personal',
                '/empresas/<string:empresa_id>/personal/<string:co_dni>'
                )

if __name__ == '__main__':
    app.run()
