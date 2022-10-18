<template>
    <Form :servicio="servicio" :submit-data="submitData" />
</template>

<script lang="ts">
import { IServicio } from '../../../models/interfaces/serviciointerfaces';
import Form from '../../UI/form.vue';
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
            store.commit('postServicio', { ...this.$data.servicio, ...servicio });
        }
    },
    components: {
        Form
    }
}

</script>

<style scoped >


</style>