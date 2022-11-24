
<template>
    <div id="function" class="container">
        <center><h1>Consulta N° 2</h1> <h1>Mostrando Consulta</h1></center>
        <div class="row">
            <div class="alert alert-success" role="alert">
                <center>
                    <p>Mostrar Pagos por fecha de los Clientes que hacen parte de Roomies.</p>
                    <button type="button" class="btn btn-primary my-1" onclick="history.back()">Volver</button>
                </center>
            </div>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Pago Fecha </th>
                        <th scope="col">Pago Valor </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="c in cc" :key="c.id" class="table-light">
                        <td>{{c.pago_fecha}}</td>
                        <td>{{c.pago_valor}}</td>
                    </tr>
                </tbody>
            </table>
            <div class="alert alert-dismissible alert-info" role="alert">
                Yonatha Mendoza || Roomies.<br/> 
            </div>
        </div>
        <div class="col-1"></div>
    </div>
</template>


<script lang="ts">
import axios from 'axios'
export default {
    data() {
        return {
            cc: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/inmueble/consulta3/').then(response => this.cc = response.data)
    },
}
</script>

<style scoped lang="css">
h1{
    justify-content: center;
    justify-items: center;
    left: 60%;
}
</style>