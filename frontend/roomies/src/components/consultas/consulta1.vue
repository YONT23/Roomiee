
<template>
    <div id="function" class="container">
        <center>
            <h1>Consulta N° 1</h1>
            <h1>Mostrando Consulta</h1>
        </center>
        <div class="row">
            <div class="alert alert-success" role="alert">
                <center>
                    <p>Mostrar todos los Clientes y la cantidad de hombres, como la de mujeres que hacen parte de
                        Roomies.</p>
                    <button type="button" class="btn btn-primary my-1" onclick="history.back()">Volver</button>
                    <br />
                </center>
            </div>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Clientes Totales</th>
                        <th scope="col">Mujeres</th>
                        <th scope="col">Hombres</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="table-light">
                        <td>{{ c.clientes_totales }}</td>
                        <td>{{ c.clientes_mujeres }}</td>
                        <td>{{ c.clientes_hombres }}</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <div class="alert alert-dismissible alert-info" role="alert">
                Yonatha Mendoza || Roomies.
            </div>
        </div>
        <div class="col-1">

        </div>
    </div>
</template>


<script lang="ts">
import axios from 'axios'
import generatePdf from '../Pdf.vue'
export default {
    data() {
        return {
            c: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/inmueble/consulta1/').then(response => this.c = response.data)
    },
}
</script>

<style scoped lang="css">
h1 {
    justify-content: center;
    justify-items: center;
    left: 60%;
}
</style>