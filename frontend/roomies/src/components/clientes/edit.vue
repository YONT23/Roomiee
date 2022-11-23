<template>
    <div class="card card-border-color card-border-color-primary w-75 mx-auto">
        <div class="card-header card-header-divider text-center fs-4">Llena el formulario de personas</div>
        <div class="card-body">
            <div class="form-group">
                <label for="" class="form-label">Nombre</label>
                <input type="text" v-model="cliente.nombre" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Apellido</label>
                <input type="text" v-model="cliente.apellido" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Telefono</label>
                <input type="text" v-model="cliente.telefono" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Correo</label>
                <input type="text" v-model="cliente.correo" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Ciudad</label>
                <input type="text" v-model="cliente.ciudad" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Identificacion</label>
                <input type="text" v-model="cliente.num_identidad" class="form-control" required>
            </div>
            <!-- <div class="form-group">
                <label for="tipo_identificacion" class="form-label">Tipo identificacion</label>
                <select name="tipo_identificacion" id="tipo_identificacion" v-model="cliente.tipo_identificacion"
                    class="form-select">
                    <option :value="''"></option>
                    <template v-for="dep in tipo_identificacion">
                        <option :value="dep['id']">{{ dep['maes_nombre'] }}</option>
                    </template>
                </select>
            </div>
            <div class="form-group">
                <label for="tipo_sexo" class="form-label">Sexo</label>
                <select name="tipo_sexo" id="tipo_sexo" v-model="cliente.tipo_sexo" class="form-select">
                    <option :value="''"></option>
                    <template v-for="dep in tipo_sexo">
                        <option :value="dep['id']">{{ dep['maes_nombre'] }}</option>
                    </template>
                </select>
            </div> -->
            <div class="d-flex flex-row justify-content-around">
                <button class="btn btn-success w-25" onclick="submitData(cliente)">Guardar</button>
                <router-link to="/clientes" class="btn btn-danger w-25">Cancelar</router-link>
            </div>
        </div>
    </div>
</template>

<script  lang="ts">
import { PersonasI } from "../../models/personas";
const persona = {
    nombre: '',
    apellido: '',
    telefono: '',
    correo: '',
    ciudad: '',
    num_identidad: '',
    tipo_identificacion: '',
    tipo_sexo: '',
};
export default {

    props: {
        cliente: {
            type: Object as () => PersonasI,
            required: true
        },
        submitData: {
            type: Function as () => any,

        }
    },
}
</script>

<style scoped>
.card-header {
    background-color: cornflowerblue;
}
</style>