<template>
    <form @submit.prevent="createPersona">
        <div class="card card-border-color card-border-color-primary w-75 mx-auto">
            <div class="card-header card-header-divider text-center fs-4">Llena el formulario de personas</div>
            <div class="card-body">
                <div class="form-group">
                    <label for="" class="form-label">Nombre</label>
                    <input type="text" v-model="personaData.nombre" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Apellido</label>
                    <input type="text" v-model="personaData.apellido" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Telefono</label>
                    <input type="text" v-model="personaData.telefono" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Correo</label>
                    <input type="text" v-model="personaData.correo" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Ciudad</label>
                    <input type="text" v-model="personaData.ciudad" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="tipo_sexo" class="form-label">Sexo</label>
                    <select>
                        <option v-for="m in maestra">{{m.maes_nombre}}</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Identificacion</label>
                    <input type="text" v-model="personaData.num_identidad" class="form-control" required>
                </div>
                <!-- <div class="form-group">
                    <label for="tipo_identificacion" class="form-label">Tipo identificacion</label>
                    <select name="tipo_identificacion" id="tipo_identificacion" v-model="personaData.tipo_identificacion" class="form-select">
                        <template v-for="dep in tipo_identificacion">
                            <option :value="dep['id']">{{ dep['maes_nombre'] }}</option>
                        </template>
                    </select>
                </div> -->
                <div class="d-flex flex-row justify-content-around">
                    <button class="btn btn-success w-25" >Guardar</button>
                    <router-link to="/clientes" class="btn btn-danger w-25">Cancelar</router-link>
                </div>
            </div>
        </div>

    </form>
</template>
<script lang="ts">
import { } from "vue-router";
import axios from 'axios'

export default {
    data() {
        return {
            personaData: { nombre: '', apellido: '', telefono: '', correo: '',
             ciudad: '', num_identidad: '', tipo_sexo:'' },
            maestra: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/maestra/').then(response => this.maestra = response.data)
    },
    methods:{
        createPersona() {
            axios.post('http://127.0.0.1:8000/persona/create/', this.personaData)
            .then((response) => console.log(response))
        }
    }
}
</script>

<style>

</style>