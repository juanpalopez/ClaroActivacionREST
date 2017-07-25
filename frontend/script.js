var apiURL = 'http://localhost/empresas'
var app =  new Vue({
  el: '#app1',
  data: {
    message:'testing',
    empresa_id:'',
    empresas:[],
    dni:'',
    personas:[],
    consultarAlert:false,
    consultableDNI:false,
    autorizadoAlert: false,
    consultadoDNI:false
  },
  created: function () {
    this.mostraEmpresas();
  },
  methods: {
    consultarEmpresa: function () {
      console.log(this.empresa_id)
      axios.get('http://localhost:5000/empresas/' + this.empresa_id)
      .then(res=> {
        this.consultarAlert = false;
        this.consultableDNI = true;
        this.empresas = res.data;
      })
      .catch(error => {
        console.log(error);
        this.consultarAlert = true;
        this.consultableDNI = false;
        this.mostraEmpresas();
      });
    },
    mostraEmpresas: function () {
      axios.get('http://localhost:5000/empresas')
      .then(res => {
        var self =  this;
        this.empresas = res.data;
        this.consultadoDNI = false;
      });
    },
    consultarDNI: function (){
      axios.get('http://localhost:5000/empresas/' + this.empresa_id + '/personal/' + this.dni)
      .then(res => {
        console.log(res.data);
        this.personas = res.data;
        this.consultadoDNI = true;
        this.autorizadoAlert = false;
      })
      .catch(error => {
        console.log(error);
        this.autorizadoAlert = true;
        this.consultadoDNI=false;
        // this.mostrarPersonas();
      });
    },
    mostrarPersonas: function() {
      axios.get('http://localhost:5000/empresas/' + this.empresa_id + '/personal')
      .then(res => {
        this.consultadoDNI = true;
        this.autorizadoAlert = false;
        console.log(res.data);
        this.personas = res.data;
      });
    }
  }
})
