<template>
    <div>
        <edit :cliente="cliente" :submit-data="submitData" />
    </div>
</template>

<script lang="ts">
import { } from "vue-router";
import { PersonasI } from "../../models/personas";
import edit from "./edit.vue";
import { store } from "../../context/cliente";
const cliente: PersonasI = {
    nombre: '',
    apellido: '',
    telefono: '',
    correo: '',
    ciudad: '',
    num_identidad: '',
    tipo_identificacion: 0,
    tipo_sexo: 0,
};
export default {
    data() {
        return {
            cliente: cliente
        }
    },
    methods: {
        submitData(cliente: PersonasI) {
            store.commit('putCliente', { url: "http://localhost:8000/persona/update/" + this.$route.params.id + '/', data: cliente });
            this.$router.push('/clientes');
        }
    },
    mounted() {
        this.$data.cliente = store.state.clienteOwner.find((ser) => ser.id === Number(this.$route.params.id))!;
    },
    components: {
        edit
    }
}
</script>

<style>
</style>