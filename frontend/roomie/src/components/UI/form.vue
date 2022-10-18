<template>
    <div class="card card-border-color card-border-color-primary w-75 mx-auto">
        <div class="card-header card-header-divider text-center fs-4">Llena el Formulario de Servicio</div>
        <div class="card-body">
            <div class="form-group">
                <label for="" class="form-label">Internet</label>
                <input type="text" v-model="servicio.serv_internet" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Cocina</label>
                <input type="text" v-model="servicio.serv_cocina" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Patio</label>
                <input type="text" v-model="servicio.serv_patio" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="" class="form-label">Ubicacion</label>
                <input type="text" v-model="servicio.serv_ubicacion" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="habitacion" class="form-label">Habitaciones</label>
                <input type="text" v-model="servicio.habitacion" id="habitacion" class="form-control"
                    required>
            </div>
            <div class="form-group">
                <label for="huesped" class="form-label">Huesped</label>
                <input type="text" v-model="servicio.huesped" id="huesped" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="baño" class="form-label">Baño</label>
                <input type="text" v-model="servicio.baño" id="baño" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="disponibilidad" class="form-label">Disponibilidad</label>
                <input type="text" v-model="servicio.disponibilidad" id="disponibilidad" class="form-control" required>
            </div>
            <div class="d-flex flex-row justify-content-around">
                <button class="btn btn-success w-25" onclick="submitData(servicio)">Guardar</button>
                <router-link to="/servicios/all/" class="btn btn-danger w-25">Cancelar</router-link>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { IServicio } from '../../models/interfaces/serviciointerfaces';
export default {
    props: {
        servicio: {
            type: Object as () => IServicio,
            required: true
        },
        submitData:{
            type: Function as ()=> any,
            
        }
    },
}
</script>

<style>
.card-header{
    background-color: cornflowerblue ;
    color:white;
}
</style>