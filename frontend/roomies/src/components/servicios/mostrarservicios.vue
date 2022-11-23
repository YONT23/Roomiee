<template>

    <div class="card card-border-color card-border-color-primary w-100 mx-auto">
        <div>
            <div class="card w-80 mx-auto">
                <div class="card-body text-center">
                    <h2 class="fs-2">Servicios</h2>
                    <p class="lead">Servicios disponibles en Roomies.</p>
                    <a position:left href="/nuevos" class="agregar">Agregar</a>
                </div>
            </div>
        </div>
        <div position="center" class="card card-transition mx-3" style="max-width: 20rem;cursor: pointer; " v-for="i in is" :key="i.id">
           <div class="hijo">
            <thead>
                <th scoped="col">Servicio {{i.id}}</th>
            </thead>
            <tbody>
                <td>
                    <div class="card" style="width: 19rem;">
                        <img class="card-img-top" :src="i.url_imagenes" alt="Image">
                        <span class="card-pinned-top-end">
                            <span class="badge bg-primary rounded-pill">Estrato: {{ i.estrato }}</span>
                        </span>
                        <div class="card-body">
                            <h3 class="card-title text-center">{{ i.descripcion }}</h3>
                            <p class="card-text text-body my-2">{{ (i as any)?.pais_id.maes_nombre }}</p>
                            <p>{{ i.ciudad }}</p>
                            <div class="card-footer d-flex flex-row justify-content-around p-1">
                                <div class="w-25 text-center">
                                    <small>Superficie</small>
                                    <br>
                                    {{ i.superficie }}
                                </div>
                                <div class="w-25 text-center">
                                    <small>Baños</small>
                                    <br>
                                    {{ i.num_baños }}
                                </div>
                                <div class="w-25 text-center">
                                    <small>Habitaciones</small>
                                    <br>
                                    {{ i.num_habitaciones }}
                                </div>
                            </div>
    
                        </div>
                    </div>
                </td>
            </tbody>
           </div>
        </div>
    </div>

</template>

<script  lang="ts">
import axios from 'axios'

export default {
    data() {
        return {
            is: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/inmueble/').then(response => this.is = response.data)
    }
}
</script>

<style scoped lang="css">
.hijo {
    justify-content: center;
    left: 800px;
    top: 50%;

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

.card-pinned-top-end {
    position: relative;
    top: -10.1rem;
    right: -0.3rem;
}
</style>