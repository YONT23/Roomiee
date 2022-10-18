<template>
    <div class="card" style="width: 18rem;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_kymwl1LDd3u13kbTHMQF0YgxYLYVWd9TCpZbwjGtiMFbCEmCLOIaOu8-yeuRgxrsnSU&usqp=CAU" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Servicio: {{y?.persona}}</h5>
          <p class="card-text">Tiene {{i?.baño}} baños, {{i?.serv_internet}} tiene conexion a Internet, {{i?.serv_cocina}} cuenta con su cocina, {{i?.serv_patio}} tiene patio.</p>
        </div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item">Habitaciones: {{i?.habitacion}}</li>
          <li class="list-group-item">DIsponibilidad: {{i?.disponibilidad}}</li>
          <li class="list-group-item">Ubicacion: {{i?.serv_ubicacion}}</li>
          <li class="list-group-item">Huesped: {{i?.huesped}}</li>
        </ul>
    </div>
</template>

<script lang="ts">

import { IServicio } from "../../models/interfaces/serviciointerfaces";
import { IPropietario } from "../../models/interfaces/personainterfaces";

export default {
    props: {
        i: {
            type: Object as () => IServicio
        },
        y: {
            type: Object as () => IPropietario
        }
    },
}

</script>

<style lang="scss">

</style>