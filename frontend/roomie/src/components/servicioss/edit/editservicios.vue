<template>
    <div>
        <Form :servicio="servicio" :submit-data="submitData" />
    </div>
</template>

<script lang="ts">
import { } from "vue-router";
import { IServicio } from "../../../models/interfaces/serviciointerfaces";
import Form from "../../UI/form.vue";

import { store } from "../../../context/store";

const servicio: IServicio = {
    serv_internet: '',
    serv_cocina: '',
    serv_patio: '',
    serv_ubicacion: '',
    habitacion: 0,
    huesped: 0,
    baño: 0,
    disponibilidad: 0
};

export default {

    data() {
        return {
            servicio: servicio
        }
    },
    methods: {
        submitData(servicio: IServicio) {
            store.commit('putServicio', { url: "http://localhost:8000/servicios/update/" + this.$route.params.id + '/', data: servicio });
            this.$router.push('servicios/mine/');
        }
    },
    mounted() {
        this.$data.servicio = store.state.servicioOwner.find((ser) => ser.id === Number(this.$route.params.id))!;
    },
    components: {
        Form
    }
}

</script>

<style>

</style>