<template>
    <div>
        <div class="card">
            <div class="card-body text-center">
                <h2 class="fs-2">Mis Servicios</h2>
            </div>
        </div>
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <template v-for="i in servicio">
            <router-link :to="{name:'updateSer',params:{id:i.id}}">
                <CardServicio :i={...i} />
            </router-link>
        </template>
    </div>
</template>

<script lang="ts" >
import { store } from "../../../context/store";
import CardServicio from "../../UI/card.vue";

export default {
    components: {
        CardServicio
    },
    data() {
        return {
            servicio: [...store.state.servicioOwner]
        }
    },
    mounted() {
        store.commit('getServicio', "http://127.0.0.1:8000/servicios/all/")
    }
}
</script>

<style scoped >

</style>