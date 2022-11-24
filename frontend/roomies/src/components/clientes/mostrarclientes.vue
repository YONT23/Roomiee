<template>
    <div id="app">
        <div class="card card-border-color card-border-color-primary w-100 mx-auto">
            <div class="card-header card-header-divider text-center fs-4">PERSONAS
                <p class="lead">Tabla con las personas que hacen parte de Roomies.</p>
                <a position:left href="/nuevoc" class="agregar">Agregar</a>
                <br />
                <button position:left @click="descargarPdf()" class="btn">Imprimir</button>
            </div>
            <table class="table">
                <thead>
                    <tr>
                        <th scoped="col">Nombre</th>
                        <th scoped="col">Apellido</th>
                        <th scoped="col">Ciudad</th>
                        <th scoped="col">Correo</th>
                        <th scoped="col">Identidad</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="persona in personas" :key="persona.id">
                        <td scoped="row">{{ persona.nombre }}</td>
                        <td scoped="row">{{ persona.apellido }}</td>
                        <td scoped="row">{{ persona.ciudad }}</td>
                        <td scoped="row">{{ persona.correo }}</td>
                        <td scoped="row">{{ persona.num_identidad }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import jsPDF from 'jspdf'

export default {
    name: 'pdf',
    data() {
        return {
            personas: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/persona/').then(response => this.personas = response.data)
    },
    el: '#app',
    methods: {
        descargarPdf: function() {
            var pdf = new jsPDF();
            window.print();
            pdf.save('roomies.pdf');
        }
    },
}
</script>

<style scoped>
.center {
    justify-content: center;
    justify-items: center;
}

.table {
    border: 0.3ch;
    border-color: rgb(68, 78, 75);
    border-style: solid;
    font-weight: 500;
    margin: 0;
    padding: 2em;
    text-align: center;
    place-items: center;
}

.th {
    border: 0.2ch
}

.centrar {
    justify-content: center;
    justify-items: center;
}

.agregar {

    box-shadow: 0px 10px 14px -7px #276873;
    background: linear-gradient(to bottom, #599bb3 5%, #408c99 100%);
    background-color: #599bb3;
    border-radius: 8px;
    display: inline-block;
    cursor: pointer;
    color: #ffffff;
    font-family: Arial;
    font-size: 13px;
    font-weight: bold;
    padding: 4px 36px;
    text-decoration: none;
    text-shadow: 0px 1px 0px #3d768a;
}

.agregar:hover {
    background: linear-gradient(to bottom, #408c99 5%, #599bb3 100%);
    background-color: #408c99;
}

.agregar:active {
    position: relative;
    top: 1px;
}
</style>